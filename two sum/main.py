# n = [2,7,11,15]
# targ = 9
#
# def Twosum(nums, target):
#     seen = {}
#
#     for i, num in enumerate(nums):
#         if target - num[i] in seen:
#             return ([seen[target - num], i])
#         elif num not in seen:
#             seen[i] = i
#
# a = Twosum(n, targ)
#
# print(a)