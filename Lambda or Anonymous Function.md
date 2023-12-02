# Lambda / Anonymous Function

A lambda function is a special type of function without the function name. 


**Syntax**

```python

variableName = lambda argument(s) : expression
```

**Example**

```python
greet = lambda : print("Welcome to Python Programming")
greet()
```
**Output**

```
Welcome to Python Programming
```

## Example Programs

1. Write a python program to get square of a number with lambda function

```python

squares = lambda num : num*num
print(squares(3))
print(squares(2))
```

2. Check wethere a number or string is palindrome or not using lambda functions

```python
isPalindrome = lambda result : str(result) == str(result)[::-1]

print(isPalindrome("malayalam"))
print(isPalindrome(123))
print(isPalindrome("dog"))
print(isPalindrome(121))
```

3. Create a lambda function that add two values

```python

sums = lambda num1, num2 : num1 + num2
print(sums(10,20))

```