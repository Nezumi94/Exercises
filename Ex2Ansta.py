n = 1
nmax = 10
values = [1,2,3,4,5,6,7,8,9,10]

In = [2,3,7,4,9],10
Out = [1,5,6,8,10]

In0 = list(In)

In0.remove(10)

A = In0[0]

print(list(set(values) - set(A)))

print(list(set(values) - set(Out)))