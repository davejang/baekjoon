def LCS(X, Y):
	# code here!
	dp = [[0 for cols in range(len(Y)+1)]for rows in range(len(X)+1)]
	lcs_length = 0
	LCS = []
	for i in range(1,len(X)+1):
		for j in range(1,len(Y)+1):
			if X[i-1] == Y[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
				lcs_length = lcs_length + 1
				if(dp[i][j] == lcs_length):
					LCS.append(X[i-1])
			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	return(dp[len(X)][len(Y)],LCS)

X = input().strip()
Y = input().strip()
k, S = LCS(X, Y)
print(k)