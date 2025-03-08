# Problem: Runner-up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    noduplicate=list(set(arr))
    if len(noduplicate) < 2:
        print("No second largest element") 
    else:
        maximum=sorted(noduplicate,reverse=True)[1]
        print(maximum)
