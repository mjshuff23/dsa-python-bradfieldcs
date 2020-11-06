# Balanced parentheses means that each opening symbol has a corresponding closing symbol
# and the pairs of parentheses are properly nested.

# Read a string of parenthesis from left to right, to see if they are balanced
#  - While processing symbols, the most recent opening ( must match the next closing )
#  - First opening symbol processed may have to wait until the last for it's match
#  - Closing symbols match from the inside out
# Pseudocode
#  1. Starting with an empty stack, process the parenthesis from left to right
#  2. If a symbol is a '(', push it on the stack as a signal we need a ')' later
#  3. If a symbol is a ')', pop the stack
#  4. As long as it's possible to pop the stack to match every ')', we have balance
#    4a. If at any time there's no '(' to match a ')', we are not balanced
#    4b. At the end of the string, when all symbols have been processed, stack should be empty

OPENING = '('

def is_balanced(parenthesis):
    """
    Returns a boolean result as to whether a string of parenthesis is balanced
    Press 'Q' to exit...
    """

    stack = []
    for paren in parenthesis:
        if paren == OPENING:
            stack.append(paren)
        elif paren != ')':
            continue
            # return 'Error: Contains characters besides parenthesis'
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return not len(stack)


print_help = input("Do you know what this function does? (Yes/No)").lower()
if print_help.startswith('y'):
    help(is_balanced)

parenthesis = input('Enter parenthesis string to check for balance: ')
while (not parenthesis
       or not '(' in parenthesis
       and not ')' in parenthesis):
    parenthesis = input(f'Please enter a set of parenthesis: ')

# print('Parenthesis Balance Tester')
# print('-'*25, 'demo', '-'*25)
# print('(()):', is_balanced('(())'))
# print('((())):', is_balanced('((()))'))
# print('((()):', is_balanced('((())'))
# print('-'*23, 'end demo', '-'*23)
print(f'{parenthesis}: {is_balanced(parenthesis)}')
