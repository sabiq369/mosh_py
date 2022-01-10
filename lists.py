# print("Enter numbers and i will tell you the greatest number you input ")
# for numbers in range(0,3) :
#     choice = 3 - numbers
#     list = [(int(input(f'{choice} choice you got : ')))]
# list.sort()
# print(list)
    

# list = [1,5,8,7777,68888]
# for i in list :
#     for j in list  :
#         if i < j :
#             temp = i
#             i = j 
#             j = temp
# print(i)




list = [5,2,6,6,8,8,4,55,44,77]
list.sort()
for i in list :
    for j in list :
        j=j+1
        if i==j :
            print(" ")
            continue

print(list)

