import string
import string
lst = []
for letter in string.ascii_uppercase:
    lst.append(letter)
n = 0
m = int(input())
st = input()
st.split()
st = [i.upper() for i in st]
for i in range(26):
    if st.count(lst[i]) >= 1:
        n = n + 1

if n == 26:
    print("YES")
else:
    print("NO")

   
