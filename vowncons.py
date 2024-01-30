def countvowsncons(a):
    count1=0
    count2=0
    for i in a:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" ):
            count1+=1
        else:
            count2+=1
    print(f"no of vowels are {count1} \n no of consonants {count2} ")


a=input("Enter any word").lower()
countvowsncons(a)