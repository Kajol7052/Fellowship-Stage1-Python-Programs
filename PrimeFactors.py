"""
   * author - kajol
   * date - 12/24/2020
   * time - 1:35 PM
   * package - com.bridgelabz.basicprograms
   * Title - Print the Prime Factors of a number
"""

num = int(input("Enter a number : "))
for i in range(2, num + 1):
    if num % i == 0:
        prime = True
        for j in range(2, (i // 2 + 1)):
            if i % j == 0:
                prime = False
                break
        if prime:
            print("%d" % i, end=' ')

print("are the prime factors of number", num)
