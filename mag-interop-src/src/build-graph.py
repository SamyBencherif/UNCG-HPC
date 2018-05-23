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

        if self.EOF:
            return

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

        if self.EOF:
            return

        self.attributes = row.split('\t')

        self.paperID = self.attributes[0]
        self.authorID = self.attributes[1]
        self.affiliationID = self.attributes[2]

class NetworkBuilder:

    def resetFileHandles(self, Papers=1, PAA=1):
        if Papers:
            self.Papers = open(join(dirname(sys.argv[0]), 'data/Papers.txt'))
        if PAA:
            self.PAA = open(join(dirname(sys.argv[0]), 'data/PaperAuthorAffiliations.txt'))

    def __init__(self):
        self.resetFileHandles()

    def applyNextPaper(self):
        self.currPaper = PaperAuthorAffiliations(self.PAA.readline())

        # Assume linearity, create graph in linear time.
        # see POA if needed, but write a no distribution algorithm first
        # create some polling options
            # 1. Detailed file / network statistics in realtime-stats.txt
                # Make sure to be indicative of what happened so far, and how much more needs to be done (eta)
            # 2. Maintain a visual representation of the graph in realtime