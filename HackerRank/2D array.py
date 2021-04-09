# array = [
# 1 1 1 0 0 0 ---> 1 1 1       
# 0 1 0 0 0 0 --->   1
# 1 1 1 0 0 0 ---> 1 1 1
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# ]

arr = []
maxSum = -63
currentSum = 0

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))


def processRow(row):  # defines the rows of the array
    global maxSum
    row1 = row
    row2 = row + 1
    row3 = row + 2
    
    for col1 in range(0,4):  # defines the columns in the array
        col2 = col1 + 1
        col3 = col1 + 2
        topRow = arr[row1][col1] + arr[row1][col2] + arr[row1][col3] 
        midRow = arr[row2][col2]
        botRow = arr[row3][col1] + arr[row3][col2] + arr[row3][col3]

        currentSum = topRow + midRow + botRow
        #print(f"*** {currentSum}")

        if currentSum > maxSum : 
            maxSum = currentSum

            
def main():  # 
    for r in range(0,4):
        processRow(r)          
    print(maxSum)

    
if __name__ == '__main__':
    main()