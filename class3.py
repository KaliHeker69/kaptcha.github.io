# Question 1

# ecount = 0
# ocount = 0
# for x in range(5,100):
#     if x%2 == 0:
#         ecount += 1

#     else:
#         ocount += 1

# print(ecount," ")
# print(ocount)



#Question 2

# x = input("Enter a sentence ")
# size =len(x) - 1
# s = ""
# for i in range(size,-1,-1):
#     s = s+x[i]

# print(s)



#Question 3

# n = int(input("Enter the end limit "))
# if n == 0 or n == 1:
#     print("Neither prime nor composite")

# else:
#     for i in range(2,n+1):
#         p = 0
#         for j in range(2,i):
#             if i%j == 0:
#                 p+=1
#         if p==0:
#             print(f'{i} is a prime number')    
#         else:
#             print(f'{i} is not a prime number')




#Question 4


# term = int(input("Enter nth term "))
# n1, n2 = 0, 1

# print("Fibonacci Series:", n1, n2, end=" ")
# while(term > 0):
#     term = term - 2
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")



#Question 5

passw = str("P@$sw0rd")
upassw = str(input("Enter your password "))

chance = 0
while(passw != upassw & chance < 5):
    chance += 1
    print("Correct password")

else:
        print("Wrong Password")    









