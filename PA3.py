import time
import argparse

def count_construct(target, wordbank):
    ways = [0] * (len(target) + 1)
    ways[0] = 1

    for i in range(len(target) + 1):
        if ways[i] > 0:
            for word in wordbank:
                if i + len(word) <= len(target) and target[i:i+len(word)] == word:
                    ways[i + len(word)] += ways[i]

    return ways[len(target)]

def all_construct(target, wordbank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        if table[i]:
            for word in wordbank:
                if i + len(word) <= len(target) and target[i:i+len(word)] == word:
                    new_combinations = [combination + [word] for combination in table[i]]
                    table[i+len(word)].extend(new_combinations)

    return table[len(target)]

def main():
    parser = argparse.ArgumentParser(description='Program to construct target string from wordbank')
    parser.add_argument('--target', type=str, help='Target string to be constructed', required=True)
    parser.add_argument('--wordbank', nargs='+', type=str, help='List of strings in the wordbank', required=True)
    args = parser.parse_args()

    start_time = time.time()

    target = args.target
    wordbank = args.wordbank

    if not target:
        print("Number of ways: 1")
        print("[ [] ]")
    elif not wordbank:
        print("Number of ways: 0")
        print("[]")
    else:
        num_ways = count_construct(target, wordbank)
        all_ways = all_construct(target, wordbank)
        print(f"Number of ways: {num_ways}")
        print("[")
        for way in all_ways:
            print(f"  {way}")
        print("]")
    
    print(f"Runtime: {time.time() - start_time:.6f} seconds")

if __name__ == "__main__":
    main()


# Define a function all_construct(target, wordbank) that takes a target string and a word bank as input and returns a list of all possible constructions of the target string from elements of the word bank.

# Decisions:
# For each index i in the target string, decide whether to use each word from the word bank at that index.
# At each index, check if a word from the word bank can be appended to the current substring to form the target string.

# Recursions:
# Count Construction (count_construct):

# Base case: When the index i reaches the length of the target string, return 1 (indicating one valid construction).
# Recursive case:
# Iterate through each word in the word bank.
# If the current substring + word matches a prefix of the target string, call the function recursively with the updated index.
# List All Constructions (all_construct):

# Base case: When the index i reaches the length of the target string, return a list containing an empty list (indicating one valid construction).
# Recursive case:
# Iterate through each word in the word bank.
# If the current substring + word matches a prefix of the target string, call the function recursively with the updated index and append the current word to all the constructions obtained from the recursive call.

