def BinarySearch(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
list=[1,4,6,8,11,24,45,67,80,93,100]
n=80
if BinarySearch(list,n):
    print("Found")
else:
    print("Not found")