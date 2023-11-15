t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if s.count('T') == 1 and s.count('i') == 1 and s.count('m') == 1 and s.count('u') == 1 and s.count('r') == 1 and len(s) == 5:
        print("YES")
    else:
        print("NO")
