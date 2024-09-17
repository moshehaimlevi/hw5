# start

diff_temp: int = 0
for _ in range(1, 5 + 1):
    temp: int = int(input("enter the city temp"))
    while not -50 <= temp <= 40:
        temp = int(input('enter temp'))
    else:
        print(f"{temp}is valid")

    diff_temp += temp
print(f"average ={diff_temp / 5}")

# end