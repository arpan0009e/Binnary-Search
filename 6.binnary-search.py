#binary search
n=int(input("Enter the length of the list: "))
l=[]
for i in range(n):
    l.append(int(input("Enter the elemnt of the list: ")))
l.sort()
print("List: ",l)
flag=0
low=0
high=(n-1)
# mid=low+high//2
key=int(input("Enter the key value: "))
while low<=high:
    mid = (low + high) // 2
    if l[mid] == key:
        flag=1
        break
    elif l[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if(flag==1):
     print("Element found at index: ",mid)
else:
    print("Element not found")