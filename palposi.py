t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    freq = [0] * 26
    
    for c in s:
        freq[ord(c) - ord('a')] += 1
    
    odd_count = sum(1 for f in freq if f % 2 != 0)
    
    if k >= odd_count and k <= len(s):
        print("YES")
    else:
        print("NO")
