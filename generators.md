# Iterators

Iterators are methods that iterate/loops through the collections like list, tuples, etc. 

Technically, in python they would have implemented two special methods, **__iter__()** and the **__next__()**


**Examples**

```python
class One2N:
    def __init__(self, n=1):
        self.start = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.n:
            self.start += 1
            return self.start
        else:
            raise StopIteration

a = One2N(10)
for i in a:
    print(i)
```

# Generators

Generators is a function that return an iterator.

Generators are useful when we want to produce a large sequences of values, but we don't want to store all of them in memory at once. 


**Syntax**

```python
def generator_name(arguments):
    # statements
    yield value
```

Instead of using return statement, you should use the yeild statement


**Examples**

1. To create an iterator which gets values from 1 to n.

```python
def one2N(n):
    for i in range(1, n+1):
        yield i

for i in one2N(10):
    print(i)
```

2. write a generator for squares of a number.

```python
def squares(num):
    i = 1

    while i <= num:
        yield i**2 # i*i
        i += 1 # i = i + 1

for i in squares(10):
    print(i)
```

3. write a generator for fibonnaci series

```python
def fibonnaci(n):
    f1 = 0
    f2 = 1

    for i in range(1, n+1):
        yield f1
        f1, f2 = f2, f1+f2

for i in fibonnaci(10):
    print(i)
```