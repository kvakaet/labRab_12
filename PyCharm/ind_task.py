#!usr/bin/env python3
# -*- coding: utf-8 -*-


def calc(m, n):
    if m == 0 or m == n:
        return 1
    else:
        return calc(m, n - 1) + calc(m - 1, n - 1)


if __name__ == '__main__':
    start_m, start_n = int(input()), int(input())
    C = calc(start_m, start_n) if 0 <= start_m <= start_n else print('неверные числа')

    print(C)
