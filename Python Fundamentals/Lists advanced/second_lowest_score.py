temp = []
scores = set()
names = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp.append([name, score])
        scores.add(score)
    second_lowest = sorted(scores)[1]

for name, score in temp:
    if score == second_lowest:
        names.append(name)

for i in sorted(names):
    print(i, end='\n')