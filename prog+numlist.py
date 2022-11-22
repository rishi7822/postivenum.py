list1 = [23,55,66,-1,-133,55]

pos_no = [num for num in list1 if num >= 0]

print("positive number:", *pos_no)

#in range now

start = int(input("enter the number:"))
end = int(input("enter the number:"))

for i in range(start ,end+1):

    #condition
    if i >= 0:
        print(i , end= " ")