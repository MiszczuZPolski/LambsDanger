import sys
import os

defaultFalsePositives = 29
def main():
    f = open("sqf.log", "r")
    log = f.readlines()
    if (len(log) == defaultFalsePositives):
        print("{} number of false Positives found".format( len(log) ))
        return 0
    print("Warning {} than the Default number of false Positives found".format( len(log) - defaultFalsePositives ))
    return 1

if __name__ == "__main__":
    sys.exit(main())
