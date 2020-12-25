"""
   * author - kajol
   * date - 12/24/2020
   * time - 4:03 PM
   * package - com.bridgelabz.functionalprograms
   * Title - Calculate the wind chill using given formula
"""
import math
import sys


def wind_chill(temp, vel):
    """
    :param temp: denotes temperature
    :param vel: denotes velocity
    :return:
    """
    power = math.pow(vel, 0.6)
    wind_speed = 35.47 + 0.6215 * temp + (0.4275 * temp + 35.75) * power
    print("The wind chill is: ", wind_speed)


arr = []
for i, arg in enumerate(sys.argv):
    arr.append((arg))
# This is created to calculate wind chills by user input
try:
    temperature = float(arr[1])
    if temperature >= 51:
        print("Enter number below 51")
        exit(1)
    velocity = float(arr[2])
    if velocity <= 4 or velocity >= 121:
        print("Enter number between 3 and 120 ")
        exit(1)
    wind_chill(temperature, velocity)
except ValueError:  # if error is found then below statement will be printed
    print("Check the input")
