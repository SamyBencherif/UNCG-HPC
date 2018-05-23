import time
import sys

def ProgressBar(message):
    def decor(f):
        def new_func(self, *k):
            print(message.format(*k))
            self.markedProgress = 0
            self.startTime = time.time()

            print("Progress")
            print("_" * 100)

            f(self, *k)

            print("Finished in {0} seconds\n".format(int((time.time() - self.startTime)*100) / 100 ))

        return new_func
    return decor

def stepProgress(self):
    sys.stdout.write('#')
    sys.stdout.flush()
    self.markedProgress += .01

class Mower:
	@ProgressBar("Mowing the lawn. This is the {0} time!")
	def mow(self, occurence, surface):
		for i in range(100):
			stepProgress(self)
			time.sleep(.1)
		print("")
		print("This lawn was made of {0}! Spectacular! Splendid!".format(surface))

mower = Mower()

mower.mow('first', 'grass')
mower.mow('second', 'gravel')
mower.mow('third', 'clouds')