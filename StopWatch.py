"""
   * author - kajol
   * date - 12/25/2020
   * time - 10:30 AM
   * package - com.bridgelabz.logicalprograms
   * Title - Stopwatch Program for measuring the time that elapses between the start and end clicks
"""

from datetime import datetime


class StopWatch:

    def stop_watch(self):
        """
        :return:
        """
        start = datetime.now()
        input("Please enter to stop the program.")
        end = datetime.now()
        print(abs(end - start))


if __name__ == '__main__':
    caller = StopWatch()
    caller.stop_watch()
