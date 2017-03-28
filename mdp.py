import copy
x = 18
delta = 1.0*x/20
array = [['W','W','W','W','W','W'],
        ['W','W','W',x,'W','W'],
        ['W',0, 0, 0, 0,'W'],
        ['W',0, -x, 'W', 0,'W'],
        ['W',0, 0, 0, 0,'W'],
        ['W','W','W','W','W','W']]
# for i in range(1,5):
#     print array[i]
def display(board):
	for i in range(1,5):
		#print
		for j in range(1,5):
			print "",
			if type(board[i][j]) is float:
				print ("%.4f" %board[i][j]),
			else:
				print board[i][j],
		print
	print

print "Initial State : "
display(array)

for k in range(0,1000):
    temp = copy.deepcopy(array)
    flag = True
    for i in range(1,5):
        for j in range(1,5):
            if temp[i][j]==x or temp[i][j]==-x or temp[i][j]=='W':
                continue
            # print type(temp[i][j+1])
            e = temp[i][j+1]
            w = temp[i][j-1]
            n = temp[i+1][j]
            s = temp[i-1][j]
            if temp[i][j+1]=='W':
                e = temp[i][j]
            if temp[i][j-1]=='W':
                w = temp[i][j]
            if temp[i+1][j]=='W':
                n = temp[i][j]
            if temp[i-1][j]=='W':
                s = temp[i][j]
            E = 0.8*e + 0.1*n + 0.1*s
            W = 0.8*w + 0.1*n + 0.1*s
            N = 0.8*n + 0.1*e + 0.1*w
            S = 0.8*s + 0.1*e + 0.1*w
            # print i,j
            # print E,W,N,S
            array[i][j] = -0.05*x + max(E,W,N,S)
            if abs(array[i][j]-temp[i][j])>delta :
                flag = False
    print "After " + str(k+1) + " Iterations"
    display(array)
    # for i in range(1,5):
    #     print array[i]
    if flag:
        #print k
        break
print "After Convergence :"
display(array)
