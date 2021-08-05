def insert_interval(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(key = lambda x: x[1])
    print(intervals)
    for x in range(0, len(intervals)):

        if(new_interval[0]<=intervals[x][0] or new_interval[0] <= intervals[x][1]):
            if(new_interval[0]<intervals[x][0]):
                intervals[x][0] = new_interval[0] 

            y = x+1
            while(intervals[y][0]!=new_interval[0] and intervals[y][1] != new_interval[1]):
                print(intervals[y])
                # intervals.pop(y)
                y += 1
                                                                                                                                                                                               
            
            if(intervals[y+1][0]==intervals[y][1]):
                intervals[x][1] = intervals[y+1][1]
                intervals = intervals[:x+1]+intervals[y+2:]
                break
            
            intervals[x][1] = intervals[y][1]
            intervals = intervals[:x+1]+intervals[y+1:]
            
            break

    return intervals
    print(intervals)








print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))