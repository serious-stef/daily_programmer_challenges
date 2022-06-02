""" Letter Value Sum - A Coding-Challenge from reddit.com/dailyprogrammer
https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/
Challenge Level: Easy
Description: Assign every lowercase letter a value, from "1" for "a" to "26" for "z".
Given a string of lowercase letters, find the sum of the values of the letters in the string."""


# This function defines a value for each character in a word.
def lettervalue(character):
    return ord(character) - ord("a") + 1


# This is the main function, which sums up the whole word.
def lettersum(word):
    lsum = 0

    for w in word:
        lsum = lsum + lettervalue(w)

    print(lsum)
