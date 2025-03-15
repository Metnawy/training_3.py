

This repository contains Python implementations of a **Circular Doubly Positional List** and a **Doubly Linked List**. These data structures are designed to handle various operations such as adding, deleting, and swapping elements, as well as iterating through the list.

## Classes and Methods

### `circular_doubly_positional_list`

- **`add_first(data)`**: Adds an element to the beginning of the list.
- **`delete_first()`**: Deletes the first element in the list.
- **`add_last(data)`**: Adds an element to the end of the list.
- **`delete_last()`**: Deletes the last element in the list.
- **`add_after_position(p, data)`**: Adds an element after a specified position.
- **`delete_after_position(p)`**: Deletes the element after a specified position.
- **`add_before_position(p, data)`**: Adds an element before a specified position.
- **`delete_before_position(p)`**: Deletes the element before a specified position.
- **`change_at_position(p, data)`**: Changes the data at a specified position.
- **`delete_at_position(p)`**: Deletes the element at a specified position.
- **`search(value)`**: Searches for a value in the list and returns its position.
- **`reverse()`**: Reverses the list.
- **`size()`**: Returns the size of the list.
- **`is_empty()`**: Checks if the list is empty.
- **`first_position()`**: Returns the position of the first node.
- **`last_position()`**: Returns the position of the last node.
- **`__iter__()`**: Allows iteration over the list.

### `doubly_linked_list`

- **`add_first(data)`**: Adds an element to the beginning of the list.
- **`delete_first()`**: Deletes the first element in the list.
- **`add_last(data)`**: Adds an element to the end of the list.
- **`delete_last()`**: Deletes the last element in the list.
- **`add_at_index(data, index)`**: Adds an element at a specific index.
- **`delete_at_index(index)`**: Deletes the element at a specific index.
- **`swap_values(index1, index2)`**: Swaps the values at two specified indices.
- **`swap_nodes(index1, index2)`**: Swaps the nodes at two specified indices.
- **`reverse()`**: Reverses the list.
- **`merge_no_change(second)`**: Merges two lists without modifying the original lists.
- **`merge_with_change(second)`**: Merges two lists, modifying the original list.
- **`search(data)`**: Searches for a value in the list and returns the node.
- **`size()`**: Returns the size of the list.
- **`is_empty()`**: Checks if the list is empty.
- **`__iter__()`**: Allows iteration over the list.

## Usage

To use the classes and methods, simply import the script and create instances of the desired classes. Here is an example:

```python
from training_3 import circular_doubly_positional_list, doubly_linked_list

# Example usage of circular_doubly_positional_list
cdpl = circular_doubly_positional_list()
cdpl.add_first(10)
cdpl.add_last(20)
print(cdpl)

# Example usage of doubly_linked_list
dll = doubly_linked_list()
dll.add_first(10)
dll.add_last(20)
print(dll)
```

## Notes

- The `circular_doubly_positional_list` class supports operations like adding, deleting, and swapping elements using positional references.
- The `doubly_linked_list` class supports similar operations but uses indices for element access and manipulation.
- Both classes support iteration, allowing you to loop through the elements in the list.
