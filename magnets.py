n = int(input())

magnets = []

for _ in range(n):
    magnets.append(input().strip())  

group = 1  

for i in range(1, len(magnets)):
    if magnets[i] != magnets[i-1]:  
        group += 1  

print(group)