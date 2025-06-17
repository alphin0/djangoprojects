d = input('Enter a sentence:')
def sentence(d):
    words=d.split()
    d1={}
    for i in words:
        if i not in d1:
            d1[i]={'length':len(i),
                             'is palindrome':i==i[::-1],
                             'count':1
            }
        else:
            d1[i]['count']+=1
    return d1

result=sentence(d)
for i,j in result.items():
    print(f'"{i}":{j}')

