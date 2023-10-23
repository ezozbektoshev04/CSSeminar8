myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}


module=input("Module name ")
mark=input("Mark here ")
myFinalMarks[module]=int(mark)
print(myFinalMarks)

def calaculateAverage(finalMarks):
    total=0
    for key in finalMarks:
        total=total+finalMarks[key]
        average=total/len(finalMarks)
    return average
print(calaculateAverage(myFinalMarks))