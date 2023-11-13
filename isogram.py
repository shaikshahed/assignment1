st='ba ckgro-u-nd'
def isogram(coll):
    uni=''
    i=0
    while i<len(coll):
        if coll[i] not in uni or coll[i] in [' ','-']:
            uni+=st[i]
        i+=1
    if uni==coll:
        print(coll,'is an isogram')
    else:
        print(coll,'is not an isogram')
isogram(st)