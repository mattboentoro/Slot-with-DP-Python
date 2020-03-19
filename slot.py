def declarearray(row,col):
    array=[]
    for i in range (row):
        arraytemp=[]
        for j in range (col):
            print("Enter the row "+str(i)+" and column "+str(j)+" item:")
            num=int(input("Enter here... "))
            arraytemp.append(num)
        print("Row "+ str(i) +" complete")
        array.append(arraytemp)
    return array
def declarearrayzero(row,col):
    array=[]
    for i in range (row):
        arraytemp=[]
        for j in range (col):
            arraytemp.append(0)
        array.append(arraytemp)
    return array
def printarray(array,row,col):
    for i in range(row):
        for j in range(col):
            print(str(array[i][j])+" ", end='')
        print()
def minfinder(array,row,col):
    arraycheck=declarearrayzero(row,col)
    increment=declarearrayzero(row,col)
    for i in range(row-1,-1,-1):
        for j in range(col):
            if(i==row-1):
                if(array[i][j]!=0):
                    increment[i][j]=1
                else:
                    increment[i][j]=0
                arraycheck[i][j]=array[i][j]
            else:
                if (j==0):
                    if(array[i][j]!=0):
                        arraycheck[i][j]=array[i][j]+arraycheck[i+1][j+1]
                        increment[i][j]=increment[i+1][j+1]+1
                    else:
                        arraycheck[i][j]=arraycheck[i+1][j]
                        increment[i][j]=increment[i+1][j]
                elif (j==col-1):
                    if(array[i][j]!=0):
                        arraycheck[i][j]=array[i][j]+arraycheck[i+1][j-1]
                        increment[i][j]=increment[i+1][j-1]+1
                    else:
                        arraycheck[i][j]=arraycheck[i+1][j]
                        increment[i][j]=increment[i+1][j]
                else:
                    if(array[i][j]!=0):
                        if((array[i][j]+arraycheck[i+1][j+1])<(array[i][j]+arraycheck[i+1][j-1])):
                            arraycheck[i][j]=arraycheck[i+1][j+1]+array[i][j]
                            increment[i][j]=1+increment[i+1][j+1]
                        else:
                            arraycheck[i][j]=array[i][j]+arraycheck[i+1][j-1]
                            increment[i][j]=1+increment[i+1][j-1]
                    else:
                        arraycheck[i][j]=arraycheck[i+1][j]
                        increment[i][j]=increment[i+1][j]
    index=0
    for j in range(1,col):
        if(arraycheck[0][j]<arraycheck[0][index]):
            index=j
    print("Ball slot "+str(index+1))
    print("Minimum value: "+str(arraycheck[0][index]))
    print("Number found: "+str(increment[0][index]))
def maxfinder(array,row,col):
    arraycheck=declarearrayzero(row,col)
    increment=declarearrayzero(row,col)
    for i in range(row-1,-1,-1):
        for j in range(col):
            if(i==row-1):
                if(array[i][j]!=0):
                    increment[i][j]=1
                else:
                    increment[i][j]=0
                arraycheck[i][j]=array[i][j]
            else:
                if (j==0):
                    if(array[i][j]!=0):
                        arraycheck[i][j]=array[i][j]+arraycheck[i+1][j+1]
                        increment[i][j]=increment[i+1][j+1]+1
                    else:
                        arraycheck[i][j]=arraycheck[i+1][j]
                        increment[i][j]=increment[i+1][j]
                elif (j==col-1):
                    if(array[i][j]!=0):
                        arraycheck[i][j]=array[i][j]+arraycheck[i+1][j-1]
                        increment[i][j]=increment[i+1][j-1]+1
                    else:
                        arraycheck[i][j]=arraycheck[i+1][j]
                        increment[i][j]=increment[i+1][j]
                else:
                    if(array[i][j]!=0):
                        if((array[i][j]+arraycheck[i+1][j+1])>(array[i][j]+arraycheck[i+1][j-1])):
                            arraycheck[i][j]=arraycheck[i+1][j+1]+array[i][j]
                            increment[i][j]=1+increment[i+1][j+1]
                        else:
                            arraycheck[i][j]=array[i][j]+arraycheck[i+1][j-1]
                            increment[i][j]=1+increment[i+1][j-1]
                    else:
                        arraycheck[i][j]=arraycheck[i+1][j]
                        increment[i][j]=increment[i+1][j]
    index=0
    for j in range(1,col):
        if(arraycheck[0][j]>arraycheck[0][index]):
            index=j
    print("Ball slot "+str(index+1))
    print("Maximum value: "+str(arraycheck[0][index]))
    print("Number found: "+str(increment[0][index]))

row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of cols: "))
array=declarearray(row,col)
printarray(array,row,col)
print()
maxfinder(array,row,col)
minfinder(array,row,col)
