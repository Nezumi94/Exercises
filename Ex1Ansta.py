PostCodeA = '79-900'
PostCodeB = '80-155'

PostListA = PostCodeA.split('-')
PostListB = PostCodeB.split('-')

A = PostListA[0]
B = PostListB[0]
C = PostListA[1]
D = PostListB[1]
print('A=',A,'B=',B,'C=',C,'D=',D)

for number in range(79,81) :
    for code in range(155,901) :
        print(number,'-',code)
