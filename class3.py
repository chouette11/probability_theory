import random

def class3(n):
    found = set()
    count = 0

    while len(found) < n:
        # 0からn-1までのランダムな整数を生成
        new_coupon = random.randint(0, n-1)
        # 新しいクーポンを集合に追加
        found.add(new_coupon)
        # 試行回数をカウント
        count += 1

    return count

# 1-100までのクーポンの種類の数に対して、100回の平均試行回数を求め、グラフに表示
import matplotlib.pyplot as plt

x = list(range(1, 101))
y = [sum(class3(i) for _ in range(100)) / 100 for i in x]
plt.plot(x, y)
plt.xlabel('Number of coupon types')
plt.ylabel('Average number of trials')
# x軸を0-1000までに設定
plt.xlim(0, 1000)
# y軸を0-1000までに設定
plt.ylim(0, 1000)
# ウィンドウの横幅と縦幅を設定
plt.show()
