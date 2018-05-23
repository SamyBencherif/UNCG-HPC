import hashlib
import time

#Next TODO! find things in directory that are missing from this list and checksum them!
hashProtected = """ #WHITELIST BEGINS AFTER THIS LINE
PaperRecommendations.txt
PaperReferences.txt
PaperUrls.txt
Papers.txt
""".split('\n')[1:-1] #WHITELIST END

output = open('integrity.md5.txt', 'a+t')


for file in hashProtected:

	print("Hashing {0}".format(file))

	currHash = hashlib.md5()
	handle = open('../data/' + file)

	line = handle.readline()
	c = 0
	while line:

		currHash.update(bytes(line, 'utf-8'))
		line = handle.readline()
		time.sleep(1/20000000) #no hot cpu
		c += len(line)+1
		if c % 1017310 == 0:
			print("{0}MB processed...".format(c/1024**2))

	hashinfo = '-- ' + file + ' --\nhash: ' + currHash.hexdigest() + '\n\n'
	output.write(hashinfo)

	print("File {0} is finished!".format(file))

output.close()