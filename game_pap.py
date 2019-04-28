class Player:

    def __init__(self,name):
        self.name = name
        self.move = None

    def make_move(self):
        choice = input('Make move pls')
        self.move = choice


class Board:

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def play(self):

        p1.make_move()
        p2.make_move()


        if p1.move == p2.move:
            result = 'draw'

        elif (p1.move == 'pap' and p2.move =='kam') or \
             (p1.move == 'kam' and p2.move =='noz'):
            result ='player 1 wins'
        else:
            result = 'player 2 wins'

        return result
