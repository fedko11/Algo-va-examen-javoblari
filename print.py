# from math import *
# a,b = map(float,input().split())



# t = (pow(sqrt , 5 ) * a) + (pow(sqrt , 4)* b * (a+b) / 2 *b + a*b ) * ((a**2) + (b**2) + (2))
# print("%.2f" %t)


# from math import *
# x,y = map(float,input().split())
# modul = log(abs((x+y)**2) + sqrt(abs(y)+2) -  (x - (x*y) /  ((x**2) / (2) - 5))) + ((cos(x+y)**2) / ((x+y) ** (1/3)))
# print("%.2f"%(modul))



# from math import *
# x1,x2,c,d = map(float,input().split())

# F = abs((sin(abs(c*(x2**3) + d*(x1**3) - (c*d)))**2) / (sqrt((c*(x1**2)) + (d*(x2**2)) + (7))))   +   tan( (x1 * (x2**2)) + (d**3))
# print("%.2f" % F)


# from math import *
# a,b,c,d,x = map(float,input().split())
# y2 = (a*(x**2)) + (b*x) + c / (x*a**3) + (a**2) + (a**b-c)   +    cos((a*x)+(b) / (c*x) + (d) + (2**c))
# print("%.2f" % y2)




# from math import *
# a,x,y = map(float,input().split())
# # W2 = sqrt(e*x**y -  x * sin(a*x) - (x**2+2) / (abs(x) +5)) +  sqrt(log((x**2+2)+5))

# W2 = sqrt(e**x*y)

# # W2 = sqrt(((e**x*y) - (x * sin(a*x))) - ((x**2) + 2) / (abs(x) + 5)) + sqrt(log((x**2+2)+5))
# print("%.2f" %W2)

# from math import *
# n = int(input())
# v = (n**2)-2
# print(v)

# a = int(input())
# if a>10:
#     print(a+3)
# if a<10:
#     print(a * 2)
# if a == 10: 
#    print(22)

# x, y, z = input().split()



# x = float(x)
# y = float(y)
# z = float(z)
# d = min(x, y, z)
# if x < 1 and y < 1 and z < 1:
#     if d == y:
#         print(x, (x + z) / 2, z)
#     elif d == z:
#         print(x, y, (x + y) / 2)
#     else:
#         print((y+z) / 2, y, z)
# else:
#     print(x,y,z)


#!103
# n = int(input())
# ar = list(map(int, input().split()))[:n]
# k, l = map(int, input().split())
# ff = []
# for  i in range(len(ar)):
#     if k <= i + 1 <= l:
#         ff.append(ar[i])
# f = sum(ff) / len(ff)
# print("%.1f" % f)

#!101
# n = int(input())

# arr = list(map(int, input().split()))[:n]
# s = sum(arr)
# uzun = len(arr)
# # print(s)
# # print(uzun)
# ortacha = s / uzun
# a = []
# for i in arr:
#     if ortacha > i:
#         a.append(i)
        
# d = sum(a) / len(a)
# print("%.2f"% d)


# mas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# n = int(input())
# s = 0
# for i in range(n - 2,n +3 ):
#     s+=mas[i-1]
# print(s)


#!  dmoi    2hoirfhw39ughqoi4uhgpuq4hu5o;h34w   algo bratim
 
 






# from math import *
# x,y,c,d = map(int,input().split())
# s = 0
# for a in range(1,x+1):
#     s += (a*x + 4) / (sqrt(a+log(6)))
    
# p = 1
# for a1 in range(1,y+1):
#     p *= (a1*x**2 + 6) / (sin(a1*x))
# sp = 1
# for i in range(1,c+1):
#     f = 1
#     for j in range(1,d+1):
#         f *=    (i *j + y*x) / (sqrt(j*x + y) ** i)
#     sp *= f
# print("%.2f %.2f %.2f"%(s,p,sp) )

#! 22022000002020020202002020020202020202002020200202020000202000202
# n = int(input())
# list = list(map(int,input().split()))[:n]
# a,b = map(int,input().split())
# s = min(list)
# mas = []
# for i in range(n):
#     if a-1<= i <= b-1:
#         mas.append(list[i]/s)
#     else: 
#         mas.append(list[i])
# for dr in mas: 
#     dr+=0.01      
#     print("%.1f" % dr)



#!2y3r7501685618374r613874ry13874tyr83174yr87314yt7834tr7831t4r7314tr7834tr8734rt3847r3471rt


