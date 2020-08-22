# Author: Xingzhong Fan
# This function generate one day data with stay or move
# Input:
#      moveLst: move hour list like [1,2,3] value from 0 to 23
#      sleepLst: sleep hour list like [1,2,3] value from 0 to 23
# Output:
#      lable: lable for each data point, segment is 0.1s. 0 is stay and 1 is move.
#          H: a list contain each hour data
# AccMeanMin: absolute mean value for each min
# move binomial value is 0.8, sleep is 0.05, other is 0.2 user can change this parameter
def GeneOneDay(moveLst,sleepLst):
    
    a0 = 0.054716176713898716
    stda0 = 0.07421516580102121
    a1 = 1.7954484714160643
    stda1 = 2.7741157783195645
    
    lable = []
    H = []
    AccMeanMin = []
    print(moveLst)
    print(sleepLst)
    for i in range(1,25):
        tempH = []
        temp_lable = []
        temp_AccMeanMin = []
        if(i in moveLst):
            for j in range(0,60):
                gene = np.random.binomial(1,0.8)
                if(gene==0):
                    test = np.random.normal(loc=a0, scale=stda0, size=600)
                    tempH.append(test)
                    temp_lable.append(gene)
                elif(gene==1):
                    test = np.random.normal(loc=a1, scale=stda1, size=600)
                    tempH.append(test)
                    temp_lable.append(gene)
            for j in range(0,60):
                temp_AccMeanMin.append(np.mean(abs(tempH[j])))
            lable.append(temp_lable)
            H.append(tempH)
            AccMeanMin.append(temp_AccMeanMin)
        elif(i in sleepLst):
            for j in range(0,60):
                gene = np.random.binomial(1,0.05)
                if(gene==0):
                    test = np.random.normal(loc=a0, scale=stda0, size=600)
                    tempH.append(test)
                    temp_lable.append(gene)
                elif(gene==1):
                    test = np.random.normal(loc=a1, scale=stda1, size=600)
                    tempH.append(test)
                    temp_lable.append(gene)
            for j in range(0,60):
                temp_AccMeanMin.append(np.mean(abs(tempH[j])))
            lable.append(temp_lable)
            H.append(tempH)
            AccMeanMin.append(temp_AccMeanMin)
        else:
            for i in range(0,60):
                gene = np.random.binomial(1,0.2)
                if(gene==0):
                    test = np.random.normal(loc=a0, scale=stda0, size=600)
                    tempH.append(test)
                    temp_lable.append(gene)
                elif(gene==1):
                    test = np.random.normal(loc=a1, scale=stda1, size=600)
                    tempH.append(test)
                    temp_lable.append(gene)
            for j in range(0,60):
                temp_AccMeanMin.append(np.mean(abs(tempH[j])))
            lable.append(temp_lable)
            H.append(tempH)
            AccMeanMin.append(temp_AccMeanMin)
    return lable, H, AccMeanMin