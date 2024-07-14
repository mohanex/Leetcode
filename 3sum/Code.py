class Solution:
    def threeSum(nums: list[int]) -> list[list[int]]:
        length_num = len(nums)
        res = []
        num_eq = 0
        for i in range(0,length_num-2):
            for j in range (i+1,length_num-1):
                for k in range (j+1,length_num):
                    if nums[i]+nums[j]+nums[k]==0: #and i!=j and i!=k and j!=k
                        if res:
                            for list in res:
                                for number in list:
                                    if number==nums[i] or number==nums[j] or number==nums[k]:
                                        num_eq +=1
                        if num_eq < 3:
                            res.append([nums[i],nums[j],nums[k]])
                        num_eq = 0
        return res
    
class main():
    print(Solution.threeSum(nums = [-1,0,1,2,-1,-4]))