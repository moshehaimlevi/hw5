# start

# 1

height: float = float(input("enter a height"))

while height <= 0.4 or height >= 2.5:
    print('wrong input')
    height: float = float(input("enter a height"))

# 2

x: int = int(input('whats the number?'))
for i in range(4, x + 1, 1):
    print(i, end=" ")
print()

# 3
counter: int = 1

pi: float = float(input('enter the correct number'))

while pi != 3.14 and counter < 3:
    counter += 3
    print('incorrect number')
    pi = float(input("enter the correct number"))

if pi <= 3.14:
    print("incorrect!")
else:
    print(f"the number is correct")

# 4

while True:
    number1: int = int(input("number1:"))
    number2: int = int(input("number2:"))
    number3: int = int(input("number3:"))
    avg_grades = (number1 + number2 + number3) / 3
    if 0 <= number1 <= 10 and 10 <= number2 <= 60 and 60 <= number3 <= 100 \
            and avg_grades and not number1 == number2 == number3:
        break

    print(f"Valid input. The average of the numbers is: {avg_grades / 3}")
    break





# end
