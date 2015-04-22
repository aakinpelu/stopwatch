#
# CSC 161 Spring 2015
#
# Akinniyi Akinpelu
#
# Object-Oriented Design Assignment
#
# Lab Section MW 3:25-4:40pm
#

import time
import datetime

class StopWatch:

    def __init__(self, start):
        self.start = start

    def getStartTime(self):
        return datetime.datetime.fromtimestamp(self.start, tz=None)

    def getEndTime(self):
        return self.currentEnd

    def start(self, currentStart):
        self.start = currentStart

    def stop(self, currentEnd):
        self.currentEnd = currentEnd

    def getElapsedTime(self):
        elapsed = self.currentEnd - datetime.datetime.fromtimestamp(self.start, tz=None)
        return elapsed

def main():
    stopWatch = StopWatch(time.time())
    print("Stopwatch started at", stopWatch.getStartTime())

    sum = 0
    for i in range(1000):
        sum = sum + i
        print(sum)

    stop = time.time()
    stopWatch.stop(datetime.datetime.fromtimestamp(stop, tz=None))
    print("Stopwatch stopped at", stopWatch.getEndTime())

    print("The loop runtime is", stopWatch.getElapsedTime(), "milliseconds")   

if __name__ == "__main__":
    main()