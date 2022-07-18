# FIHP (first in high priority).
#
# В случае коллизии наблюдается спутник, который первым попал в
# зону видимости станции мониторинга. Для этого алгоритма, станция РТМ в случае коллизии
# продолжает следить за спутником, не переходя к наблюдению нового.
# После этого выбирается спутник, который первым вошел в область наблюдения при коллизии.
#
# Алгоритм прост в реализации, однако не гарантирует равномерность распределения по времени,
# при этом возникает вероятность пропуска спутника, который наблюдается кратковременно одновременно
# с другим спутником.
import numpy as np


def findVisible(data, j):
    for i in range(len(data)):
        if data[i][j] == 1:
            return i + 1

    return 0


def FIHP(data):
    res = np.zeros(len(data[0]), dtype=np.int64)

    res[0] = findVisible(data, 0)

    for j in range(1, len(data[0])):
        if data[res[j-1]-1][j] == 1:
            res[j] = res[j-1]
            continue

        res[j] = findVisible(data, j)

    return res