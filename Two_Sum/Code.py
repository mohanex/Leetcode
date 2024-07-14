class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        List_length = len(nums)
        #print(List_length)
        if List_length<3 :
            return [0,1]
        else :
            for i in range(0,List_length-1):
                #print(i)
                for j in range (i+1,List_length):
                    #print(j)
                    if nums[i]+nums[j] == target:
                        return [i,j]

class main():
    print(Solution.twoSum(nums = [3,3], target = 6))
    print(Solution.twoSum(nums = [4,2,9,0,6,3,9,1,0,76,98,3,4,2,23,51], target = 74))