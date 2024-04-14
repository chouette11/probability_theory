import random
from collections import defaultdict

# 山手線の駅名リスト
yamanote_stations = [
    "東京", "神田", "秋葉原", "御徒町", "上野", "鶯谷", "日暮里", "西日暮里", "田端", "駒込",
    "巣鴨", "大塚", "池袋", "目白", "高田馬場", "新大久保", "新宿", "代々木", "原宿", "渋谷",
    "恵比寿", "目黒", "五反田", "大崎", "品川", "田町", "浜松町", "新橋", "有楽町"
]

# 最後にTrueになった駅の出現回数を記録する辞書
station_counts = defaultdict(int)

# 100回のシミュレーションを実行
for _ in range(10000):
    station_visited = {station: False for station in yamanote_stations}
    index = 0
    last_true_station = None

    while not all(station_visited.values()):
        if not station_visited[yamanote_stations[index]]:
            station_visited[yamanote_stations[index]] = True
            last_true_station = yamanote_stations[index]

        if random.random() < 0.5:
            index += 1
            if index >= len(yamanote_stations):
                index = 0
        else:
            index -= 1
            if index < 0:
                index = len(yamanote_stations) - 1

    # 最後にTrueに変更された駅名を記録
    station_counts[last_true_station] += 1

# 出現回数の結果を表示
for station, count in sorted(station_counts.items(), key=lambda item: item[1], reverse=True):
    print(f"{station}: {count}回")
