def getdata():
    ravinshu=[2,7,11,15]
    return ravinshu
def calculation(data):
    sum=0
    for i in data:
        sum=sum+i
        
    return sum

def finalresult(final):
    return final/2
finalresult(calculation(getdata()))