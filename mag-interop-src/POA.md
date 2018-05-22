
-- Draft --

# Algorithm Design Plan Of Attack

This document serves to evaluate the network specification in the context of building the network. Here is where the technical limitations of the hardware and the computability of the algorithm will be considered.

## Task
Create weighted graph that meets specification outlined here <https://www.sharelatex.com/read/cszpyqnxryqm>.
In the implementation all weights should be real numbers, the graph itself should have minimal memory impact, and the computation should have minimal time complexity.


## P1

Lets say we've transformed `PapersAuthorsAffiliations.txt` into `PapersAffiliations.txt` and we have rows of this form.

| Paper | Affiliation |
| :---: | :---------: |
|   X   |      A      |
|   X   |      B      |
|   X   |      C      |

The following edges should be added to the graph.

```
(A, B)
(A, C)
(B, C)
```

If the edge did not exist already the weight should be initialized to 1.

If the edge already exists the weight should be incremented by 1.

## P2

Now considering distribution. In hopes of keeping the resulting graph size under 100GB I will only distribute
over two time periods. Pre-21st-Century and 21st-Century.

 Given rows of the form:

| Paper |    FOS    | Published | Affiliation |
| :---: | :-------: | :-------: | :---------: |
|   X   |    tv     |   1970    |      A      |
|   X   |    tv     |   1970    |      B      |
|   X   |    tv     |   1970    |      C      |
|   Y   | interests |   1970    |      D      |
|   Y   | interests |   1970    |      E      |
|   Y   | interests |   1970    |      F      |
|   Z   | interests |   2010    |      G      |
|   Z   | interests |   2010    |      H      |
|   Z   | interests |   2010    |      I      |

Will result in a cataloged group of networks like this:


```
Period: 21st, fos: interests
(G,H,1)
(G,I,1)
(H,I,1)

Period: 20th, fos: interests
(D,E,1)
(D,F,1)
(E,F,1)

Period: 20th, fos: tv
(A,B,1)
(A,C,1)
(B,C,1)
```