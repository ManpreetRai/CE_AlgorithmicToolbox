# Uses python3

def get_change(m):
    count_coins = 0
    (div10, rem10) = divmod(m, 10)

    count_coins += div10
    if rem10 >= 5:
        (div5, rem5) = divmod(rem10, 5)
        count_coins = count_coins + div5 + rem5
    else:
        count_coins += rem10

    return count_coins

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
