def call_me(a):
    return 9


a=[12,3,4,5,6,7,7,8,9,10]
list2 =None
t=3
a.sort(key=call_me)#sort accepts boolean to sort the data
#default is always false
'''
a[1]="pop" ##for adding elements
a.append("kolaparthi") #2nd approach for adding elements
#a.remove(7)#for removing elements from collection
#a.pop()#2nd approach to remove element
print(a)
# Displaying values from collections
a.reverse()
list2=a.copy() # copying content from src
print(list2,"list222")
print(a)
print(a.count(7),"7ss")
print("No of Elements",len(a))
#a.clear()
#print("aa",a)
#Using foreach/any loop and enumerators/generators/iterators
# for destination variable in source variable:
#   code
'''
for x in a :
    print(x,"$")

'''

'''