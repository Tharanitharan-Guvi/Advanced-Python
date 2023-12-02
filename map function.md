# Map Function

- Map function is a kind of function which is applied to each and every element of a iterator ie List, Tuple, sets.

**Syntax**

```python

map(function_name, iterator)
```


**1. Example**

```python

def squares(num):
    return num*num

arr = [1,2,3,4,5]
output = list(map(squares, arr))
print(output)
```

**Output**

```
[1, 4, 9, 16, 25]
```

**2. Example**

You need to get muliple values from a single line

```python
arr = list(map(int, input().split()))
print(arr)
```

**3. Example**

```python

def toUpper(inp):
    return inp.upper()

data = ['python', 'programming']
print(list(map(toUpper, data)))
print(list(map(lambda inp: inp.upper(), data)))
print(list(map(str.upper, data)))
```