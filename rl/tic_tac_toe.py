"""Reinforced learning algorithm to play Tic Tac Toe."""
import re


def ternary(n):
    """Convert number representation to string representation in base 3."""
    if n == 0:
        return '000000000'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums)).zfill(9)


def list_all_states():
    """Create a list of all possible tic tac toe board states.

    Some are invalid board states.
    """
    states = []
    for i in range(3**9):
        states.append(ternary(i))
    return states

# states = listAllStates()
# print(len(states))
# print(states[0])
# print(states[1])
# print(states[5])
# print(states[19400])
# print(states[19682])


def is_full(s):
    """Regex checks if all positions are either 1 or 2."""
    pattern = re.compile(r"^[1|2]{9}$")
    if pattern.match(s):
        return True
    else:
        return False


def is_p1_win(s):
    """Check if player 1 has won."""
    p1 = re.compile(r"^1.{2}1.{2}1.{2}$")  # 1's in 1st column
    p2 = re.compile(r"^.1.{2}1.{2}1.$")  # 1's in 2nd column
    p3 = re.compile(r"^.{2}1.{2}1.{2}1$")  # 1's in 3rd column
    p4 = re.compile(r"^1{3}.{6}$")  # 1's in 1st row
    p5 = re.compile(r"^.{3}1{3}.{3}$")  # 1's in 2nd row
    p6 = re.compile(r"^.{6}1{3}$")  # 1's in 3rd row
    p7 = re.compile(r"^1.{3}1.{3}1$")  # 1's in diagonal l->r
    p8 = re.compile(r"^.{2}1.1.1.{2}$")  # 1's in diagonal r->l

    patterns = [p1, p2, p3, p4, p5, p6, p7, p8]
    for p in patterns:
        if p.match(s):
            return True
    else:
        return False


def is_p2_win(s):
    """Check if player 2 has won."""
    p1 = re.compile(r"^2.{2}2.{2}2.{2}$")  # 2's in 1st column
    p2 = re.compile(r"^.2.{2}2.{2}2.$")  # 2's in 2nd column
    p3 = re.compile(r"^.{2}2.{2}2.{2}2$")  # 2's in 3rd column
    p4 = re.compile(r"^2{3}.{6}$")  # 2's in 1st row
    p5 = re.compile(r"^.{3}2{3}.{3}$")  # 2's in 2nd row
    p6 = re.compile(r"^.{6}2{3}$")  # 2's in 3rd row
    p7 = re.compile(r"^2.{3}2.{3}2$")  # 2's in diagonal l->r
    p8 = re.compile(r"^.{2}2.2.2.{2}$")  # 2's in diagonal r->l

    patterns = [p1, p2, p3, p4, p5, p6, p7, p8]
    for p in patterns:
        if p.match(s):
            return True
    else:
        return False



# class Player:
#     """Agent to play tic tac toe."""
#
#     def __init__(self):
#         """Initialise agent."""
#         pass
#
#     def take_action(self, env):
#         """Make a valid move on env."""
#         pass
#
#     def update_state_history(self, state):
#         """Update internal state history."""
#         pass
#
#     def update(self, env):
#         """Update value function."""
#         pass
#
#
# class Environment:
#     """Tic tac toe environment for agents to play in."""
#
#     def __init__(self):
#         """Initialise environment."""
#         pass
#
#     def draw_board(self):
#         """Draw current board state."""
#         pass
#
#     def get_state(self):
#         """Return current board state."""
#         pass
#
#     def take_action(self, action):
#         """Allow agent to take an action."""
#         pass
#
#
# def play_game(p1, p2, env, draw=False):
#     # loops until the game is over
#     current_player = None
#     while not env.game_over():
#         # alternate between players
#         # p1 always starts first
#         if current_player == p1:
#             current_player = p2
#         else:
#             current_player = p1
#
#         # draw the board
#         if draw:
#             if draw == 1 and current_player == p1:
#                 env.draw_board()
#             if draw == 2 and current_player == p1:
#                 env.draw_board()
#
#         # current_player makes a move
#         current_player.take_action(env)
#
#         # update state histories
#         state = env.get_state()
#         p1.update_state_history(state)
#         p2.update_state_history(state)
#
#     if draw:
#         env.draw_board()
#
#     # do the value function update
#     p1.update(env)
#     p2.update(env)
