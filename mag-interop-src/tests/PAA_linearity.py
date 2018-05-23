import unittest
import time

"""
A naked-eye look at the file PaperAuthorAffiliations.txt reveals that there are often consecutive rows with the same paper id.
See the example below.

-----------------------------------------
2789232023      2792569368              7
2789232023      2793695134              2
2789232023      2791475204              4
2789232023      2791087716              3
2789232023      2790187053              6
2789232023      2789427676              1
2789232023      2791135981              5
2789232023      2789328014              8
-----------------------------------------

It is possible that the file is organized with no disjoint groups of rows with the same paper id.
In other words:

CND1: If row[i].paperid != row[i+1].paperid then row[i].paperid does not occur after row[i+1].

With this assumption the algorithm can reduced from O(n^2) to O(n) time complexity. If the assumption is false then the graph
created by the linear algorithm would be incomplete. Given the large size of the data an O(n^2) algorithm may be very slow. It
might be a good idea to first try the linear algorithm, and missing connections can be filled in later if necessary.

This program is a probabilistic test of CND1. If it tests negative you are guranteed a non-linearity, every time it tests
positive the effective probability that the data set is linear goes up marginally. The probability table is pictured below.

+------------+--------------+----------+
|            |    tests     |  tests   |
|            |   positive   | negative |
+------------+--------------+----------+
|  actually  |  P(A)^(n-1)  |    0%    |
|   linear   |              |          |
+------------+--------------+----------+
|  actually  | 1-P(A)^(n-1) |   100%   |
| non-linear |              |          |
+------------+--------------+----------+

Note that n is a very large number in this case.
"""

import random

class PAA_Linearity(unittest.TestCase):

	def test(self):

		PAA = open("data/PaperAuthorAffiliations.txt")

		c = 0
		b = 0

		# randomly seek forward
		for i in range(random.randint(0,1000)):
			line = PAA.readline()
			c += 1
			b += len(line) + 1

		originLn = c
		# get paper id of interest
		attributes = line.split('\t')
		paperId = attributes[0]
		if ' ' in paperId:
			raise Exception("Paper id contains whitespace! This may interfere with comparisons.")

		prev_seekId = paperId

		line = PAA.readline()
		c += 1
		b += len(line) + 1

		# linearity test
		while line:
			attributes = line.split('\t')
			seekId = attributes[0]

			if seekId == paperId and prev_seekId != paperId:
				print("Paper id: {0} is non-linear. Found id from block {1} at line #{2}".format(paperId, originLn, c))
				self.assertTrue(False) # found non-linearity

			prev_seekId = seekId

			line = PAA.readline()
			c += 1
			b += len(line) + 1

			if b % 2100480 == 0: # give output about every 2,000,000 lines
				print("{0}GB scanned.".format(int(100 * b/1024**3)/100))

			# This line will slow the process down but keep the cpu nice and cool.
			# The magic number 2B keeps usage on my Macbook Pro 15in down to 60ish% cpu
			time.sleep(1/2000000000)

if __name__ == '__main__':
    unittest.main()