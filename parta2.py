def displayPossibleCombinations():
    combinations = [[0] * 6 for _ in range(6)]
    distribution = [[0] * 6 for _ in range(6)]

    for i in range(1,7):
        for j in range(1,7):
            combinations[i-1][j-1] = ((i), (j))
            distribution[i-1][j-1] = i + j
    print("Combinations")
    for row in combinations:
        print(*row)
    print("Distributions")
    for row in distribution:
        print(row)
displayPossibleCombinations()