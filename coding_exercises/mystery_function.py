from interval import interval, imath, inf
def mysteryFunction(arr):
    arr = sorted(arr, key = lambda interval:interval.start)

    stack = []
    stack.append(arr[0])

    for i in range(1, len(arr)):
        top = stack[-1]
        if(top.end < arr[i].start):
            stack.append(arr[i])

        elif(top.end<arr[i].end):
            top.end = arr[i].end
            stack.pop()
            stack.append(top)

    for t in stack:
        print('['+str(t.start)+','+str(t.end)+'] ')


arr = []
arr.append(Interval(6,8))
arr.append(Interval(1,9))
arr.append(Interval(2,4))
arr.append(Interval(4,7))
mysteryFunction(arr)