#Write a function 'remove_duplicates' that takes
#in a list and returns a list without duplicatesself
#For examples:
#remove_duplicates([1,1,2,2])' should return '[1,2]'.

a_list1 = [1,2,3,4,5,1,2,3]

def remove_duplicates(a_list1):
    new_list1 = []
    for i in a_list1:
        if i not in new_list1:
            new_list1.append(i)
    return new_list1
print(remove_duplicates(a_list1))

a_list = [0,1,2,3,4,5,6,7,8,9,10]

def return_square(a_list):
    new_list = []
    for i in a_list:
        new_list.append(i * i)
    return new_list

print(return_square(a_list))

def division_reader(a_list):

    a_list = [a,b,c]
    new_list=[]
    result = len(str(new_list))

    for i in range(a,b):
        if i%c == 0:
            new_list.append(i)

    return result
print(division_reader(a_list))
