data = list(input())
result = list(filter(lambda x: x.lower() not in "aeiou", data))
print("".join(result))