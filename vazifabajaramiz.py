# from math import*
# a,b,c,d = map(int,input().split())
# m=1
# s = 0
# while m <= a:
#     s += (3 * (m**3) + 4*m +5) / (m**3 + log(m))
#     m+=1
# p=1
# k=1
# for i in range(1,b+1):
#    p *= (k) / ((k**3)+ 7*k+5)
# sp=0 
# for i in range(1,c+1):
#     p1 = 1
#     for m in range(1,d+1 ):
#         p1 *= (log(i) + m**i) / (m**i) 
#     sp += p1     
    
# print("%.2f %.2f %.2f" %(s,p,sp))   



# from math import*
# x,y,a,b = map(int,input().split())
# a = 1
# s = 0
# while a<=x:
#     s+= (a**2 + 2*a) / (a**3 + a*cos(a)**2 + 1)
#     a+=1
# p=1
# i = 1
# while i <=y:
#     p *= (i**2+1) / (i**(3/i) + 2)
#     i += 1
# sp = 0
# i = 1
# k = 1
# while i <=a:
#     i += 1
#     while k<=b:
#         p1 = 1
#         k += 1
#         p1 *= log((k**i + pow(k,(1/i)) ) / (k**3 + pow(i,(1/k))))
  
#     sp *= p1
# print("%.2f %.2f %.2f" %(s,p,sp)) 



# a = input()
# a1 = 0
# y1 = 0

# for i in a:
#     if i.upper() == 'A':
#         a1+=1
#     if i.upper() == 'Y':
#         y1 +=1
# print(a1)
# print(y1)


# a = input().split()
# i = 0
# for i in a:
#     if i.startswith('A') :
#         print(i)



# a = input().split()
# for i in a:
#     if i.startswith("Info") or i.endswith("Info"):
#         print(i,end=" ")











# x = a.replace("salom", "xayr")
# print(x)






# s = 0
# for harf in a:
#     if harf.lower() == 'a':
#         s+=1
# print(s)




# a = input().split()
# b = 0
# for a in b:
#     if a.startswith('A'):
#         print(a)
   
       
# a = input()
# nums = 0
# for i in a:
#     if i.isdigit():
#         nums +=int(i)
# print(nums)

# a = input().split()
# for i in a:
#     print(i,len(i))


# a = input().split()
# nums = 0 
# for i in a:
#     for ia in i:
#         d = ia
#         if ia  == d.upper():
#             nums+=1
#         break
# print(nums)

# a = input( ) [::-1]
# print(a)


# a = input()
# s = 0   
# for i in a:
#     if i == "a" or i == "A" or i == "i" or i == "I" or i == "u" or i == "U" or i == "e" or i == "E" or i == "o" or i == "O":
#         s =+ 1
# print(s)                           #xatoooooooooooo

#?1
# a = input().swapcase()
# print(a)

#2
# a = input()
# print(len(a))

#?3
# a = input()
# c=0
# for i in a:
#     c =+ 1
# print(a)

# a = input().split()

# for i in a:
#     if  i.istitle() and i.endswith("ton"):
#         print(i)


#?13
# a = input("Do'konimizga xush kelibsiz!").split()
# s = 0
# while True:
#     for i in a:
#         if i.startswith("+998") and len(a) == 13:
#             print("Mahsulotlarimizdan foydalanish mumkun")
#         elif i.startswith("+7") and i.startswith("+1"):
#             print("Siz boshqa davlatdansiz")
#     else:
#         i.startswith("+1")
#         print("Raqam kiritishda xatolik")
#     break                                                     #xatoooooooo
    
    
# print("Ro\'yhatdan o'ting")
# while True:
#     a = input('Telefon raqamingizni kiriting: ')
#     if a.startswith("+998") and len(str(a)) == 13:
#         print("Mahsulotlarimizdan foydalanishingiz mumkin")
#         break
#     elif a.startswith("+7"):
#         print("Biz ruslarga xizmat ko'rsatmaymiz")
#     elif a.startswith("+1"):
#         print("Biz USA ga xizmat ko'rsatmaymiz")
#     elif a.startswith("+998") and (len(str(a)) == 13) == False:
#         print("Raqamni to'liq kiriting")
#     else:
#         print("Biz sizga xizmat ko'rsatmaymiz")
        