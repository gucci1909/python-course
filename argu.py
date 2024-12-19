def average(a=2,b=34):
    print("the average of a and b", (a+b)/2)
    
average(b=4)

# tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# *numbers this is tuple

def average_1(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Average is: ", sum/len(numbers))
    
# I can write as many as numbers as I want
average_1(1,24,44)

# **names are dict
# def name(**names)

