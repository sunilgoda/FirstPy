import sys
a =4//2 #floor division - returns int
print(a)

b = 5/2 #returns float
print(b)

print(type(a)) #prints type of variable

print(sys.version) #prints version

c = 5
str(c) # str() - type casting to string
print(type(str(c)))

d = "Hyderabad Python Users Group"
print(dir(d)) # dir() - returns dunders & functions on variable

print(help("str")) # help()

print("capitalized " , d.capitalize())
print(d.upper())
print(d.split(' '))
print(d.lower())
print(d)

e= 'India\'s Best'
print(e)

#f =input('whats up') #seeks input
#print("type of f is %s" %type(f))

a,b = b,a #swapping
print(a)
print(b)
print("------------------------")
l = [1,2,3,4]
for i in l:
    print(i)
print(4 in l) # returns true if value is in list

r = range(10) # returns range from 0 to n
for i in r:
    print(i,end=',')
print()

r = range(11,14)
for i in r:
    print(i, end=',')
print("\n------------------------")

word = "Python3 Programming"
for i in word: #can be iterated over string
    if i is '3': # is can be used
        continue
    print(i,end='')

print("\n------------------------")
list1 = ['a',2,3.0]
for i in list1:
    print(i)
list1.append(4) #appends
print(list1[3])
list1.pop() #pops out
print(list1)
print(len(list1)) # length of list
list1.insert(2,2.2) #inserts in middle
print(list1)
print(list1[2:4]) #slicing -start index and ending index

list2 = [1,2,3,4,5,6,7,8,9]
print(list2[2:9:3]) # slicing with stepping of 3
print(list2[2::3]) # slicing till end
print(list2[::-1]) # reverses the iteration

str1 ="madam"
print(str1[::] == str1[::-1]) #tests for palindrome
print("------------------------")
tuple1 = (1,2,3,4,5)
print(type(tuple1))
tuple2 = 2,3,  #comma ending
print(len(tuple2))

int1,int2= tuple2 # tuple unpacking
print(int1)
print(int2)
print("------------------------")
set1 = set()
print(type(set1))
print(dir(set1))

duplist = [1,1,2,2,3,4]
duplist = set(duplist)
print(duplist)

print("------------------------")
dict1 = dict() #1st way
dict2 = {} #2nd way
dict3={"key1":"value1","key2":30}
print(dict3)
dict4={4:"val1","key2":5}
print(dict4)
dict5= {'names':['sun','god']}
dict5['ages'] = [1,2]
print(dict5)
print(dict5.keys()) #returns keys
print(dict5.get('names')) # returns value of keys
print(dict5.get('names1','defvalue')) # returns default value if key is not present
dict5.setdefault('locations','hyd')
print(dict5)
dict5['addresses'] = 'gachibowli'

for i,j in dict5.items(): #use items() to iteratte
    print(i)
    print(j)














