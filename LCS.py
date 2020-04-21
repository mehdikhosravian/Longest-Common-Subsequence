X='AGGTAB'
Y='GXTXAYB'

class LongestCS:
    lcs = ""
    val = 0

def LCS (X, Y, m, n):
    L=[[LongestCS() for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j].val = 0
                L[i][j].lcs = ""
            elif X[i-1] == Y[j-1]:
                L[i][j].val = L[i-1][j-1].val + 1
                L[i][j].lcs = L[i-1][j-1].lcs + Y[j-1]
            elif L[i][j-1].val >= L[i-1][j].val:
                L[i][j].val = L[i][j-1].val
                L[i][j].lcs = L[i][j-1].lcs
            else:
                L[i][j].lcs = L[i-1][j].lcs
                L[i][j].val = L[i-1][j].val          
    print('The length of LCS is {} and the common subsequence is {}'.format(L[m][n].val,L[m][n].lcs))
LCS(X,Y,len(X),len(Y))

