int(input())
s = input().split()
b = list(input())

temp = [0]*len(s)
c = 0

for i in range(len(s)):
    for j in range(len(s[i])-1):
        if b[i+j] == b[i+j+1]:
            temp[i-1] = 1
        else:
            temp[i-1] = 0 

print(sum(temp))
