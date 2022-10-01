# list1 = list(range(0,50))
# empty_list=[]
# for i in list1:
#     if i%2==0:
#         empty_list+=[i]
# print(empty_list)

str1 = "Hello Bapu How are you, You have done lots of thing for us."
empty_str=""
for i in str1:
    if i not in empty_str:
        empty_str+=i
print("Duplicate are removed :",empty_str)