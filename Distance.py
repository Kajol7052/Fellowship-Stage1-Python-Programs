"""
   * author - kajol
   * date - 12/24/2020
   * time - 4:03 PM
   * package - com.bridgelabz.functionalprograms
   * Title - Prints the Euclidean distance from the point (x, y) to the origin (0, 0)
"""
import math


def distance(x1, y1):
    """
    :param x1: X value
    :param y1: Y value
    :return:
    """
    diff = math.sqrt((x1 ** 2 + y1 ** 2))
    print(diff)


x = int(input("enter num 1 : "))
if x <= 0 or x >= 1000:
    print("enter the number between 0 and 1000")
    exit(1)
y = int(input("enter num 2 : "))
if y <= 0 or y >= 1000:
    print("enter the number between 0 and 1000")
    exit(1)
distance(x, y)
