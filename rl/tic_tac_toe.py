"""Reinforced learning algorithm to play Tic Tac Toe."""
import re


class Player:
    """Agent to play tic tac toe."""

    def __init__(self, number, epsilon, env):
        """Initialise agent.

        number - String '1' or '2' representing symbol player will use,
        epsilon - learning rate
        env - Environment object
        """
        self.number = number
        self.epsilon = epsilon
        self.stateHistory = []
        self.valueFunction = self._initialise_value(env)

    def _initialise_value(self, env):
        value = dict()
        states = env.list_all_states()
        for state in states():
            if env.is_win(self.number, state):
                value[state] = 1
            elif env.is_loss(self.number, state) or env.is_draw(state):
                value[state] = 0
            else:
                value[state] = 0.5
        return value

    def take_action(self, env):
        """Make a valid move on env."""
        pass

    def update_state_history(self, state):
        """Update internal state history."""
        self.stateHistory.append(state)

    def update(self, env):
        """Update value function."""
        pass


class Environment:
    """Tic tac toe environment for agents to play in."""

    def __init__(self):
        """Initialise environment."""
        self.state = '000000000'

    def draw_board(self):
        """Draw current board state."""
        print('----------')
        print(self.state)
        print('----------')

    def accept_action(self, player, action):
        """Allow agent to take an action."""
        playerNumber = player.number
        if self.state[action] == '0':
            self.state[action] = playerNumber
        else:
            raise RuntimeError('Player attemted to play invalid action.')

    def _ternary(self, n):
        """Convert number representation to string representation in base 3."""
        if n == 0:
            return '000000000'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums)).zfill(9)

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
        pattern = re.compile(r"^[1|2]{9}$")
        if pattern.match(state):
            return True
        else:
            return False

    def is_win(self, playerNumber, state):
        """Check if player has won."""
        if playerNumber == '1':
            p1 = re.compile(r"^1.{2}1.{2}1.{2}$")  # 1's in 1st column
            p2 = re.compile(r"^.1.{2}1.{2}1.$")  # 1's in 2nd column
            p3 = re.compile(r"^.{2}1.{2}1.{2}1$")  # 1's in 3rd column
            p4 = re.compile(r"^1{3}.{6}$")  # 1's in 1st row
            p5 = re.compile(r"^.{3}1{3}.{3}$")  # 1's in 2nd row
            p6 = re.compile(r"^.{6}1{3}$")  # 1's in 3rd row
            p7 = re.compile(r"^1.{3}1.{3}1$")  # 1's in diagonal l->r
            p8 = re.compile(r"^.{2}1.1.1.{2}$")  # 1's in diagonal r->l

        elif playerNumber == '2':
            p1 = re.compile(r"^2.{2}2.{2}2.{2}$")  # 2's in 1st column
            p2 = re.compile(r"^.2.{2}2.{2}2.$")  # 2's in 2nd column
            p3 = re.compile(r"^.{2}2.{2}2.{2}2$")  # 2's in 3rd column
            p4 = re.compile(r"^2{3}.{6}$")  # 2's in 1st row
            p5 = re.compile(r"^.{3}2{3}.{3}$")  # 2's in 2nd row
            p6 = re.compile(r"^.{6}2{3}$")  # 2's in 3rd row
            p7 = re.compile(r"^2.{3}2.{3}2$")  # 2's in diagonal l->r
            p8 = re.compile(r"^.{2}2.2.2.{2}$")  # 2's in diagonal r->l
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
        if playerNumber == '1':
            return self.is_win('2', state)
        elif playerNumber == '2':
            return self.is_win('1', state)
        else:
            raise RuntimeError('Invalid playerNumber', state)

    def is_draw(self, state):
        """Check if game is drawn for specified state."""
        if not (self.is_win('1', state) or self.is_win('2', state)) and self._is_full(state):
            return True
        else:
            return False

    def game_over(self):
        """Check if game is over."""
        if self.is_win('1', self.state) or self.is_win('2', self.state) or self._is_full(self.state):
            return True
        else:
            return False


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
            if draw == 1 and current_player == p1:
                env.draw_board()
            if draw == 2 and current_player == p1:
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
