def count_extended_words_set(word_list):
    # 1. Store all words in a set for O(1) average-time lookups.
    word_set = set(word_list)
    count = 0

    # 2. Iterate through each word in the original list
    for word in word_list:
        for i in range(1, len(word)):
            prefix = word[:i] # prefix is the slice from the start up to index i-1
            if prefix in word_set:
                count += 1
                break

    return count

# Example usage:
my_list = ["well", "welling", "wellbeing", "apple", "app"]
result = count_extended_words_set(my_list)
print(f"The result is: {result}")