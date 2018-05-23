import unittest
import time
import sys
import os

def isIntegerRepresentation(x):
    """
    Verifies that every character in string `x` is a numeral.
    """
    for i in x:
        if not i in '0123456789':
            return False

    return True


# Thanks to Sridhar Ratnakumar from StackOverflow for this function
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

KB = 1024
MB = 1024*KB
GB = 1024*MB
TB = 1024*GB

def ProgressBar(message):
    def decor(f):
        def new_func(self, *k):
            print(message.format(*k))
            self.markedProgress = 0
            self.startTime = time.time()

            print("Progress")
            print("_" * 100)

            f(*k)

            print("")
            print("{0} lines ({1}) read.".format(counter, sizeof_fmt(memRead)))
            print("{0}% clean".format(100 * cleanCount / counter))

        return new_func
    return decor

def stepProgress(self):
    sys.stdout.write('#')
    sys.stdout.flush()
    self.markedProgress += .01

class Papers(unittest.TestCase):

    memLimit = 1 * GB

    @ProgressBar("Testing {0}s are in numeric form...")
    def columnIsNumeric(self, displayName, index):

        filepath = 'data/Papers.txt'
        papers = open(filepath)

        if self.memLimit == None:
            memLimit = os.stat(filepath).st_size
        else:
            memLimit = self.memLimit

        cleanCount = 0
        counter = 0

        memRead = 0

        row = papers.readline()

        while row:
            memRead += len(row) + 1
            attributes = row.split('\t')

            if isIntegerRepresentation(attributes[index]):
                cleanCount += 1

            #if counter == 1000:
            #    print ("ETA: {0} minutes".format(total * (time.time() - startTime) / 1000.))

            counter += 1
            if memRead / memLimit - markedProgress > .01:
                stepProgress()

            if memRead >= memLimit:
                break

            row = papers.readline()

        papers.close()


    def testIntegerValues(self):
        try:
            os.stat('data/Papers.txt')
        except:
            print("\n\nHINT: Make sure you're working directory is the project root and that data/Papers.txt is a file you have access to.\n\n")
        self.columnIsNumeric('ID', 0)
        self.columnIsNumeric('Publication Year', 7)
        self.columnIsNumeric('Journal ID', 10)
        self.columnIsNumeric('Citation Count', 18)

if __name__ == '__main__':
    unittest.main()
