#!/usr/bin/env python3
#求和 1...100
n = 100
sum = 0
counter = 1
while counter<=n :
	sum = sum + counter
	counter += 1
print("Sum of 1 until %d: %d" % (n,sum))
