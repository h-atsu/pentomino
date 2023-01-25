import numpy as np
import itertools
import math
from tqdm import tqdm

NUM_PIECE = 12
X_WIDTH = 6
Y_WIDTH = 10


class Mino:
    def __init__(self, arr):
        self.arrs = self.generate_arrs(arr)

    def rotate_arr(self, arr):
        ret = []
        h, w = len(arr), len(arr[0])
        for i in range(w):
            ret.append([arr[h - j - 1][i] for j in range(h)])
        return ret

    def reverse_arr(self, arr):
        return [v[::-1] for v in arr]

    def generate_arrs(self, arr):
        arrs = [arr]
        for i in range(3):
            if self.rotate_arr(arrs[-1]) not in arrs:
                arrs.append(self.rotate_arr(arrs[-1]))

        if self.reverse_arr(arr) not in arrs:
            arrs.append(self.reverse_arr(arr))
            for i in range(3):
                if self.rotate_arr(arrs[-1]) not in arrs:
                    arrs.append(self.rotate_arr(arrs[-1]))

        return arrs


def base_pos(arr):
    for i, vs in enumerate(arr):
        for j, v in enumerate(vs):
            if v == '#':
                return (i, j)


minos = [[] for _ in range(NUM_PIECE)]

minos[0] = Mino(
    [['#', '.'],
     ['#', '.'],
     ['#', '#'],
     ['#', '.']]
)

minos[1] = Mino(
    [['#', '#'],
     ['#', '#'],
     ['.', '#']]
)


minos[2] = Mino(
    [['#', '#', '#'],
     ['#', '.', '#']]
)

minos[3] = Mino(
    [['.', '#', '.'],
     ['#', '#', '#'],
     ['.', '#', '.']]
)

minos[4] = Mino(
    [['.', '#', '.'],
     ['#', '#', '#'],
     ['#', '.', '.']]
)

minos[5] = Mino(
    [['#', '#', '.'],
     ['.', '#', '#'],
     ['.', '.', '#']]
)

minos[6] = Mino(
    [['#'],
     ['#'],
     ['#'],
     ['#'],
     ['#']]

)


minos[7] = Mino(
    [['#', '#', '#'],
     ['.', '#', '.'],
     ['.', '#', '.']]
)


minos[8] = Mino(
    [['#', '.'],
     ['#', '.'],
     ['#', '.'],
     ['#', '#']]
)

minos[9] = Mino(
    [['#', '.'],
     ['#', '.'],
     ['#', '#'],
     ['.', '#']]
)

minos[10] = Mino(
    [['#', '#', '.'],
     ['.', '#', '.'],
     ['.', '#', '#']]
)

minos[11] = Mino(
    [['#', '.', '.'],
     ['#', '.', '.'],
     ['#', '#', '#']]
)


# for i, mino in enumerate(minos):
#     print(f"======== {i} th mino ========")
#     for arr in mino.arrs:
#         print('-----')
#         for c in arr:
#             print(c)


ans = []


def dfs(idx, used, seen):
    if idx == X_WIDTH * Y_WIDTH:
        ans.append(seen)
        return
    x, y = idx % X_WIDTH, idx // X_WIDTH
    if seen[y][x] == -1:
        for k in range(NUM_PIECE):
            # 置くミノの選択
            if used[k] == False:
                used[k] = True
                for arr in minos[k].arrs:
                    h, w = len(arr), len(arr[0])
                    base_y, base_x = base_pos(arr)
                    for i in range(h):
                        for j in range(w):
                            if arr[i][j] == '#':
                                dx, dy = j - base_x, i - base_y
                                nx, ny = x + dx, y + dy
                                if ny < 0 or ny >= Y_WIDTH or nx < 0 or nx >= X_WIDTH:
                                    return
                                if seen[ny][nx] != -1:
                                    return

                                seen[ny][nx] = k

                    # ith　のミノをおける
                    dfs(idx + 1, used, seen)
                used[k] = False
    else:
        # 置くべきマスを進める
        dfs(idx + 1, used, seen)


bar = tqdm(total=math.factorial(NUM_PIECE))
used = [False for _ in range(NUM_PIECE)]

seen = [[-1 for _ in range(X_WIDTH)] for i in range(Y_WIDTH)]
dfs(0, used, seen)

# for perm in tqdm(itertools.permutations(mino)):
#     idx = 0
#     seen = [[False for _ in range(X_WIDTH)] for i in range(Y_WIDTH)]
#     is_valid = True
#     for y, x in itertools.product(range(Y_WIDTH), range(X_WIDTH)):
#         if seen[y][x] == False:
#             seen[y][x] = True
#             for dy, dx in perm[idx]:
#                 ny = y + dy
#                 nx = x + dx
#                 if ny < 0 or ny >= Y_WIDTH or nx < 0 or nx >= X_WIDTH:
#                     is_valid = False
#                     break
#                 if seen[ny][nx] == True:
#                     is_valid = False
#                     break
#                 seen[ny][nx] = True
#             idx += 1
#         else:
#             continue

#         if is_valid == False:
#             break

#     if is_valid:
#         print('found')
#         print(perm)
