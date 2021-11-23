# To Print numbers from divisible by 5, 7, 11 from 1 to 45
for num in range(1,45+1):
    if num % 5 == 0 and num % 7 == 0  and num % 11 == 0:
        print("given numbers are divisible by all three numbers:",num)
    elif  num % 5 == 0:
        print(" numbers is divisible 5 is :",num)
    elif num % 7== 0:
        print(" numbers is divisible 7 is :",num)
    elif num % 11 == 0:
        print(" numbers is divisible 11 is :", num)
    else:
        print(num)


