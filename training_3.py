class circular_doubly_positional_list:
    '''
    objectives & pardigm : creating circular doubly positional list with wide verstile pardiagm in approaches LIFO-FIFO at same time using the position instance 
    as the tool to interact with the object
    '''

    def _check_dtype(self,data):
        if  isinstance(data,type(None)) :
            raise TypeError("it's not accepted to have data type as None ...except in case of empty list as data type of the spaceholder")

    class _node:
        # the composite the class to represent the nodes we will use in the class 
        def __init__(self,data,next=None):
            self.data=data
            self.next=next
        
        def __repr__(self) -> str:
            return f"{self.data}"

    class _position:
        #composite class ...we use it's instances as interface to deal with the nodes of the list
        def __init__(self,node,container):
            self.node=node
            self.container=container

        def __repr__(self) -> str:
            return f"{self.node}"
        
    
 
    def __init__(self,data=None,next=None):
        self.first=self._node(data,next)
        self.first.next=self.first
        self.curser=self.first
        if self.first.data==None:
            self._size=0
        else:
            self._size=1

    #operations
    def add_first(self,data):
        # adding new data/node to the list handling the two cases of empty & non-empty list 
        self._check_dtype(data)
        if self._size>0:
            new_node=self._node(data,self.first)
            self.curser=new_node
            # reach to the last 
            last=self.first
            for _ in range(self._size-1):
                last=last.next
            last.next=new_node
            self.first=new_node
            self._size+=1

            return self._position(new_node,self)


        else:
            self.first.data=data
            self._size+=1
            return self._position(self.first,self)
    

    def delete_first(self):
        #delete first node with shifting the first node/ reference to the next node in the series
        if self._size>1:
            #save the value
            value=self.first.data
            old_first=self.first

            #getting the last 
            last=self.first

            for _ in range(self._size-1):
                last=last.next
            

            self.first=self.first.next

            last.next=self.first
            self._size-=1
            old_first.next=None
            self.curser=self.first

            return value
        
        elif self._size==1:
            value=self.first.data
            self._size-=1
            self.first.data=None
            self.curser=self.first

            return value
        else:
            return "the list is empty ...no nodes to delete"
        
    def add_after_first(self,data):
        
        if self.size==0:
            return "the list is empty..no first value to insert after it"
        else:
            self._check_dtype(data)
            new_node=self._node(data,self.first.next)
            self.first.next=new_node
            self.curser=new_node
            self._size+=1

            return self._position(new_node,self)
            
        

    def delete_after_first(self):
        # with dealing the first node as the corner of the list here we use it as reference to delete the node after it returning the value of it 
        if self._size==0:
            return "the list already empty ..nothing to delete"
        elif self._size==1:
            return "the list has only one element ...nothing to delete after the first"
            
        else:
            concerned=self.first.next
            value=concerned.data

            self.first.next=concerned.next
            self.curser=self.first
            self._size-=1

            concerned.next=None

            return value


    def add_last(self,data):
        self._check_dtype(data)
        if self._size==0:
            self.first.data=data
            self._size+=1
            self.curser=self.first
        else:
            new_node=self._node(data,self.first)
            last=self.first

            for _ in range(self._size-1):
                last=last.next

            last.next=new_node
            self._size+=1
            self.curser=new_node

            return self._position(new_node,self)

    def delete_last(self):
        if self._size==0:
            return "the list is empty ...no nodes to delete"
        
        elif self._size==1:
            value=self.first.data
            self.first.data=None
            self._size-=1
            self.curser=self.first

            return value
        else:
            pre_last=self.first

            for _ in range(self._size-2):
                pre_last=pre_last.next
            value=pre_last.next.data
            last=pre_last.next

            pre_last.next=self.first
            self.curser=pre_last
            last.data=last.next=None
            self._size-=1

            return value
            


    def change_at_position(self,p,d):
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self:
            self._check_dtype(d)
            p.node.data=d
            self.curser=p.node
            return p
        else:
            raise TypeError("we need position instance to use in this method and that position should be related to the concerned list ")

    def delete_at_position(self,p):
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=None:
            pre_deleted=self.get_position_before(p).node
            concerned_delete=p.node
            next_node=concerned_delete.next
            value =concerned_delete.data


            self.curser=next_node
            pre_deleted.next=next_node
            if concerned_delete==self.first:
                self.first=next_node
            
            concerned_delete.next=concerned_delete.data=None
            self._size-=1

            return value

            

        else:
            raise TypeError("we need position instance to use in this method and that position should be related to the concerned list ")


    def add_after_position(self,p,d):
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=None:
           if self._size>0:
               new_node=self._node(d,p.node.next)
               p.node.next=new_node
               self._size+=1
               self.curser=new_node

               return self._position(new_node,self)

           else:
               return "the list is empty... there is no nodes to insert data after them"
        else:
            raise Exception("there is something wrong in the input")

    def delete_after_position(self,p):
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=None:
            if self._size>0:
                pre_concerned=p.node
                concerned=pre_concerned.next
                next_concerned=concerned.next
                if concerned==self.first:
                    self.first=next_concerned
                pre_concerned.next=next_concerned
                self._size-=1
                self.curser=next_concerned
                value=concerned.data
                concerned.next=concerned.data=None

                return value
            else:
                return "the list is empty... there is no nodes to insert data after them"

        else:
            raise Exception

    def add_before_position(self,p,d):
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=None:
            pre_concerned=self.get_position_before(p).node
            concerned=p.node
            new_node=self._node(d,concerned)
            pre_concerned.next=new_node
            self.curser=new_node
            self._size+=1

            return self._position(new_node)
        else:
            raise Exception 

    def delete_before_position(self,p):
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=None:
            #getting main nodes concerned
            to_delete_position=self.get_position_before(p)
            to_delete_node=to_delete_position.node
            value=to_delete_node.data
            concerned_node=p.node
            new_pre_concerned_node=self.get_position_before(to_delete_position).node

            #changing the pointers & values
            new_pre_concerned_node.next=concerned_node
            if to_delete_node==self.first:
                self.first=concerned_node
            self.curser=concerned_node
            self._size-=1
            to_delete_node.data=to_delete_node.next=None


            return value
            
        else:
            raise Exception 

    def get_position_after(self,p):
        
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=None:
            self.curser=p.node
            return self._position(self.curser,self)
        else:
           raise Exception("to use this method .. the argument should be _position instance ..active associated to this list")
        

    def get_position_before(self,p):
        #get position instance according another specific given position a
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=None:
            concernded=p.node
            for _ in range(self._size-1):
                concernded=concernded.next
            self.curser=concernded
            return self._position(concernded,self)
        else:
           raise Exception("to use this method .. the argument should be _position instance ..active associated to this list")
        

    def search(self,value):
        #search specific value if exists ...return the position represents it 
        if self._size>0:
            curser=self.first
            flag=False
            for _ in range(self._size):
                if type(curser.data)==type(value) and curser.data==value:
                    flag=True
                    break
                else:
                    curser=curser.next
            if flag:
                return self._position(curser,self)
            else:
                return f"{value} doesn't exist"
        else:
            return "the list is empty ...no nodes to search among of them"
    

    def __iter__(self):
        #iteration method 
        point=self.first
        for _ in range(self._size):
            yield point
            point=point.next
        

    def reverse(self):
        if self._size==0:
           return None
        #reversing the list
        
        concerned=self.first.next
        self.first.next=self.get_position_before(self.first_position()).node
        new_first=self.first.next
        new_ref=self.first

        for _ in range(self._size-1):
            virtual_next=concerned.next
            concerned.next=new_ref
            new_ref=concerned

            concerned=virtual_next

        self.first=new_first
        return self


    #info

    def size(self):
        return self._size

    def is_empty(self):
        return self._size==0 

    def __repr__(self) -> str:
       if self._size==0:
           return "none"
       else:
           node_related=self.first
           string="the_list:"

           for _ in range(self._size):
               string=string+"  "+f"({node_related.data})"
               node_related=node_related.next
           return string
       
    def first_node(self):
        #get first node
        return self.first
    
    def first_position(self):
        # get a positon represents the first node
        return self._position(self.first,self)
    

    def last(self):
        #get the last node 
        if self._size>0:

          return self.get_position_before(self.first_position()).node
        else:
            return "the list is already empty"


    def last_position(self):
               #get the last node 
        if self._size>0:

          return self.get_position_before(self.first_position())
        else:
            return "the list is already empty"


    #curser
    def curser_node(self):
        return self.curser

    def position_at_curser(self):
        return self._position(self.curser,self)

    def move_curser_first(self):
        self.curser=self.first

    def move_curser_last(self):
        self.curser=self.last()

    def set_curser(self,p):
        if isinstance(p,circular_doubly_positional_list._position) and p.container==self and p.node.data!=0:
            self.curser=p.node

            return self.curser

        else:
            raise Exception
    
    def add_after_curser(self,d):
        if self._size==0:
            return "no explicit curser...because the list is empty"
        else:
            new_node=self._node(d,self.curser.next)
            self.curser.next=new_node
            self._size+=1

            return self._position(new_node,self)

    def delete_after_curser(self):
        if self._size==0:
            return "this list is empty ...nothing is curser to reference or to delete"
        elif self._size==1:
            return "we just have one element ...no values after curser to delete"
        else:
            new_after_curser=self.curser.next.next
            value=self.curser.next.data

            #changes
            self.curser.next=new_after_curser
            self._size-=1
            self.curser.next.data=self.curser.next.next=None

            return value


    def add_before_curser(self,d):
        if self._size==0:
            return "this list is empty...no curser to use a reference"
        else:
            current_pre_curser_node=self.get_position_before(self.position_at_curser()).node
            new_node=self._node(d,self.curser)
            current_pre_curser_node.next=new_node
            self._size+=1

            return self._position(new_node,self)

    def delete_before_curser(self):
        if self._size==0:
            return "this list is empty...no curser to use a reference"

        elif self._size==1:
            return "we just have one element as a curser ...no other nodes to delete"

        else:
            position_to_delete=self.get_position_before(self.position_at_curser())
            position_new_pre_curser=self.get_position_before(position_to_delete)

            #changes
            position_new_pre_curser.node.next=self.curser
            self._size-=1

            value=position_to_delete.node.data
            position_to_delete.node.data=position_to_delete.node.next=None

            return value

    def move_curser_forward(self,steps):
        for _ in range(steps):
            self.curser=self.curser.next
        return self._position(self.curser,self)

    def move_curser_backward(self,steps):
        for _ in range(steps):
            self.curser=self.curser.next
        return self._position(self.curser,self)



