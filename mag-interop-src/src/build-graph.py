#
# MAG Interoperability Network Builder
#
# (c) Samy Bencherif
# University of North Carolina Greensboro
#

import networkx

from os.path import join, dirname
import sys

def HandlesMalformedRows(filename):
    def decor(f):
        def new_func(self, row, i):
            try:
                f(self, row, i)
            except:
                raise Exception("Did not recieve a well formed row at line #{0} in file {1}!".format(i, filename))
        return new_func
    return decor

#
# Wrapper classes for database rows
#

class Paper:

    @HandlesMalformedRows("Papers.txt")
    def __init__(self, row, i):
        self.EOF = (row == "")
        self.attributes = row.split('\t')

        self.id = self.attributes[0]
        self.title = self.attributes[4]
        self.journalID = self.attributes[10]
        self.year = self.attributes[7]
        self.citationCount = self.attributes[18]

class PaperAuthorAffiliations:

    @HandlesMalformedRows("PaperAuthorAffiliations.txt")
    def __init__(self, row, i):
        self.EOF = (row == "")
        self.attributes = row.split('\t')

        self.paperID = self.attributes[0]
        self.authorID = self.attributes[1]
        self.affiliationID = self.attributes[2]

class NetworkBuilder:

    def resetFileHandles(self, Papers=1, PaperAuthorAffiliations=1):
        if Papers:
            self.Papers = open(join(dirname(sys.argv[0]), 'data/Papers.txt'))
        if PaperAuthorAffiliations:
            self.PaperAuthorAffiliations = open(join(dirname(sys.argv[0]), 'data/PaperAuthorAffiliations.txt'))

    def __init__(self):
        self.resetFileHandles()

    def applyNextPaper(self):
        self.currPaper = Paper(self.Papers.readline())

        # Next I need to search for self.currPaper.id in PaperAuthorAffiliations