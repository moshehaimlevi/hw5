# start

num: int = int(input("Enter a number"))

for i in range(1, num * 1, 2):
    print("  " * ((num * 1 - i) // 2), end="  ")
    print( "$ " * i )
print()
