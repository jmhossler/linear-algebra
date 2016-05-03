from sympy import *

# task 1

def task1():
    print("\n\n----------TASK 1-------------\n\n")
    t1 = Matrix([[1,2,3],[1,3,5],[-2,-4,-5]])
    t1Inv = t1 ** -1
    print("Original:\n",t1,"\n")
    print("Inverse:\n",t1Inv,"\n")
    print("matrix * inverse:\n",t1 * t1Inv,"\n")

# task 2

mat = Matrix([[1,4,7,10],[2,5,8,11],[3,6,9,12]])

def linTrans(v):
    return (mat * v.T).T
    #return (mat.rref()[0] * v.T).T

def task2():
    print("\n\n----------TASK 2-------------\n\n")
    a = Matrix([[1,-2,1,0]])
    b = Matrix([[2,-3,0,1]])
    for i in range(0,10):
        print(linTrans(a * i))
        print(linTrans(b * i))

    print("Basis for the ker of T: [[1,-2,1,0]],[[2,-3,0,1]]")

def task3():
    print("\n\n-----------TASK 3------------\n\n")
    #print(mat.T)
    #print((mat.T).rref()[0])
    for i in range(0,5):
        #print("I = ",i)
        for j in range(0,5):
            #print("J = ",j)
            for k in range(0,5):
                #print("K = ",k)
                for m in range(0,5):
                    x = linTrans(Matrix([[i,j,k,m]]))
                    #if(x[0,2] != 0):
                        #print(i,",",j,",",k,",",m)
                    #print("M = ",m)
                    #print(linTrans(Matrix([[i,j,k,m]])))
    print("Basis for im of T: [[1,2,3],[4,5,6]]")

def task4():
    print("\n\n------------TASK 4-------------\n\n")
    m = Matrix([[1,4,7,10,3],[3,5,8,11,3],[3,6,9,12,3]])
    print(m.rref()[0])
    print("The set of vectors, {v1,...,vn} in R^4 that satisfy T(vi) = [3,3,3] for i = 1,...,n is {[0,0,-1,1],[0,-1,1,0]}.")
    a = Matrix([[0,0,-1,1]])
    b = Matrix([[0,-1,1,0]])
    print(linTrans(a))
    print(linTrans(b))


def task5():
    print("\n\n------------TASK 5-------------\n\n")
    a = Matrix([[1,2,3]])
    b = Matrix([[4,5,6]])
    print(a.cross(b))
    print("The equation for the plane that represents the im(T) is -x+2*y-z = 0")

# running functions
task1()
task2()
task3()
task4()
task5()
