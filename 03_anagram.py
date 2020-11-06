# One string is an anagram of another if the second is a rearrangement of the letters in the first.
# heart/earth, role/lore, etc..
#   1.  Must be same length
#   2.  Letters in second word must be rearrangement of 1st

# def anagram_checking_off(s1, s2):
#     # Make sure words are same length
#     if len(s1) != len(s2):
#         return False
#     # Turn second word into a list to iterate through
#     to_check_off = list(s2)
#     # Loop through the first word
#     for char in s1:
#         # i is an index added to each loop thanks to enumerate
#         for i, other_char in enumerate(to_check_off):
#             if char == other_char:
#                 to_check_off[i] = None
#                 break
#         # else clause executes after the for loop completes normally. This means that the loop did not
#         # encounter a break statement.
#         else:
#             return False

#     return True


# # print(anagram_checking_off('abcd', 'dcba'))
# print(anagram_checking_off('abcd', 'dcbc'))

# 2. Sort and Compare
#     - use sorted to sort both and compare

from itertools import zip_longest

def anagram_sort_and_compare2(s1, s2):
    for a, b in zip_longest(sorted(s1), sorted(s2)):
        if a != b:
            return False
    return True

def anagram_sort_and_compare(str1, str2):
    for a, b in zip_longest(sorted(str1), sorted(str2)):
        if a != b:
            return False
    return True


print(anagram_sort_and_compare('abcde', 'edcba'))  # => True
print(anagram_sort_and_compare('abcde', 'abcd'))   # => False
