"""
This program was written by Joel Muyskens for CS344 lab01

This program demonstrates that the GPS algoritm cannot solve some problems

When the program sees the goal 'have money' and the initial state 'have money' the algorithm sees that
goals as already satisfied, however, through the course of the program it spends money to fix the car
which means that the program doesn't end with all of the goal states reached. I also added a way to
get more money from home if the son is home but because it thinks this is already satisfied, it doesn't
use this action.

This demonstrates a problem GPS can't solve and I can.

(solution: get car fixed, get money from home, bring son to school)
"""


from gps import gps
import logging




problem = {

    'initial': ['son at home', 'have money', 'car broken'],
    'goal': ['have money', 'son at school'],


    'actions': [
        {
            'action': 'bring son to school',
            'preconds': [
                'son at home',
                'car works'
            ],
            'add': [
                'son at school'
            ],
            'delete': [
                'son at home'
            ]
        },
        {
            'action': 'get car fixed',
            'preconds': [
                'have money',
                'car broken'
            ],
            'add': [
                'car works'
            ],
            'delete': [
                'car broken'
            ]
        },
        {
            'action': 'get money from home',
            'preconds': [
                'son at home'
            ],
            'add': [
                'have money'
            ],
            'delete': [

            ]
        }
    ]
}


if __name__ == '__main__':

    # This turns on detailed logging for the GPS "thought" process.
    logging.basicConfig(level=logging.DEBUG)

    #Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')
