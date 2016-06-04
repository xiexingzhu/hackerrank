# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 22:02:03 2016

@author: kid

hackerrank Algorithms Dynamic Programming Bricks Game
"""
"""
Given a stack of bricks, You have to remove the bricks in such a way that you get the maximum possible socore while It is given that other player will also play optimally. 
So,
Suppose numbers written on bricks are a[0], a[1]....., a[n-1] where a[0] is the bottom-most brick. 
Consider another array of prefix sum i.e. sum[n]
where sum[i] = a[0] + a[1] + ....+ a[i]
Consider another array dp[n]
where dp[i] = maximum score of first player for stack a[0],a[1]...,a[i] when he is playing optimally. 
It is obvious that,
dp[0] = a[0]
dp[1] = a[0] + a[1]
dp[2] = a[0] + a[1] + a[2]

Now suppose that dp[0], dp[1],....., dp[k-1] has been calculated and we want to calcualte dp[k].

For kth brick, first player will have 3 options.
Pick one 
Then first player will get a[k] and his opponenet will get dp[k-1] so first will get { (sum[k-1] - dp[k-1]) + a[k] } in total.
Pick two 
Then first player will get a[k]+a[k-1] and his opponenet will get dp[k-2] so first will get { (sum[k-2] - dp[k-2]) + a[k]+ a[k-1] } in total.
Pick three 
Then first player will get a[k]+a[k-1]+a[k-2] and his opponenet will get dp[k-3] so first will get { (sum[k-3] - dp[k-3]) + a[k]+ a[k-1] +a[k-2] } in total.
so dp[k] = max {(sum[k-1] - dp[k-1]) + a[k] ,(sum[k-2] - dp[k-2]) + a[k]+ a[k-1], (sum[k-3] - dp[k-3]) + a[k]+ a[k-1] +a[k-2] }
This can be calculated in O(1) time, so total time needed will be O(n).
"""

# really brilliant method

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    v = map(int,raw_input().split())
    c = [0]*n
    c[n-1] = v[n-1]
    c[n-2] = v[n-2]+v[n-1]
    c[n-3] = v[n-3]+v[n-2]+v[n-1]
    sc = c[n-3]
    for i in range(n-4,-1,-1):
        sc += v[i]
        c[i] = sc - min(c[i+1],c[i+2],c[i+3])
    print c[0]