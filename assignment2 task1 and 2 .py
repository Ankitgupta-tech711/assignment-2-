#TASK 1

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


#TASK 2
    sum = 0
    for i in range(1, 51):
        sum += i

    print("The sum of the first 50 odd numbers is:", sum)