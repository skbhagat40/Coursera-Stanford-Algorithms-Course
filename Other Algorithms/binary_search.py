'''Binary Search Implementation . O(logN) runtime complexity'''

def binary_search(list,n):
    low = 0
    high = len(list)
    mid = (high+low)//2
    while(high>=low):
        print("mid",list[mid],n,high,low)
        if list[mid] > n:
            high = mid -1
        elif list[mid]<n:
            low = mid + 1
        else:
            print("found")
            return True
        mid = (high+low)//2
print(binary_search([1,2,8,21,55],27))