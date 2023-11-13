num=153
def armstrong(st):
    temp=st
    count=0
    while temp:
        count+=1
        temp=temp//10
    sum1=0
    res=st
    while res:
        ld=res%10
        sum1=ld**count+sum1
        res=res//10
    if sum1==st:
        print(st,'is an armstrong number')
    else:
        print(st,'is not an armstrong number')
armstrong(num)

