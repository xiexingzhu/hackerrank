# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 20:56:57 2016

@author: kid

leetcode 3sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        an=[]
        
        for i in range(len(nums)):
            if nums[i]<=0:
                tmp=-nums[i]
                j=i+1
                k=len(nums)-1
                
                if j<k:
                
                    while(j<k):
                        if nums[j]+nums[k]>tmp:
                            k-=1
                        elif nums[j]+nums[k]<tmp:
                            j+=1
                        else:
                            an.append([nums[i],nums[j],nums[k]])
                            j+=1
                        
        an.sort()
        for i in range(1,len(an)):
            if an[i]==an[i-1]:
                an[i-1]=-1
                
        an=[x for x in an if not x==-1]
        return an