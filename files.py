X, Y, Z = 45,32,44
S = 'Spam'
D = {'a' : 1, 'b' : 2}
L = [1, 2, 3]

F = open('data.txt','w')
F.write(S + '\n')
F.write('{},{},{}\n'.format(X,Y,Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

F = open('data.txt')
string = F.readline().rstrip()
numbers = F.readline().split(',')
numbers_int = [int(n) for n in numbers]

F.close()