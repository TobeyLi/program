# 还能种植的最大的树木
# 5
# 1 0 0 0 0  ==》 1 0 1 0 1
# 输出：2

total_len=int(input())
arr=list(map(int,input().split()))

print(arr)

max_num=0
count=1

for i in range(len(arr)):
    if(arr[i]==0):
        count+=1
    else:
        count=0
    if count==3:
        max_num+=1
        count=1
if count==2:
    max_num+=1

print(max_num)