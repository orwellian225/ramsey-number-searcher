import sys
import math

num_objects = int(sys.argv[1])
combination_len = int(sys.argv[2])
desired_object = int(sys.argv[3])

print("Number of objects:", num_objects)
print("Combination length:", combination_len)
print("Desired object:", desired_object)

node_count = 0
def recursive_combinations(depth, length, combination, list_of_combinations, with_obj):
    global node_count
    node_count = node_count + 1

    print((depth - 1) * "\t" + "|-------" + str(combination[-1]) if depth != 0 else "root")

    if depth == length - 1 and with_obj not in combination:
        combination.append(with_obj)
        list_of_combinations.append(combination)
        return
    elif depth == length - 1:
        for i in range(combination[-1] + 1, num_objects - (length - depth) + 1): 
            new_combination = combination.copy()
            new_combination.append(i)
            list_of_combinations.append(new_combination)
        return

    if depth != 0:
        for i in range(combination[-1] + 1, num_objects - (length - depth) + 1):
            new_combination = combination.copy()
            new_combination.append(i)
            recursive_combinations(depth + 1, length, new_combination, list_of_combinations, with_obj)
    else:
        for i in range(0, num_objects - (length - depth) + 1):
            new_combination = combination.copy()
            new_combination.append(i)
            recursive_combinations(depth + 1, length, new_combination, list_of_combinations, with_obj)


combinations = []
recursive_combinations(0, combination_len, [], combinations, desired_object)
print("Number of visits:", node_count)
print("Number of generated combinations:", len(combinations))
print("Combinations:", combinations)