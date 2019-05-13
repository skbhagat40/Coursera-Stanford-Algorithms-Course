# python program to find wheather there are two numbers in an array that add up to a particular number.
file = open(r"C:\users\skbha\videos\2sum.txt")
f = file.readlines()
nums = []
for line in f:
    nums.append(int(line))
s = set(nums)
ctr = 0
for el in range(-10000,10001):
    #print(el)
    for ela in s:
        if  el-ela in s and el != el-ela:
            print(el,ela,el-ela)
            ctr += 1
            break
print("the final count is",ctr)