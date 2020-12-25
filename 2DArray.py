"""
   * author - kajol
   * date - 12/24/2020
   * time - 4:02 PM
   * package - com.bridgelabz.functionalprograms
   * Title - Print 2 Dimensional array
"""


def array_2d(row, col):
    """

    :param row: denotes number of rows
    :param col: denotes number of columns
    :return:
    """
    try:
        array = []
        for i in range(row):
            temp_array = []
            for j in range(col):
                number = int(input("Enter any number: "))
                temp_array.append(number)
            array.append(temp_array)
        print(array)
    except IndexError:
        print("Index error please check ")


row = int(input("Enter number of rows: "))
if row <= 0 or row >= 100:
    print("Enter valid input for row")
col = int(input("Enter number of cols: "))
if col <= 0 or col >= 100:
    print("Enter valid input for col")
array_2d(row, col)