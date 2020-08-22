# Author: Xingzhong Fan
# This function calculate segement porbability of move or walk
# Input:
#      oneDayLable: one day generate data
#      segment: time segment  eg: 5min or 10min or 15min
# Output:
#      T: generate time list for one day
#  mean_day: mean segment value for each day
def segmentProb(oneDayLable,segment):
    mean_day = []
    mean_day.append(0)
    T = np.arange(0,(segment/60*24*60/segment)+segment/60,segment/60)
    for item in oneDayLable:
        for j in range(0,len(item),segment):
            avg = np.mean(item[j:j+segment])
            mean_day.append(avg)
    return T, mean_day

