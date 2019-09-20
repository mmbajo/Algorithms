# Uses python3
import sys
inf = float('inf')
def DPchange(money, coins):
    MinNumCoins = (money + 1) * [0]
    for m in range(1, money + 1):
        MinNumCoins[m] = inf
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m - coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(DPchange(m, [1, 3, 4]))
