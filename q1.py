#Create generator with and without comprehension for getting multiples of given number upto 10.
#Eg. generator(5) =>> 5, 10, 15 …. 50


#without comprehension
n=int(input("Enter a number: "))
for i in range(1,11):
    x=n*i
    print(x)

#With comprehension
num=int(input("Enter a number:"))
length=10
multiple=range(num,num*length+1,num)
print(*multiple)

