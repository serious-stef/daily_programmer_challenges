""" Letter Value Sum - A Coding-Challenge from reddit.com/dailyprogrammer
https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/
Challenge Level: Easy
Description: Assign every lowercase letter a value, from "1" for "a" to "26" for "z".
Given a string of lowercase letters, find the sum of the values of the letters in the string."""
import string

letters = [str(s) for s in str(string.ascii_lowercase)]  # List of all lowercase letters from a-z
values = [int(v) for v in range(1, 27)]  # List of values from 1-26


def lettervalue(character):
    i = 0

    for letters[i] in letters:
        if character == letters[i]:
            return values[i]
        i += 1


def lettersum(word):
    lsum = 0

    for w in word:
        lsum = lsum + lettervalue(w)

    print(lsum)
