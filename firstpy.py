print("hello world")
x = 5
print(type(x))
x=str(x)
print(type(x))
a = "hello"

print("hello world",x)
names=["ermi","ermu",'erma']
v,y,z = names
print(v,z,y) 
for c in names:
    print(c)

print("ermi" in names)
print(names[0].replace("e","i"))
print(names)

fruits=["banana","apple","orange"]

fruits.extend([x for x in names])

print(fruits)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

print(mytuple.index("apple"))

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

set1= {"a",True,"data3"}
set2={"b",mytuple,}
set3=set1.union(set2)
print(set3)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)
