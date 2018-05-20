
good = open('good.txt')

line = good.readline()

while line:
    print(line[:-1])
    line = good.readline()
