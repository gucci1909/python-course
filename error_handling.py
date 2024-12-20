a = input('Enter a number')
print("Multiplication table")

try:
    for i in range(1, 11):
        print(f"{int(a)*i}")
except Exception as e:
    print("Some error occurred, invalid input")
    
    
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")