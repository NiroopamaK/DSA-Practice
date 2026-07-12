# Substring with Concatenation of All Words
# -------------------------------------------------------------

# Problem:
# Given a string s and a list of words (all same length),
# return all starting indices of substring(s) in s that is
# a concatenation of each word exactly once (in any order).
#
# -------------------------------------------------------------
# Example:
# s = "barfoothefoobarman"
# words = ["foo", "bar"]
#
# Output: [0, 9]
#
# Explanation:
# "barfoo" starts at index 0
# "foobar" starts at index 9
#
# -------------------------------------------------------------
# Key Concepts:
#
# 1. All words have SAME length → allows fixed-size window jumps
# 2. Use sliding window with step size = word_len
# 3. Use hashmap (Counter) to track required word frequencies
#
# -------------------------------------------------------------
# Approach:
#
# - Let word_len = length of each word
# - total_len = total length of all concatenated words
#
# - Loop through all possible starting offsets:
#     (important for alignment)
#
# - Use sliding window:
#     - Expand right pointer word-by-word
#     - Track counts in current_map
#
# - If a word exceeds allowed frequency:
#     shrink from left
#
# - If all words matched:
#     record index
#
# -------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(k)  (k = number of words)
# -------------------------------------------------------------


from collections import Counter


def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    total_words = len(words)
    total_len = word_len * total_words

    # Frequency map of words we need
    word_map = Counter(words)

    result = []

    # Try all alignments (important!)
    for i in range(word_len):
        left = i
        count = 0
        current_map = Counter()

        # Move right pointer in steps of word length
        for right in range(i, len(s) - word_len + 1, word_len):
            word = s[right:right + word_len]

            # Valid word
            if word in word_map:
                current_map[word] += 1
                count += 1

                # If word frequency exceeds allowed → shrink window
                while current_map[word] > word_map[word]:
                    left_word = s[left:left + word_len]
                    current_map[left_word] -= 1
                    left += word_len
                    count -= 1

                # All words matched
                if count == total_words:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    current_map[left_word] -= 1
                    left += word_len
                    count -= 1

            else:
                # Reset window if invalid word
                current_map.clear()
                count = 0
                left = right + word_len

    return result
