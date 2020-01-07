def minion_game(s):
    score_s=0 # for stuart
    score_k=0 # for kevin
    vowels='AEIOU'
    for i in range(len(s)):
        print(i, len(s))
        if s[i] in vowels:
            score_k += (len(s) - i)
        else:
            score_s += (len(s) - i)

    if (score_k > score_s):
        print("Kevin", score_k)
    elif (score_k < score_s):
        print("Stuart", score_s)
    else:
        print("Draw")


if __name__=="__main__":
    inp= str(input("Enter the string")).upper()
    minion_game(inp)