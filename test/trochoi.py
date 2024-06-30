def min_cost_card(max_pos,card,max_):
    N=len(card)
    dp=[float('inf')]*(max_pos+1)
    dp[0]=0
    for i in range (N):
        for x in range (max_pos,-1,-1):
            if dp[x]!=float('inf'):
                if x+card[i][0]<=max_pos:
                    dp[x+card[i][0]]=min( dp[x+card[i][0]],dp[x]+card[i][1])
    if dp[max_]==float('inf'):
        return -1
    else:
        return dp[max_]
    

for t in  range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=list(map(int,input().split()))
    card= list(zip(a,c))
    max_position=max(sum(a),1)
    m=max(a)-1
    print(min_cost_card(max_position,card,m))
