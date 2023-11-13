s='cool'
temp=[]
for i in s:
    temp.append(ord(i))
k=26
res=''
for code in temp:
    if 65<=code<=90:
        res+=chr(((code+k-65)%26)+65)
    elif 97<=code<=122:
        res+=chr(((code+k-97)%26)+97)
    elif code==32:
        res+=chr(32)
print(res)
