#Funcitons,build in funcitons,lamda functions
# a = 'Paratha'

# for i in range(100):
#     print(a)


# b = "samosa"

# for i in range(100):
#     print(b)

# #function

# l =[2,3,4,2,2,3,4,34,5,1]

# print(sum(l))

#user defined function

# def add(a,b):
#     c = a+b
#     return c

# #calling the fucntin in the print fucntion
# print(add(5,20))


# k.e = 0.5 * m * v**2

# def KE(m,v):
#     x = 0.5 * m * v**2
#     return x

# value = KE(2,3)
# print(value)


# def f(x):
#     return x**2 + 3*x + 4

# value = f(2)
# print(value)



#10%

# def das_takka(x):
#     return x*1.1

# value = das_takka(150)
# print(value)


def खाओ(name,veg = True):

    global a
    a = "Emma watson"
    b = "Ketaki Mategaonkar"

    if veg :
        return f'{name} app paneer biriyani खाओ'
    else:
        return f'{name} app mutton biriyani खाओ'

value = खाओ("Pooja",veg = "")

print(a)



# add_1 = lambda x : x + 1

# v = add_1(6)
# print(v)



# #-----------
l = [1,2,3,2,3,4,5,6,5,6,7,8,9,9,88,13,300000]

s = list(map(lambda x : x**2,l))
print(s)



# def das_takka(x):
#     return x*1.1


# def add(a,b):
#     c = a+b
#     return c

# value = add(100,das_takka(500))

# print(value)
