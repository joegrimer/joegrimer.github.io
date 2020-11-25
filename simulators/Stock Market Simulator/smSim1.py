# stock market simulator JosephGrimer 20/jul/2016
# This reached a dead end, because I didn't understand the stock market enough!

print("Welcome to Stock Market Sim")

# Classes

class firm:
	def __init__(self,name="CompanyX",shares=0,costPerShare=0): #(name,shareCount,costPerShare)
		self.name=name
		self.shares=shares # (800+oneIn(1000))
		if(shares==0):
			self.shares=(800+oneIn(1000))
		self.costPerShare=costPerShare
		if(costPerShare==0):
			self.costPerShare=(10+oneIn(10))
#		self.size=(800+oneIn(100))
		self.stability=oneIn(7)-4
	def stats(self):
		stats = "\n Company Name: "
		stats += self.name
		stats += "\nShares: " + str(self.shares)
		stats += "\nCost Per Share:" + u"\xA3"
		stats += str(self.costPerShare)
		stats += "\nTotal Value: " + u"\xA3"
		stats += str(self.shares*self.costPerShare)
		return stats
	def iterate(self):
		print("Iterating:"+self.name)
		self.costPerShare +=self.stability


#################### Main Function ###################################

def main():

	#initiate firms
	alpha=firm("Alpha",10,10)
	beta=firm("Beta",5,5)
	gamma=firm("Gamma")

  #print firms
	print(alpha.stats())
	print(beta.stats())
	print(gamma.stats())
  
	#iterate firms
	print("\n")
	alpha.iterate()
	beta.iterate()
	gamma.iterate()
  
  #print firms
	print(alpha.stats())
	print(beta.stats())
	print(gamma.stats())

##################### Tail ###########################################

### simple seeding:

def aSeed():
	global seeds
	global lastSeed
	lastSeed += 1
	if lastSeed >= len(seeds):
#		print("clocking")
		lastSeed = 0
	seeds[lastSeed]+=59
	return seeds[lastSeed]

def oneIn(max):
	return ((aSeed()+aSeed()+aSeed()+aSeed())%max) # 400-800?

seeds = [] # string based randomiser setup
lastSeed = -1
seedStr = "4eg567er5zzzp4j89ed7g6nl.ef7e58oy8ilfhogbu;/gp09d/[-9hje5sgh'4689=8se"

# Prepare Randomiser
for char in seedStr:
	seeds.append(ord(char))

#run main... always put me at the bottom!
main()



