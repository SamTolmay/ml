"""Reinforced learning algorithm to play Tic Tac Toe."""
import re
import math
import random


class Player:
    """Agent to play tic tac toe."""

    def __init__(self, symbol, epsilon, alpha, env):
        """Initialise agent.

        symbol - String 'X' or 'O' representing symbol player will use,
        epsilon - learning rate for epsilon greedy
        alpha - learning rate when updating value function
        env - Environment object
        """
        self.symbol = symbol
        self.epsilon = epsilon
        self.alpha = alpha
        self.stateHistory = []
        self.valueFunction = self._initialise_value(env)
        self.t = 1

    def _initialise_value(self, env):
        value = dict()
        states = env.list_all_states()
        for state in states:
            if env.is_win(self.symbol, state):
                value[state] = 1
            elif env.is_loss(self.symbol, state):
                value[state] = -1
            elif env.is_draw(state):
                value[state] = 0
            else:
                value[state] = 0.5
        return value

    def take_action(self, env):
        """Make a valid move on env."""
        possible_actions = []
        for i, char in enumerate(env.state):
            if char == '-':
                state = env.state[:i] + self.symbol + env.state[(i + 1):]
                possible_actions.append({'a': i, 'v': self.valueFunction[state]})

        if random.random() < self.epsilon/(math.log(self.t) + 1):
            chosen_action = random.choice([i['a'] for i in possible_actions])
        else:
            maxA = [possible_actions[0]['a']]
            maxV = possible_actions[0]['v']
            for i, A in enumerate(possible_actions):
                if i > 0:
                    if A['v'] > maxV:
                        maxV = A['v']
                        maxA = [A['a']]
                    elif A['v'] == maxV:
                        maxA.append(A['a'])
            chosen_action = random.choice(maxA)

        env.accept_action(self, chosen_action)

    def update_state_history(self, state):
        """Update internal state history."""
        self.stateHistory.append(state)

    def update(self, env):
        """Update value function."""
        rev = list(reversed(self.stateHistory))
        next_state = rev[0]
        states = rev[1:]
        for state in states:
            self.valueFunction[state] = self.valueFunction[state] + self.alpha*(self.valueFunction[next_state]-self.valueFunction[state])
            next_state = state
        self.stateHistory = []
        self.t += 1


class Human:
    """Class to allow user to play."""

    def __init__(self, symbol, name):
        """Initialise agent.

        symbol - String 'X' or 'O' representing symbol player will use,
        """
        self.symbol = symbol
        self.name = name
        welcome = """Welcome human player.
you are playing with symbol {}
You will be prompted to make a move when it is your turn.
You should enter a number from 1 to 9, to indicate which position
you would like to place your symbol. The positions are numbered from
left to right, top to bottom:
123
456
789
""".format(symbol)
        print(welcome)

    def take_action(self, env):
        """Promt user for a move."""
        print('Current board state')
        env.draw_board()
        print('{}, Please select a position to make a move:'.format(self.name))
        action = self._prompt_action(env)
        env.accept_action(self, action)

    def _prompt_action(self, env):
        try:
            action = int(input()) - 1
        except Exception:
            print('That was not a valid move. Please try again.')
            action = self._prompt_action(env)
        if action not in range(0, 9) or env.state[action] is not '-':
                print('That was not a valid move. Please try again.')
                action = self._prompt_action(env)
        return action

    def update_state_history(self, state):
        """Update internal state history."""
        pass

    def update(self, env):
        """Update value function."""
        if env.is_win(self.symbol, env.state):
            print('You have won')
        elif env.is_loss(self.symbol, env.state):
            print('You have lost')
        elif env.is_draw(env.state):
            print('The game ended in a draw')
        print('The final board state was:')
        env.draw_board()


