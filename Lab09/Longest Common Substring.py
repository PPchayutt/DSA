def lcs(str1, str2):
    n = len(str1)
    grid = [[0 for i in range(n)] for j in range(n)]
    long_common = 0
    row_common = 0
    for row in range(n):
        for col in range(n):
            if str1[row] == str2[col]:
                grid[row][col] = grid[row-1][col-1] + 1
            
            if grid[row][col] > long_common:
                long_common = grid[row][col]
                row_common = row
    if long_common > 0:
        print(str1[row_common-long_common+1: row_common+1])
        print(long_common)
    else:
        print("No common substring.")

def main():
    str1 = input()
    str2 = input()
    lcs(str1, str2)
main()
