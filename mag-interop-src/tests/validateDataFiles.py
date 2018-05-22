import unittest
import time
import sys
import os

def integerRepresentation(x):
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

class Papers(unittest.TestCase):

    memLimit = 1 * GB

    def trackedIntegerValidation(self, displayName, index):

        print("Testing {0}s are in numeric form...".format(displayName))

        filepath = 'data/Papers.txt'
        papers = open(filepath)

        if self.memLimit == None:
            memLimit = os.stat(filepath).st_size
        else:
            memLimit = self.memLimit

        cleanCount = 0
        counter = 0

        markedProgress = 0
        memRead = 0

        startTime = time.time()

        print("Progress")
        print("_" * 100)

        row = papers.readline()

        while row:
            memRead += len(row) + 1
            attributes = row.split('\t')

            if integerRepresentation(attributes[index]):
                cleanCount += 1

            #if counter == 1000:
            #    print ("ETA: {0} minutes".format(total * (time.time() - startTime) / 1000.))

            counter += 1
            if memRead / memLimit - markedProgress > .01:
                sys.stdout.write('#')
                sys.stdout.flush()
                markedProgress += .01

            if memRead >= memLimit:
                break

            row = papers.readline()

        papers.close()
        print("")
        print("{0} lines ({1}) read.".format(counter, sizeof_fmt(memRead)))
        print("{0}% clean".format(100 * cleanCount / counter))

    def test(self):
        try:
            os.stat('data/Papers.txt')
        except:
            print("\n\nHINT: Make sure you're working directory is the project root and that data/Papers.txt is a file you have access to.\n\n")
        self.trackedIntegerValidation('ID', 0)
        self.trackedIntegerValidation('Publication Year', 7)
        self.trackedIntegerValidation('Journal ID', 10)
        self.trackedIntegerValidation('Citation Count', 18)

if __name__ == '__main__':
    unittest.main()
