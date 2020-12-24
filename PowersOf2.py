"""
   * author - kajol
   * date - 12/24/2020
   * time - 1:24 PM
   * package - com.bridgelabz.basicprograms
   * Title - Print a table of the powers of 2 that are less than or equal to 2^N
"""
number = int(input("Enter n: "))

if number < 31:
    for i in range(1, number+1):
        print("2 ^", i, "=", 2**i)
else:
    print("Enter number in valid range")

