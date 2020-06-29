
# 给出n个链表，将它们排序成一个链表输出，最终是一个有序的链表

total_len=int(input())

final_arr=[]

for i in range(total_len):
    arr=list(map(int,input().split()))
    final_arr.extend(arr)

res=sorted(final_arr)

print(" ".join(map(str,res)))