class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.endWord = True

    def hasPrefix(self, word):
        # print(word)
        curr = self.root
        for char in word:
            # print(char)
            if curr.endWord:
                return True
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        # print(curr)
        # print(' ')
        return False

def count_extended_words_set(word_list):
    # Trie Tree Solution
    trie = TrieTree()
    for word in word_list:
        trie.insert(word)

    cnt = 0
    for word in word_list:
        if trie.hasPrefix(word):
            cnt += 1
    return cnt

    # Brute Force Better Solution
    # # 1. Store all words in a set for O(1) average-time lookups.
    # word_set = set(word_list)
    # count = 0

    # # 2. Iterate through each word in the original list
    # for word in word_list:
    #     for i in range(1, len(word)):
    #         prefix = word[:i] # prefix is the slice from the start up to index i-1
    #         print(word)
    #         print(prefix)
    #         print(i)
    #         if prefix in word_set:
    #             count += 1
    #             break

    # return count

# Example usage:
my_list = ["well", "welling", "wellbeing", "apple", "app"]
result = count_extended_words_set(my_list)
print(f"The result is: {result}")