import math

# 点数
scores = [20, 60, 65, 70, 100]

# 100点が1人、0点が39人
scores = [100] + [0 for i in range(39)]

# 0点が1人、100点が39人
# scores = [0] + [100 for i in range(39)]

# 人数
n = len(scores)

# 平均: average
avg = sum(scores) / n

# 偏差: deviation
dev_l = []
for score in scores:
    dev = score - avg
    dev_l.append(dev)

# 分散: variance
var = sum([dev * dev for dev in dev_l]) / n

# 標準偏差: standard deviation
sd = math.sqrt(var)

# 偏差値 (日本独特の概念なので適切な英語はない)
hensachi_d = {}
for score in scores:
    dev = score - avg
    if sd != 0:
        hensachi_d[str(score) + '点'] = 50 + 10 * dev / sd
    else:
        hensachi_d[str(score) + '点'] = 50

# 出力
print('人数 :', n)
print('点数 :', scores)
print('平均 :', round(avg, 2))
print('偏差 :', [round(dev, 2) for dev in dev_l])
print('分散 :', round(var, 2))
print('標準偏差 :', round(sd, 2))
print()
print('点数 : 偏差値')
for score, hensachi in hensachi_d.items():
    print(score, ':', round(hensachi, 2))