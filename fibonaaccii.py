r = 10
n1=0
n2=1
temp = n1+n2
for i in range(1,r+1): #i=1 now as i=2,n1=1 and n2=1
    print(temp) # temp=1 and temp=2
    n1=n2 # 0 =1 now n1=n2=1 as n1=n2, so we take bigger number for both, so n1=1 and n2=1,,--n1=n2=1
    n2=temp #= n2 = 1 as value of temp,--n2=2 as value if temp
    temp=n1+n2  # temp=1+1 = 2 --- temp=1+2=3