# Uses python3


def edit_distance(s, t):

    len_s = len(s)
    len_t = len(t)

    d = [[x for x in range(len_t + 1)] for y in range(len_s + 1)]
    for y in range(len_s + 1):
        d[y][0] = y

    s = ["t"] + s
    t = ["t"] + t

    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            insertion = d[i][j - 1] + 1
            deletion = d[i - 1][j] + 1
            match = d[i - 1][j - 1]
            mismatch = d[i - 1][j - 1] + 1
            if s[i] == t[j]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)

    return d[len_s][len_t]


if __name__ == "__main__":
   print(edit_distance(list(input()), list(input())))
