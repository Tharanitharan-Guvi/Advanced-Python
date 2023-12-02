# Filter Function

A filter function chooses elements from an iterator i.e list, tuple or set and return us data based on it

**Syntax**

```python

filter(function_name, iterator)
```

**Examples**

1. using filter() function create a new list which are even

```python

data = [1,2,3,4,5,6,7,8,9,10]
output = list(filter(lambda num: num%2 == 0, data))
print(output)
```

2. Using filter() function to remove all the negative numbers

```python

data = [-1,-2, 10, 20, 30 ,-40, 2]
output = list(filter(lambda num: num>=0, data))
print(output)
```

3. Remove all the vowels from a string using filter()

```python
data = list(input())
result = list(filter(lambda x: x.lower() not in "aeiou", data))
print("".join(result))
```
