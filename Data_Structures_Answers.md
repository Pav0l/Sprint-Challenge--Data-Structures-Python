Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(c) - constant time. I'm accessing the list at a specific index (constant)

2. What is the space complexity of your ring buffer's `append` function?

O(c) - constant space. I'm not taking up any new memory with this method call

3. What is the runtime complexity of your ring buffer's `get` method?

O(n) - linear time. I have to loop through the whole list and remove every `None` value

4. What is the space complexity of your ring buffer's `get` method?

O(n) - Need to create new array of length n (minus the `None`)

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) - nested for loops.

6. What is the space complexity of the provided code in `names.py`?

O(c) = or rather O(2c) as I have to keep track of `name_1` and `name_2`
O(n) - as I'm storing the values from both text files in arrays
final O(n)

7. What is the runtime complexity of your optimized code in `names.py`?

O(n) or more specifically O(2n). As I'm running two for loops in series

8. What is the space complexity of your optimized code in `names.py`?

O(n) - as I'm storing the values from the text files in a dict
