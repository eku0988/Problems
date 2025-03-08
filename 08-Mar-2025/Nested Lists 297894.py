# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    nameScore=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameScore.append((name,score))
        
    nameScore.sort(key=lambda x: x[1])

    Scores=sorted(set(score for _,score in nameScore))
    if len(Scores) > 1:
        second_lowest = Scores[1]
    else:
        second_lowest = Scores[0]

    result = sorted([name for name, score in nameScore if score == second_lowest])

    for name in result:
        print(name)
