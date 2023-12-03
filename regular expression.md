# Regular Expression (Regex)

A regular expression is a sequence of characters that defines a search pattern.

## RegEx in Python

```python
import re
```

## Functions in RegEx:

### 1. search()

It will return us the match object of the first occurance of the pattern.

**Program**
```python

import re

sentence = "This is a world beautifull world"
pattern = "world"

result = re.search(pattern, sentence)
print(result)
print(result.span())
print(result.group())

```

**Output**

```
<re.Match object; span=(10, 15), match='world'>
(10, 15)
world
```
---

### 2. findall()

It returns all the occurances of the pattern in the string.

**Program**

```python
import re

sentence = "This is a world beautifull world"
pattern = "world"

result = re.findall(pattern, sentence)
print(result)
```

**Output**
```
['world', 'world']
```
---

## Patterns

### 1. Period (.)

A period matches any single character except the newline character (\n).

```python
import re

sentence = "This is a world beautifull world wa cd"
pattern = "w...d"

result = re.findall(pattern, sentence)
print(result)
```

**Output**

```
['world', 'world', 'wa cd']
```

---

### 2. Caret (^)

It is used to check if a string **starts with** a certain pattern

```python
import re

sentence = "This is a world beautifull world wa cd"
pattern = "^T..."

result = re.search(pattern, sentence)
print(result)
```

---


### 3. Dollar ($)

It is used to check if a string **ends with** a certain pattern

```python
import re

sentence = "This is a world beautifull world wa cd"
pattern = "^.d$"

result = re.search(pattern, sentence)
print(result)

sentence = "Td"
pattern = "^.d$"

result = re.search(pattern, sentence)
print(result)
```

**output**

```
None
<re.Match object; span=(0, 2), match='Td'>
```

---


### 4. Star (*)

It matches with **zero or more** occurences of the pattern.

```python
import re

sentence = "mn man maaan main woman"
pattern = "ma*n"

result = re.findall(pattern, sentence)
print(result)
```

**output**

```
['mn', 'man', 'maaan', 'man']
```

---


### 5. Plus (+)

It matches **one or more occurances** of the pattern

```python
import re

sentence = "mn man maaan main woman"
pattern = "ma+n"

result = re.findall(pattern, sentence)
print(result)
```

**output**

```
['man', 'maaan', 'man']
```

---


### 6. Question Mark (?)

It matches **zero or one occurances** of the pattern

```python
import re

sentence = "mn man maaan main woman"
pattern = "ma?n"

result = re.findall(pattern, sentence)
print(result)
```

**output**

```
['mn', 'man', 'man']
```

---


### 7. Braces ({})

```python
import re

sentence = "mn man maaan maaaan main woman"
pattern = "ma{1,3}n"

result = re.findall(pattern, sentence)
print(result)
```

**Output**
```
['man', 'maaan', 'man']
```

---


### 8. Square Brackets []

A set of character you wish for

```python
import re

sentence = "mn mAn min m0n maaan maaaan main woman"
pattern = "m[a-zA-Z0-9]*n"

result = re.findall(pattern, sentence)
print(result)
```

---


## **Example**

### 1. Validate an email

```python
# Email Validation
import re

def validate_email(email):
    pattern = '^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,4}'

    result = re.search(pattern, email)

    if result is not None:
        return True
    else:
        return False

print(validate_email('tharani@guvi.in'))
print(validate_email('tharaniguvi.in'))
print(validate_email('@guvi.in'))
```
