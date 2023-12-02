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