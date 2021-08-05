def find132pattern(nums):
    def generate_subset(nums, arr, index):
        print("Arr",arr)
        if(len(arr)==3):
            if(arr[0] < arr[2] and arr[2] < arr[1]):
                return True
            return False

        elif(index > len(nums)-2):
            return False

        elif(len(arr)>3):
            return False
        else:
            return generate_subset(nums,arr,index+1) or generate_subset(nums, arr+[nums[index+1]],index+1) or generate_subset(nums,[nums[index+1]], index+1)

    return generate_subset(nums, [nums[0]],0)


#print(find132pattern([3,1,4,2]))

print(find132pattern([-1,3,2,0]))