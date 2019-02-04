import math
x=[185,170,168,179,182,188]
y=[72,56,60,68,72,77]

k=2

clust1=["cluster1"]
clust2=["cluster2"]

k1=[]
k2=[]
k1.append([x[0],y[0]])
k2.append([x[1],y[1]])


for i in range(0,len(x)-1):
    
    c1=(x[i+1]-k1[0][0])**2
    c2=(y[i+1]-k1[0][1])**2
    print(c1)
    print(c2)
    print(math.sqrt((c1+c2)))
    clust1.append(math.sqrt((c1+c2)))
    
for i in range(len(x)):
    c11=(k2[0][0]-x[i])**2
    c22=(k2[0][1]-y[i])**2
    print(c11)
    print(c22)
    
    print(math.sqrt((c11+c22)))
    if math.sqrt((c11+c22))==0:
          print(0);
    else:
        clust2.append(math.sqrt((c11+c22)))
   
    if clust1[i] > clust2[i]:
        
        k2[0]=[(k2[0][0]+x[i])/2,(k2[0][1]+y[i])/2]
        print(k2)
    else:
        k1[0]=[(k1[0][0]+x[i])/2,(k1[0][1]+y[i])/2]
        print(k1)
    
        
    
print(k1)
print(k2)
print(clust1)   
print(clust2)


  
    
    

   
    
    
    
        
   
   

   
   


