String ="aaabbbccc";
container=[]
element=[]
count=0
dict={}
for i in String:
    if(container==[]):
        container.append(i)
    else:
        if(i not in container):
           container.append(i)
           
#The element are stored in container to get there count in the string
for i in container:
    Counter=String.count(i);
    dict.update( {i : Counter} )
print(dict)

bEqual=True
element.append(list(dict.values()))
print("dictionary values are saved in list:",element)

#nTemp is storing first value of the dictionay
nTemp = element[0][0]

print()
#so we are running an for loop for comparing the value of dictionary
for item in dict.values():
  if nTemp != item:
    bEqual = False
    break;
 
if bEqual:
   print("The given ",String,"is valid")
else:
   print("The given ",String," is invalid")




    

