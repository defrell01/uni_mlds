a = int(input())

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def mcd(n,m):
    return (n/gcd(n,m))*m

def pick(arr):
    res = 0
    min = 2147483647
    if len(arr) == 0:
        return arr[0]
    else:
        for i in range(len(arr)):
            if mcd(arr[i][0], arr[i][1]) < min:
                min = mcd(arr[i][0], arr[i][1])
                res = i
        return res

        
temp = []


i = 1
while (i <= a-i):
    temp.append([i, a-i])
    i += 1

print(*temp[pick(temp)])
# 8

# 0 8 
# 1 7
# 2 6
# 3 5
# 4 4
