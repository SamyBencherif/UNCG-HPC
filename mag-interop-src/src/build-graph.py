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
        self.prevRow = PaperAuthorAffiliations(self.PAA.readline())
        self.paper = [self.prevRow]
        self.network = networkx.Graph()

    # Assuming PAA linearity, creates graph in O(n) time.
    # See tests/PAA_linearity.py
    def applyNextRow(self):
        self.curRow = PaperAuthorAffiliations(self.PAA.readline())

        if self.curRow == self.prevRow:
            self.paper.append(self.curRow)
        else:
            # here self.paper presumably contains all the rows related to a paper
            for row1 in self.paper:
                for row2 in self.paper:

                    affiliation1 = row1.affiliationID
                    affiliation2 = row2.affiliationID

                    self.network.add_node(affiliation1)
                    self.network.add_node(affiliation2)

                    self.network.add_edge(affiliation1, affiliation2)

            # self.curRow is pointing at the start of the next paper
            self.paper = [self.curRow]



        # then create some polling options
            # 1. Detailed file / network statistics in realtime-stats.txt
                # Make sure to be indicative of what happened so far, and how much more needs to be done (eta)
            # 2. Maintain a visual representation of the graph in realtime