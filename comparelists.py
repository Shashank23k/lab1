def compare(list1,list2):
    count = 0
    for i in list1:
        if i in list2:
            count+=1
    print(f"no of similar elements is {count}")

list1=[1,2,-1,5,-10,15,33]
list2=[-10,20,30,15,1,44,34,2]
compare(list1,list2)