import copy 

class doubly_linked_list:
    '''
    class concerned to create a linked lis t with the techniques and tools of doubly linked list 
    '''

    class _node:

        def __init__(self,data=None,next=None,prev=None):
            self.data=data
            self._next=next
            self._prev=prev


        def __repr__(self) -> str:
            return f"{self.data}"

        def eq(self,second: object) -> bool:
            if type(second)==type(self):
                
                if   self.data==second.data and self._next.data==second._next.data and self._prev.data==second._next.data:
                    return True
                else:
                    return False
            else:
                return  False
        def __ne__(self, second: object) -> bool:
            
            return not self==second


    def __init__(self):
        # initilizing the instance of the class
        self.head=self._node()
        self.tail=self._node()
        self.head._next=self.tail
        self.tail._prev=self.head
        self._size=0


    def eq(self,first,second):
       

            if isinstance(second,doubly_linked_list._node) and isinstance(first,doubly_linked_list._node):
                
               if first._next==second._next:
                   if first._prev==second._prev:
                       if first.data==second.data:
                         return True
                       else:
                          return False
                   else:
                     return  False
               else:
                  return False
            else:
              return  False
        
    def not_eq(self,first,second):
        return not self.eq(first,second)
    
    
    #operations

    def add_first(self,data):
        #adding new node at the beginning of the list 
        new_node=self._node(data,self.head._next,self.head)
        self.head._next._prev=new_node
        self.head._next=new_node
        self._size+=1

    def delete_first(self):
        # delete the first node in the list 
      if self._size!=0:
        concerned=self.head._next
        value=concerned.data
        new_first=concerned._next

        self.head._next=new_first
        new_first._prev=self.head
        self._size-=1
        concerned._next=concerned._prev=concerned.data=None

        return value
      else:
          return "the list empty nothing to delete"
    

    def add_last(self,data):
        # add new new at the last point 
        new_node=self._node(data,self.tail,self.tail._prev)

        #updating the pointers 
        self.tail._prev._next=new_node
        self.tail._prev=new_node
        self._size+=1 

    def delete_last(self):
      if self._size!=0:
        new_last=self.tail._prev._prev
        concerned=self.tail._prev
        value=concerned.data


        new_last._next=self.tail
        self.tail._prev=new_last
        self._size-=1

        return value 
      else:
          return "it's empty nothing to delete"

    def add_at_index(self,data,index):
        if 0<index and  index<=self._size:
            curser=self.head
            for _ in range(index):
                curser=curser._next
            
            new_node=self._node(data,curser,curser._prev)
            curser._prev._next=new_node
            curser._prev=new_node
            self._size+=1
            
        else:
            return "this index doesn't exist in the list"

    def delete_at_index(self,index):
        if 0<index and index<=self._size:
            curser=self.head
            for _ in range(index):
                curser=curser._next
            value=curser.data
            pre_curser=curser._prev
            after_curser=curser._next
            pre_curser._next=after_curser
            after_curser._prev=pre_curser
            self._size-=1

            curser._next=curser._prev=curser.data=None

            return value
        else:
            raise IndexError


    def swap_values(self,index1,index2):
        if 0<index1<=self._size and 0<index2<=self._size:
            self.get_node_at_index(index1).data,self.get_node_at_index(index2).data=self.get_node_at_index(index2).data,self.get_node_at_index(index1).data
            return self
        else:
            raise IndexError

    def swap_nodes(self,index1,index2):
        if 0<index1<=self._size and 0<index2<=self._size and index1!=index2:
            if abs(index1-index2)==1:#consecutive case
                if index1<index2:
                    first=self.get_node_at_index(index1)
                    second=self.get_node_at_index(index2)

                    pre_first=first._prev
                    after_second=second._next

                    pre_first._next=second
                    second._prev=pre_first
                    first._next=after_second
                    after_second._prev=first

                    return self
                else:
                    first=self.get_node_at_index(index2)
                    second=self.get_node_at_index(index1)
                    
                    pre_first=first._prev
                    after_second=second._next

                    pre_first._next=second
                    second._prev=pre_first
                    first._next=after_second
                    after_second._prev=first

                    return self

            elif abs(index1-index2)==2:#with one mutual node
                if index1<index2:
                    first=self.get_node_at_index(index1)
                    second=self.get_node_at_index(index2)

                    pre_first=first._prev
                    mutual=first._next
                    after_second=second._next


                    #changing the pointers 
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=mutual
                    mutual._prev=second

                    mutual._next=first
                    first._prev=mutual
                    first._next=after_second
                    after_second._prev=first

                    return self
                else:
                    first=self.get_node_at_index(index2)
                    second=self.get_node_at_index(index1)

                    pre_first=first._prev
                    mutual=first._next
                    after_second=second._next


                    #changing the pointers 
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=mutual
                    mutual._prev=second

                    mutual._next=first
                    first._prev=mutual
                    first._next=after_second
                    after_second._prev=first

                    return self
            
            else:
                if index1<index2:
                    first=self.get_node_at_index(index1)
                    second=self.get_node_at_index(index2)

                    pre_first=first._prev
                    after_first=first._next
                    pre_second=second._prev
                    after_second=second._next
                    
                    #change the pointers
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=after_first
                    after_first._prev=second

                    pre_second._next=first
                    first._prev=pre_second
                    first._next=after_second
                    after_second._prev=first

                    return self
                else:
                    
                    first=self.get_node_at_index(index2)
                    second=self.get_node_at_index(index1)

                    pre_first=first._prev
                    after_first=first._next
                    pre_second=second._prev
                    after_second=second._next
                    
                    #change the pointers
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=after_first
                    after_first._prev=second

                    pre_second._next=first
                    first._prev=pre_second
                    first._next=after_second
                    after_second._prev=first

                    return self

        else:
            raise IndexError


    def reverse(self):
        #method to reverse the nodes of the list 
        if self._size<=1:
            return self
        else:
            end=self.tail
            ref=self.tail._prev
            concerned=self.head._next
            new_concerned=concerned._next

            while concerned!=ref:
                concerned._next=end
                end._prev=concerned

                end=concerned
                concerned=new_concerned
                new_concerned=concerned._next

            self.head._next=ref
            ref._prev=self.head
            ref._next=end
            end._prev=ref
            return self

    def merge_no_change(self,second):
        self_list=copy.deepcopy(self)
        second_list=copy.deepcopy(second)

        self_list.last()._next=second_list.first()
        second_list.first()._prev=self_list.last()

        self_list._size+=second_list._size

        return self_list

    def merge_with_change(self,second):
        second_list=copy.deepcopy(second)
        self.last()._next=second_list.first()
        second_list.first()._prev=self.last()

        self.tail._next=None

        self._size+=second_list._size

        return self
    def search(self,data):
        # return the node of the data 
        if self._size==0:
            return "the list is empty"
        else:
            curser=self.head._next
            flag= False

            for _ in range(self._size):
                if curser.data==data:
                    flag= True
                    return curser
                else:
                    curser=curser._next
            if not flag:
                return "there is no such value in the list "
    #info 

    def get_node_at_index(self,index):
         if 0<index and  index<=self._size:
            curser=self.head
            for _ in range(index):
                curser=curser._next
            
            return curser 
            
         else:
            return "this index doesn't exist in the list"

    def first(self):
        return self.head._next

    def last(self):
        return self.tail._prev

    def size(self):
        return self._size

    def __repr__(self) -> str:
        
            string="head"
            curser=self.head._next
            for _ in range(self._size):
                string=string+"-->"+f"({curser})"
                
                curser=curser._next
            string=string+"-->tail"
            return string
    

    def __iter__(self):
        curser=self.head
        for _ in range(self._size):
            yield curser._next
            curser=curser._next

    def is_empty(self):
        return self._size==0
    
