# Exceptions

Errors that occur at runtime are called exceptions or logical errors.

## Examples:

```python
a = [1,2,3]
print(a[3])
```
**Output**:
IndexError: list index out of range

```python
dict = {"India": "Delhi"}
print(dict["London"])
```
**Output**:
KeyError: 'London'

## List of other builtin exceptions
1. ZeroDivisionError - Raised when the second operand of division or modulo operation is zero

2. ValueError - Raised when a function gets an argument of correct type but improper value.

3. TypeError - Raised when a function or operation is applied to an object of incorrect type.

4. NameError - Raised when a variable is not found in local or global scope.

5. KeyError - Raised when a key is not found in a dictionary.

6. IndexError - Raised when the index of a sequence is out of range.


# Exception Handling

It is nothing but handling the exceptions raised while running our program. In python we use,

```python

try:
    # code that may cause exception 
except:
    # code to run when an exception occurs
```


**Example**

```python

while True:
    try:
        numerator = int(input())
        denominator = int(input())
        print(numerator / denominator)
        break
    except ZeroDivisionError:
        print("Error: You should not give 0 to the denominator")
    except ValueError:
        print("Enter values only in digits i.e 0-9")

```

**Output**
```
ten 
Enter values only in digits i.e 0-9
10
0
Error: You should not give 0 to the denominator
10
2
5.0
```

## Try Except Block with else clause

We might want to run a certain block of code if there are no errors occured inside the try block.

**Example**

```python

while True:
    try:
        numerator = int(input())
        denominator = int(input())
        print(numerator / denominator)
    except ZeroDivisionError:
        print("Error: You should not give 0 to the denominator")
    except ValueError:
        print("Enter values only in digits i.e 0-9")
    else:
        break
```

**Output**

```
ten 
Enter values only in digits i.e 0-9
10
0
Error: You should not give 0 to the denominator
10
2
5.0
```

## Python Try ... Finally

The finally block is always executed no matter whether there is an exception or not. This is also optional.

**Example**

```python

while True:
    try:
        numerator = int(input())
        denominator = int(input())
        print(numerator / denominator)
    except ZeroDivisionError:
        print("Error: You should not give 0 to the denominator")
    except ValueError:
        print("Enter values only in digits i.e 0-9")
    else:
        break
    finally:
        print("This will be always executed")

```

**Output**

```
ten
Enter values only in digits i.e 0-9
This will be always executed
10
0
Error: You should not give 0 to the denominator
This will be always executed
10
2
5.0
This will be always executed
```

# User - Defined Exceptions

We can define custom exceptions by creating a new class that is derived from the builtin Exception class.

**Syntax**

```python
class ClassNameError(Exception):
    pass

try:
    pass
except ClassNameError:
    pass
```

**Example**

```python


class CheckAge(Exception):
    def __init__(self):
        self.msg = "The age should should not be less than 18"
    
    def __str__(self):
        return self.msg


while True:
    try:
        age = int(input())
        if age < 18:
            raise CheckAge()
    except ValueError:
        print("Enter values only in digits i.e 0-9")
    except CheckAge as e:
        print(e)
    else:
        break

```

**Output**

```
17  
The age should should not be less than 18
10
The age should should not be less than 18
0
The age should should not be less than 18
19
```