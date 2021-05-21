def input_func():
    while True:
        number = input("Write a number! : ")
        entery = number.isdigit()
        if entery:
            return int(number)

a = input_func()
# print (a)
if a > 1:
    for i in range(2, a):
        if a % i == 0:
            print (a, "is not a prime number")
            break
        else:
            print (a, "is a prime number")
            break
else: 
    print (a, "is not a prime number")                 

        