x=doubly_linked_list()


for i in range(10,0,-1):
    x.add_first(i)


print(x)
x.add_at_index(500,5)


print(x)
print(x.delete_first())
print(x.delete_last())
print(x)
x.add_last(1000)
print(x)
print(x.delete_at_index(4))
print(x)
x.swap_values(4,x._size)
print(x)
x.swap_nodes(4,x._size)
print(x)
print(x.search(1001))
print(x.reverse())
y=doubly_linked_list()
y.add_first(5)
y.add_first(6)
print(y)
print(y.reverse())

a=[1,2,3,4,5]
b=a[3:]

b.append(6)
print(a,b)
del b[0]
print(a,b)
print(x.add_at_index(5647,-1))
print(x)

n=iter(x)
z=iter(x)
x.head._next.data=000
print(x)
print(next(n))# we want to test it in case of nested class 




class doubly_linked_list200:
    '''
    concerned to create a linked lis t with the techniques and tools of doubly linked list 
    '''

    class _node:

        def __init__(self,data=None,next=None,prev=None):
            self.data=data
            self._next=next
            self._prev=prev


        def __repr__(self) -> str:
            return f"{self.data}"

        def eq(self,second: object) -> bool:
            if type(second)==type(self):
                
                if   self.data==second.data and self._next.data==second._next.data and self._prev.data==second._next.data:
                    return True
                else:
                    return False
            else:
                return  False
        def __ne__(self, second: object) -> bool:
            
            return not self==second


    def __init__(self):
        # initilizing the instance of the class
        self.head=self._node()
        self.tail=self._node()
        self.head._next=self.tail
        self.tail._prev=self.head
        self._size=0


    def eq(self,first,second):
       

            if isinstance(second,doubly_linked_list._node) and isinstance(first,doubly_linked_list._node):
                
               if first._next==second._next:
                   if first._prev==second._prev:
                       if first.data==second.data:
                         return True
                       else:
                          return False
                   else:
                     return  False
               else:
                  return False
            else:
              return  False
        
    def not_eq(self,first,second):
        return not self.eq(first,second)
    
    
    #operations

    def add_first(self,data):
        #adding new node at the beginning of the list 
        new_node=self._node(data,self.head._next,self.head)
        self.head._next._prev=new_node
        self.head._next=new_node
        self._size+=1

    def delete_first(self):
        # delete the first node in the list 
      if self._size!=0:
        concerned=self.head._next
        value=concerned.data
        new_first=concerned._next

        self.head._next=new_first
        new_first._prev=self.head
        self._size-=1
        concerned._next=concerned._prev=concerned.data=None

        return value
      else:
          return "the list empty nothing to delete"
    

    def add_last(self,data):
        # add new new at the last point 
        new_node=self._node(data,self.tail,self.tail._prev)

        #updating the pointers 
        self.tail._prev._next=new_node
        self.tail._prev=new_node
        self._size+=1 

    def delete_last(self):
      if self._size!=0:
        new_last=self.tail._prev._prev
        concerned=self.tail._prev
        value=concerned.data


        new_last._next=self.tail
        self.tail._prev=new_last
        self._size-=1

        return value 
      else:
          return "it's empty nothing to delete"

    def add_at_index(self,data,index):
        if 0<index and  index<=self._size:
            curser=self.head
            for _ in range(index):
                curser=curser._next
            
            new_node=self._node(data,curser,curser._prev)
            curser._prev._next=new_node
            curser._prev=new_node
            self._size+=1
            
        else:
            return "this index doesn't exist in the list"

    def delete_at_index(self,index):
        if 0<index and index<=self._size:
            curser=self.head
            for _ in range(index):
                curser=curser._next
            value=curser.data
            pre_curser=curser._prev
            after_curser=curser._next
            pre_curser._next=after_curser
            after_curser._prev=pre_curser
            self._size-=1

            curser._next=curser._prev=curser.data=None

            return value
        else:
            raise IndexError


    def swap_values(self,index1,index2):
        if 0<index1<=self._size and 0<index2<=self._size:
            self.get_node_at_index(index1).data,self.get_node_at_index(index2).data=self.get_node_at_index(index2).data,self.get_node_at_index(index1).data
            return self
        else:
            raise IndexError

    def swap_nodes(self,index1,index2):
        if 0<index1<=self._size and 0<index2<=self._size and index1!=index2:
            if abs(index1-index2)==1:#consecutive case
                if index1<index2:
                    first=self.get_node_at_index(index1)
                    second=self.get_node_at_index(index2)

                    pre_first=first._prev
                    after_second=second._next

                    pre_first._next=second
                    second._prev=pre_first
                    first._next=after_second
                    after_second._prev=first

                    return self
                else:
                    first=self.get_node_at_index(index2)
                    second=self.get_node_at_index(index1)
                    
                    pre_first=first._prev
                    after_second=second._next

                    pre_first._next=second
                    second._prev=pre_first
                    first._next=after_second
                    after_second._prev=first

                    return self

            elif abs(index1-index2)==2:#with one mutual node
                if index1<index2:
                    first=self.get_node_at_index(index1)
                    second=self.get_node_at_index(index2)

                    pre_first=first._prev
                    mutual=first._next
                    after_second=second._next


                    #changing the pointers 
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=mutual
                    mutual._prev=second

                    mutual._next=first
                    first._prev=mutual
                    first._next=after_second
                    after_second._prev=first

                    return self
                else:
                    first=self.get_node_at_index(index2)
                    second=self.get_node_at_index(index1)

                    pre_first=first._prev
                    mutual=first._next
                    after_second=second._next


                    #changing the pointers 
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=mutual
                    mutual._prev=second

                    mutual._next=first
                    first._prev=mutual
                    first._next=after_second
                    after_second._prev=first

                    return self
            
            else:
                if index1<index2:
                    first=self.get_node_at_index(index1)
                    second=self.get_node_at_index(index2)

                    pre_first=first._prev
                    after_first=first._next
                    pre_second=second._prev
                    after_second=second._next
                    
                    #change the pointers
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=after_first
                    after_first._prev=second

                    pre_second._next=first
                    first._prev=pre_second
                    first._next=after_second
                    after_second._prev=first

                    return self
                else:
                    
                    first=self.get_node_at_index(index2)
                    second=self.get_node_at_index(index1)

                    pre_first=first._prev
                    after_first=first._next
                    pre_second=second._prev
                    after_second=second._next
                    
                    #change the pointers
                    pre_first._next=second
                    second._prev=pre_first
                    second._next=after_first
                    after_first._prev=second

                    pre_second._next=first
                    first._prev=pre_second
                    first._next=after_second
                    after_second._prev=first

                    return self

        else:
            raise IndexError


    def reverse(self):
        #method to reverse the nodes of the list 
        if self._size<=1:
            return self
        else:
            end=self.tail
            ref=self.tail._prev
            concerned=self.head._next
            new_concerned=concerned._next

            while concerned!=ref:
                concerned._next=end
                end._prev=concerned

                end=concerned
                concerned=new_concerned
                new_concerned=concerned._next

            self.head._next=ref
            ref._prev=self.head
            ref._next=end
            end._prev=ref
            return self

    def merge_no_change(self,second):
        self_list=copy.deepcopy(self)
        second_list=copy.deepcopy(second)

        self_list.last()._next=second_list.first()
        second_list.first()._prev=self_list.last()

        self_list._size+=second_list._size

        return self_list

    def merge_with_change(self,second):
        second_list=copy.deepcopy(second)
        self.last()._next=second_list.first()
        second_list.first()._prev=self.last()

        self.tail._next=None

        self._size+=second_list._size

        return self
    def search(self,data):
        # return the node of the data 
        if self._size==0:
            return "the list is empty"
        else:
            curser=self.head._next
            flag= False

            for _ in range(self._size):
                if curser.data==data:
                    flag= True
                    return curser
                else:
                    curser=curser._next
            if not flag:
                return "there is no such value in the list "
    #info 

    def get_node_at_index(self,index):
         if 0<index and  index<=self._size:
            curser=self.head
            for _ in range(index):
                curser=curser._next
            
            return curser 
            
         else:
            return "this index doesn't exist in the list"

    def first(self):
        return self.head._next

    def last(self):
        return self.tail._prev

    def size(self):
        return self._size

    def __repr__(self) -> str:
        
            string="head"
            curser=self.head._next
            for _ in range(self._size):
                string=string+"-->"+f"({curser})"
                
                curser=curser._next
            string=string+"-->tail"
            return string
    class _iter:
        def __init__(self,positional_list):
            self.positional_list=positional_list
            self._current=self.positional_list.first()

        def __iter__(self):
            return self
        
        def __next__(self):
            if not self._current:
                raise StopIteration
            element=self._current.data
            self._current=self._current._next
            return element

    def __iter__(self):
        return self._iter(self)

    def is_empty(self):
        return self._size==0


print("\n")

x=doubly_linked_list200()


for i in range(10,0,-1):
    x.add_first(i)

x.add_at_index(500,5)



(x.delete_first())
(x.delete_last())
x.add_last(1000)

(x.delete_at_index(4))

x.swap_values(4,x._size)

x.swap_nodes(4,x._size)


print(x.reverse())
y=doubly_linked_list()
y.add_first(5)
y.add_first(6)

print(y.reverse())


print(x.add_at_index(5647,-1))
print(x)

n=iter(x)
z=x._iter(x)

x.head._next.data=000
print(x)