class Environment:
    """Tic tac toe environment for agents to play in."""

    def __init__(self):
        """Initialise environment."""
        self.state = '---------'

    def draw_board(self):
        """Draw current board state."""
        print(self.state[:3])
        print(self.state[3:6])
        print(self.state[6:])
        print('***')

    def accept_action(self, player, action):
        """Allow agent to take an action."""
        if self.state[action] == '-':
            self.state = self.state[:action] + player.symbol + self.state[(action + 1):]
        else:
            raise RuntimeError('Player attemted to play invalid action.')

    def _ternary(self, n):
        """Convert number representation to string representation in base 3."""
        if n == 0:
            return '---------'
        symMap = {0: '-',
                  1: 'X',
                  2: 'O'}
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(symMap[r])
        return ''.join(reversed(nums)).rjust(9, '-')

    def list_all_states(self):
        """Create a list of all possible tic tac toe board states.

        Some are invalid board states.
        """
        states = []
        for i in range(3**9):
            states.append(self._ternary(i))
        return states

    def _is_full(self, state):
        """Regex checks if all positions are either 1 or 2."""
        pattern = re.compile(r"^[X|O]{9}$")
        if pattern.match(state):
            return True
        else:
            return False

    def is_win(self, playerSymbol, state):
        """Check if player has won."""
        if playerSymbol == 'X':
            p1 = re.compile(r"^X.{2}X.{2}X.{2}$")  # X's in 1st column
            p2 = re.compile(r"^.X.{2}X.{2}X.$")  # X's in 2nd column
            p3 = re.compile(r"^.{2}X.{2}X.{2}X$")  # X's in 3rd column
            p4 = re.compile(r"^X{3}.{6}$")  # X's in 1st row
            p5 = re.compile(r"^.{3}X{3}.{3}$")  # X's in 2nd row
            p6 = re.compile(r"^.{6}X{3}$")  # X's in 3rd row
            p7 = re.compile(r"^X.{3}X.{3}X$")  # X's in diagonal l->r
            p8 = re.compile(r"^.{2}X.X.X.{2}$")  # X's in diagonal r->l

        elif playerSymbol == 'O':
            p1 = re.compile(r"^O.{2}O.{2}O.{2}$")  # O's in 1st column
            p2 = re.compile(r"^.O.{2}O.{2}O.$")  # O's in 2nd column
            p3 = re.compile(r"^.{2}O.{2}O.{2}O$")  # O's in 3rd column
            p4 = re.compile(r"^O{3}.{6}$")  # O's in 1st row
            p5 = re.compile(r"^.{3}O{3}.{3}$")  # O's in 2nd row
            p6 = re.compile(r"^.{6}O{3}$")  # O's in 3rd row
            p7 = re.compile(r"^O.{3}O.{3}O$")  # O's in diagonal l->r
            p8 = re.compile(r"^.{2}O.O.O.{2}$")  # O's in diagonal r->l
        else:
            raise RuntimeError('Invalid playerNumber')

        patterns = [p1, p2, p3, p4, p5, p6, p7, p8]
        for p in patterns:
            if p.match(state):
                return True
        else:
            return False

    def is_loss(self, playerNumber, state):
        """Check if game is lost for player at specified state."""
        if playerNumber == 'X':
            return self.is_win('O', state)
        elif playerNumber == 'O':
            return self.is_win('X', state)
        else:
            raise RuntimeError('Invalid playerNumber', state)

    def is_draw(self, state):
        """Check if game is drawn for specified state."""
        if not (self.is_win('X', state) or self.is_win('O', state)) and self._is_full(state):
            return True
        else:
            return False

    def game_over(self):
        """Check if game is over."""
        if self.is_win('X', self.state) or self.is_win('O', self.state) or self._is_full(self.state):
            return True
        else:
            return False

    def clear(self):
        """Reset game state."""
        self.state = '---------'


def play_game(p1, p2, env, draw=False):
    """Play game for 1 episode."""
    # loops until the game is over
    current_player = None
    while not env.game_over():
        # alternate between players
        # p1 always starts first
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1

        # draw the board
        if draw:
                env.draw_board()

        # current_player makes a move
        current_player.take_action(env)

        # update state histories
        p1.update_state_history(env.state)
        p2.update_state_history(env.state)

    if draw:
        env.draw_board()

    # do the value function update
    p1.update(env)
    p2.update(env)
    env.clear()


env = Environment()
p1 = Player('X', 1, 0.1, env)
p2 = Player('O', 1, 0.1, env)
human = Human('O', 'Sam')


print('Training AI')
for i in range(5000):
    if (i % 2) == 0:
        play_game(p1, p2, env)
    else:
        play_game(p2, p1, env)

print('Human turn 1')
play_game(p1, human, env)
print('Human turn 2')
play_game(human, p1, env)
print('Human turn 3')
play_game(p1, human, env)
