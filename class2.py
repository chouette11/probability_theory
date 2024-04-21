import random

def class2(index):
    rand_val = random.random()  # 一度だけ乱数を生成

    if index == 1:
        if rand_val < 0.5:
            return 0
        elif rand_val < 0.75:
            return 2
        else:
            return 4
    elif index == 2:
        if rand_val < 0.25:
            return 1
        elif rand_val < 0.5:
            return 0
        elif rand_val < 0.75:
            return 5
        else:
            return 3
    elif index == 3:
        if rand_val < 0.33333:
            return 2
        elif rand_val < 0.66667:
            return 6
        else:
            return 0
    elif index == 4:
        if rand_val < 0.25:
            return 5
        elif rand_val < 0.5:
            return 1
        elif rand_val < 0.75:
            return 0
        else:
            return 7
    elif index == 5:
        if rand_val < 0.25:
            return 4
        elif rand_val < 0.5:
            return 2
        elif rand_val < 0.75:
            return 6
        else:
            return 7
    elif index == 6:
        if rand_val < 0.5:
            return 3
        else:
            return 5

def run_simulation(start_index):
    index = start_index
    while index not in (0, 7):  # 0または7になるまで続ける
        index = class2(index)
    return index  # 最終的に0か7で終わる

# シミュレーションを多数回実行して、7で終了する確率を求める
for i in range(1, 7):
    trials = 10000
    end_at_7 = sum(run_simulation(i) == 7 for _ in range(trials))
    probability = end_at_7 / trials
    print(f"Starting from index {i}, the probability of ending at 7 is approximately {probability:.4f}")
