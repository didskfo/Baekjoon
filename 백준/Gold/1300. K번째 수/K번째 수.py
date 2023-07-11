n = int(input())
k = int(input())

start, end = 1, k

while start <= end:
    mid = (start+end)//2
    cnt = 0
    
    for i in range(1, n+1):
        cnt += min(mid//i, n)
        
    if cnt >= k:
        end = mid-1
    else:
        start = mid+1
        
print(end+1)