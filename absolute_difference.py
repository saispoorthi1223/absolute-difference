'''you are given an arrray arr of n positive integers.Partition this array into twi subsets such that the absolute difference between
the sums of the subsets is minimized.
write a function min_difference(arr) thet returns this minimun possible difference.
example input: arr=[1,6,11,5]   outpput: 1'''
def min_difference_tab(arr):
    totalsum=sum(arr)
    n=len(arr)
    halfsum=totalsum//2
    dp=[[False]*(halfsum+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,halfsum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    for j in range(halfsum,-1,-1):
        if dp[n][j]:
            return totalsum-2*j
arr=[1,6,11,5]
print(min_difference_tab(arr))

''' recursion
def find_min_diff(arr,n,sum_calculated,sum_total):
    if n==0:
        return abs((sum_total-sum_calculated)-sum_calculated)
    include=find_min_diff(arr,n-1,sum_calculated+arr[n-1],sum_total)
    exclude=find_min_diff(arr,n-1,sum_calculated,sum_total)
    return min(include,exclude)
def min_dif(arr):
    sum_total=0
    for num in arr:
        sum_total+=num
    return find_min_diff(arr,len(arr),0,sum_total)
arr=[1,5,11,5]
print(min_dif(arr))


*Memorization
def find_min_dif_memo(arr,n,sum_cal,sum_t,memo):
    if n==0:
        return abs((sum_t-sum_cal)-sum_cal)
    if(n,sum_cal)in memo:
        return memo[(n,sum_cal)]
    include=find_min_dif_memo(arr,n-1,sum_cal+arr[n-1],sum_t,memo)
    exclude=find_min_dif_memo(arr,n-1,sum_cal,sum_t,memo)
    memo[(n,sum_cal)]=min(include,exclude)
    return memo[(n,sum_cal)]
def min_dif_memo(arr):
    sum_t=sum(arr)
    memo={}
    return find_min_dif_memo(arr,len(arr),0,sum_t,memo)
arr=[1,5,11,5]
print(min_dif_memo(arr))
'''


