import numpy as np

a=input("Enter string1:\t")
b=input("Enter string2:\t")


m=len(a)
n=len(b)

 
l = np.zeros([m+1,n+1],dtype=int) 
#print("Matrix b : \n", l)

for i in range(m+1):
    #print("string a",a[i-1])
    for j in range(n+1):
        #print("string b",b[j-1])
        if i==0 or j==0:
            l[i,j]=0
        elif (a[i-1]==b[j-1]):
            l[i,j]=1+l[i-1,j-1]
        else:
            
            l[i,j]=max(l[i-1,j],l[i,j-1])
index = l[m][n] 
#print(index)  
# Create a character array to store the lcs string 
lcs = [""] * (index+1)
#print(lcs)
lcs[index] = ""  
i = m 
j = n 
while i > 0 and j > 0: 
  
    # If current character in X[] and Y are same, then 
    # current character is part of LCS 
    if a[i-1] == b[j-1]: 
        lcs[index-1] = a[i-1] 
        i-=1
        j-=1
        index-=1
  
    # If not same, then find the larger of two and 
    # go in the direction of larger value 
    elif l[i-1][j] > l[i][j-1]: 
        i-=1
    else: 
        j-=1
print(l)  
print ("The largest common subsequence is:\t","".join(lcs))
print("The letter in common are:\t ",l[-1][-1])

