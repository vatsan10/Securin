def probabilityOfPossibleSums():
    dieFaces = 6
    combinations = [0] * (dieFaces * 2 + 1)  # +1 for sums from 2 to 12
    for i in range(1, dieFaces + 1):
        for j in range(1, dieFaces + 1):
            sum = i + j
            combinations[sum] += 1
    for sum in range(2, 13):
        print(f"Sum {sum} => Count:{combinations[sum]} Probability:{combinations[sum]/36} Combinations:",end=" ")
        # Print the combinations for the current sum
        for i in range(1, dieFaces + 1):
            for j in range(1, dieFaces + 1):
                if i + j == sum:
                    print(f"({i}, {j})",end=" ")
        print()

probabilityOfPossibleSums()
