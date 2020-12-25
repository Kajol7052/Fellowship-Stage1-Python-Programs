"""
   * author - kajol
   * date - 12/24/2020
   * time - 1:17 PM
   * package - com.bridgelabz.basicprograms
   * Title - Print the Nth Harmonic Number
"""
try:
    number = int(input("Enter the value of n : "))
    s = 0.0
    for i in range(1, number + 1):
        s = s + 1 / i
    print("Sum is: ", round(s, 3))
except IOError:
    print("Exception occurred ", IOError)
