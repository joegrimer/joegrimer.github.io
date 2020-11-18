# the purpose of this program is to test the speed of:
# division vs multiplication,
# in order to make my program more efficient!


def div():
	for i in range(1,20000000):
		c = 10000000/333333
# 1.592 secs
		
def mul():
	for i in range(1,20000000):
		c = 30*333333
# 0.957 secs

mul()
