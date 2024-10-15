# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu
# Spire IDs : 34569497
import string, random

def get_guess():
    s = input('What word is this?: ')
    return s.upper()
# print(get_guess())
def print_word(word):
    print(' '.join(word))
    return
# print_word('HELLO')
def exact_match_compare(fword, sword):
    empty = ''
    for i in range(len(fword)):
        if fword[i] == sword[i]:
            empty += '🟢'
        else:
            empty += '🔴'
    return empty
# print(exact_match_compare('Hello', 'H'))
def one_turn(solution):
   s = get_guess()
   print_word(s)
   print(exact_match_compare(solution.upper(), s))
   if solution == s:
       print('Congratulations!')
       exit()
       return
# one_turn('Hello')
def make_solution():
    possibility = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
    word = random.choice(possibility)
    return word
# print(make_solution())

soln = make_solution()
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
print(f"Word was \"{soln}\", better luck next time.")