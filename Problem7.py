#7.COUNT EVEN AND ODD NUMBERS IN A LIST
L1=[1,2,3,5,9,10,14,16,17]
EVEN=0
ODD=0
for numbers in L1:
	if(numbers%2==1):
		ODD=ODD+1
	if(numbers%2==0):
		EVEN=EVEN+1
print("the total even numbers in a list is:",EVEN)
print("the total ODD numbers in a list is:",ODD)
	
	