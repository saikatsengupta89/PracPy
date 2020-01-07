def climbingLeaderboard(scores, alice):
    rank=list()
    rnk=1
    scores_sort= sorted(scores, reverse=True)
    rank.append(rnk)
    for i in range(len(scores_sort)-1):
        if scores_sort[i+1]== scores_sort[i]:
            rank.append(rnk)
        else:
            rnk=rnk+1
            rank.append(rnk)
    print(scores_sort)
    print(rank)
    for i in alice:
        for j in range(len(scores_sort)):
            if i < min(scores_sort):
                print(max(rank) + 1)
                break
            elif i > max(scores_sort):
                print(1)
                break
            elif (scores_sort[j] > i and i > scores_sort[j+1]):
                print(rank[j+1])
                break
            elif scores_sort[j]== i:
                print(rank[j])
                break
            else:
                continue

if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)

