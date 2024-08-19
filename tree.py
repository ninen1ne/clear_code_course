n = int(input('Enter some number: '))
a_start = 1
space_start = n + 2
for i in range(n):
    a = a_start
    space = space_start
    for j in range(4):
        for k in range(0, space):
            print(" " , end="")
        for k2 in range(0, a):
            print('*' , end="")
        print()
        space -=1;
        a += 2
    a_start += 2
    space_start -= 1;


for k3 in range(3):
    for k4 in range(n + 1):
        print(" " , end="")
    for k5 in range(3):
        print('*', end="")
    print()