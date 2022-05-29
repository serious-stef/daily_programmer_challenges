""" Game of Threes - A Coding-Challenge from reddit.com/dailyprogrammer
https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/
Challenge Level: Easy
Description: Give the program a value. Let it divide that value by "3" until it gets to "1".
If a number is not divisible by three, let the program add or substract "1" to make it divisible by three.
Print out every step the program does during runtime.
For the whole explanation follow the link at the top of this file."""


divthree = [3, 6, 9]  # Array for checking the digit sum on divisibility by three.


# Function for calculating the digit sum.
def digitsum(number):
    q = [int(n) for n in str(number)]  # Array for saving all digits.
    digitsumresult = 0
    i = 1

    while i <= len(q):  # Starting at "0" add every digit to the digit sum.
        digitsumresult = digitsumresult + q[i - 1]
        i += 1
    return digitsumresult  # Return the result for further usage.


# Main function. This is where python plays the "Game of Threes"
def game(gamenumber):
    while gamenumber > 1:
        checker = [digitsum(gamenumber), digitsum(gamenumber + 1), digitsum(gamenumber - 1)]
        i = 0
        for p in checker:
            while p >= 10:
                p = digitsum(p)  # Why doesn't this change the value of checker[0]/checker[1]/...?
            checker[i] = p
            i += 1

            if checker[0] in divthree:
                print(str(gamenumber) + " 0")
                gamenumber = int(gamenumber / 3)
                break
            elif checker[1] in divthree:
                print(str(gamenumber) + " 1")
                gamenumber = int((gamenumber + 1) / 3)
                break
            elif checker[2] in divthree:
                print(str(gamenumber) + " -1")
                gamenumber = int((gamenumber - 1) / 3)
                break
    print(gamenumber)
