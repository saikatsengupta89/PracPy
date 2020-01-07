from collections import Counter
def company_logo(string):
    c = Counter(sorted(string))
    for i in c.most_common(3):
        print(i[0] + " " + str(i[1]))

if __name__=="__main__":
    string= input("Enter the company logo :")
    company_logo(string)