"""
Given two strings, create a function that returns the total number of unique characters from the combined string.

Examples:
    count_unique_chars("apple", "play") ➞ 5
    "appleplay" has 5 unique characters:  "a", "e", "l", "p", "y"

    count_unique_chars("sore", "zebra") ➞ 7

    count_unique_chars("a", "soup") ➞ 5

Notes:
 - Careful with empty strings
 - All characters will be lowercase.

"""

def count_unique_chars(string_1, string_2):
    s3 = string_1 + string_2
    new_string=[]
    for i in s3[::]:
        if i not in new_string:
            new_string.append(i)
    return (len(new_string))