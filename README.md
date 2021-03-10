# pyPtr
 Pointers for Python

## Usage
 To create a new `Pointer`:
 ```python
 import ptr

 num: int = 10
 num_pointer: ptr.Pointer = ptr.Pointer(num)
 ```

 To get the address and value that the pointer points to:
 ```python
 num_pointer_address: int = num_pointer.getAddress()
 num_pointer_value: int = num_pointer.getVal()
 ```
 
 To perform calculations:
 ```python
 # += and -=
 num_pointer.increment()
 num_pointer_value_after_plus_equals: int = num_pointer.getVal()

 num_pointer.decrement()
 num_pointer_value_after_minus_equals: int = num_pointer.getVal()


 # + and -
 num_pointer.add(10)
 num_pointer_value_after_plus: int = num_pointer.getVal()

 num_pointer.sub(15)
 num_pointer_value_after_minus: int = num_pointer.getVal()


 # ==, !=, <, >, <= and >=
 other: int = 15
 other_pointer: ptr.Pointer = ptr.Pointer(other)

 are_addresses_equal: bool = num_pointer.eqeq(other_pointer)
 are_addresses_equal: bool = num_pointer.ne(other_pointer)
 are_addresses_equal: bool = num_pointer.gt(other_pointer)
 are_addresses_equal: bool = num_pointer.lt(other_pointer)
 are_addresses_equal: bool = num_pointer.lte(other_pointer)
 are_addresses_equal: bool = num_pointer.gte(other_pointer)
 ```