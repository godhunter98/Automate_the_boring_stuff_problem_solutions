def collatz(number:int):
    if number % 2 ==0:
        result = number//2
    elif number % 2 != 0:
        result = 3 * number + 1
    print(result)
    return result

while True:
    try:
        num = int(input("Enter a number: \n"))
        break
    except ValueError:
        continue

while num !=1:
    num = collatz(num)