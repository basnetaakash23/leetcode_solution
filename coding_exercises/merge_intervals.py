def merge_intervals(intervals):
    x = 1
    while(x < len(intervals)):
        if(intervals[x-1][1] >= intervals[x][0] and intervals[x-1][0] < intervals[x][0]):
            first  = intervals[x-1]
            second = intervals[x]
            intervals[x-1] = [0,0]
            intervals.pop(x)
            intervals[x-1] = [first[0]]+[second[1]]

        elif(intervals[x-1][0] > intervals[x][0] and intervals[x-1][1] <= intervals[x][1]):
            first  = intervals[x-1]
            second = intervals[x]
            intervals[x-1] = [0,0]
            intervals.pop(x)
            intervals[x-1] = [second[0]]+[second[1]]

        else:
            x+=1

        print(intervals)
    return intervals

# print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[1,4],[0,4]]))