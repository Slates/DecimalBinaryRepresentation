import sys

num = 0.5
target = 0.45
curnumber = 0
binary = ""

for a in range(0,17):
	if ((num + curnumber) > target):
		binary = binary + "0"
	else:
		curnumber = curnumber + num
		binary = binary + "1"
	num = num/2


print(target)

print(curnumber)
print(binary)