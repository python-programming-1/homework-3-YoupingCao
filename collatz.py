def collatz(num):
    if num <= 0:
        print("Please enter a positive integer")
    if num == 1:
        print(num)
        return num
    while num > 1:
        if num % 2 == 0:
            num = int(num/2)
            print(num)
        else:
            num = int((3 * num) + 1)
            print(num)


try:
    num = int(input("Enter an integer: "))
    collatz(num)
except ValueError:
    print("Invalid input!")
