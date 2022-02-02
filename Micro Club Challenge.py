from ast import Div, While


print('Enter your number:' )
x = input()
j=x
i=1
while j!=0:
  j=int(j)//10
  i=i*10

if (int(x)**2)%i == int(x):
    print('number is valid')
else:
    print('number is not valid')




