def find_median(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)

    if(l1<=l2):
        print("Inside")
        final_arr = []
        x = 0
        y = 0
        while(x<l1):
            if(arr1[x]<arr2[y]):
                final_arr.append(arr1[x])
                x+= 1

            elif(arr1[x]>arr2[y]):
                final_arr.append(arr2[y])
                y = y+1

            else:
                final_arr.append(arr1[x])
                final_arr.append(arr1[y])
                x += 1
                y += 1

        final_arr.extend(arr1[x:])
        final_arr.extend(arr2[y:])

    else:
        print("Else")
        final_arr = []
        x = 0
        y = 0
        while(x<l2):
            if(arr1[x]<arr2[y]):
                final_arr.append(arr1[x])
                x+= 1

            elif(arr1[x]>arr2[y]):
                final_arr.append(arr2[y])
                y = y+1

            else:
                final_arr.append(arr1[x])
                final_arr.append(arr1[y])
                x += 1
                y += 1

        final_arr.extend(arr1[x:])
        final_arr.extend(arr2[y:])

    length = len(final_arr)
    med = (length + 1)/2
    median = (final_arr[int(med)-1]+final_arr[int(med)])/2
    return median


            





print(find_median([1,2],[5,6]))
