from .max import max

def lcs(string1: str, string2: str):
    m = len(string1)
    n = len(string2)

    operations = 0
    subsequence = ""

    L = [[None for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            operations += 1

            if i == 0 or j == 0:
                L[i][j] = 0

            elif string1[i - 1] == string2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1

                if L[i][j] == len(subsequence) + 1:
                    subsequence += string1[i - 1]

            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    length = L[m][n]

    print(string1 + '\t' + string2 + '\t' + str(length) + '\t' + subsequence + '\t' + str(operations))

    return length