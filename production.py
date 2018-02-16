#Write a function 'remove_duplicates' that takes
#in a list and returns a list without duplicatesself
#For examples:
#remove_duplicates([1,1,2,2])' should return '[1,2]'.

a_list = [1,2,3,4,5,1,2,3]

def remove_duplicates(a_list):
    new_list = []
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(remove_duplicates(a_list))
