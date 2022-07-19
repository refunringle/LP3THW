n=int(input('ENTER THE NUMBER:'))

for i in range(1,n+1):
	for j in range(1,i):
		if j%2==0:
	   		print('+',end=' ')
	    else:
			print('*',end=' ')

	print("")
for k in range(n,0,-1):
	for l in range(1,k+1):
		if l%2==0:
	   		print('+',end=' ')
		else:
			print('*',end=' ')
	print("")
for a in range(1,n+1):
	for b in range(1,a+1):
		if b%2==0:
	   		print('+',end=' ')
		else:
			print('*',end=' ')
	print("")
for e in range(n,n+n):
	for f in range(n,n+2):
		if f%2==0:
	   		print('+',end=' ')
		else:
			print('*',end=' ')
	print(" ")	
