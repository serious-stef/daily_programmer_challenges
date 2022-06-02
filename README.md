# daily_programmer_challenges
A repository for reddit/dailyprogrammer coding challenges 

## Disclaimer

All challenges have been done by me. I am using the challenges to learn coding, so they might not be very efficient or aesthetically pleasing. I just started out programming, so before challenge 1 I had no experience whatsoever. 
I am always open for suggestions, so please contact me for any ideas on how to improve.

## Currently completed challenges:

### Challenge 239
[Link to reddit post](https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/)

This gave me a hard time figuring out how to change the value of the array within the "game"-function. I thought it is enough to assign p = digitsum(p), but it didn't change the value within the array, hence why I added an iteration using "i". I still have to find out why this is necessary.

Anyway, I am very proud to having done this within 24 hours of learning python :). On to the next one!

#### Lessons learned
* `len(a)` is the length of an array
* `[int(n) for n in str(number)]` creates a list of integers from a string of numbers. Attention: It has to be numbers. First value can also be a different datatype though, so it is also possible to make an array of characters or one digit strings.
* Learned how to use github (hi everyone!) and how to push, commit and pull.
* Got a good sense of how to use for and while loops.

### Challenge 399
[Link to reddit post](https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/)

This was harder to solve than I expected. The only problem here was to convert the letters of the alphabet to values. First I tried to solve it by determining the value of a complete word. That didn't really work though. In the process however I realised it might be easier to just determine the value of one character at a time. Also I did a redundant approach to connecting values and letters through an additional variable "lettervalues" which I later found obsolete.
It's not a beauty, but it solves the problem, and I am proud of my solution.

After revisiting the solution again I tried solving it "the python way".
So I tried to get rid of an incrementable variable. Having no success I asked for help and learned about the ``ord()`` function.
This function uses the fact, that every ascii character has a value, which it returns.

#### Lessons learned
* Every challenge is now in a different .py to stay organised. Had to learn how to import functions from other files.
* string is a class which lets you import a list of the alphabet through `string.ascii_lowercase`.
* Learned about the ``ord()`` function.
* Learned about ascii-values: https://ascii.cl/

#### Bonus Challenges

So this