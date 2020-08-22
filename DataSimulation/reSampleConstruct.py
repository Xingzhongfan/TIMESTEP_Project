# Author: Xingzhong Fan
# Resample method constuct differet days data
# Input:
#     inData: List of Data input
#     sampleTimes: resample how many times ex:180
# Output:
#     outData: List of output Data
def reSampleConstruct(inData,sampleTimes):
    outData = []
    for i in range(sampleTimes):
        temp_index = random.randint(0,len(inData)-1)
        outData.append(inData[temp_index])
    return outData