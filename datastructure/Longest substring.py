# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:07:27 2016

@author: kid

leetcode Longest Substring Without Repeating Characters
"""

def lengthOfLongestSubstring(s):
    i=0
    j=1
    count=1
        
    while(i<j and j<len(s)):
        if not s[j] in s[i:j]:
            j+=1
        else:
            count=max(count,j-i)
            while(i<j):
                if s[i]==s[j]:
                    break
                else:
                    i+=1
            i+=1
            j+=1
    return count
    
def threeSum(nums):
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
                        an.append([i,j,k])
                        
    print an
        
                
