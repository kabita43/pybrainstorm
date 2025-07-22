'''
1 for snake
-1 for water
0 for gun
'''
computer= -1
youstr= input("enter your choice :")
youDic= {"s":1,"w":-1,"g":0}
you= youDic[youstr]

if(computer==-1 and you ==1):
    print("you win!")
elif(computer==1 and you == -1):
    print("computer win!")
elif(computer==-1 and you ==0):
    print("computer win!")
elif(computer==0 and you ==0):
    print("computer win!")
elif(computer==-1 and you ==0):
    print("computer win!")
elif(computer==-1 and you ==0):
    print("computer win!")


