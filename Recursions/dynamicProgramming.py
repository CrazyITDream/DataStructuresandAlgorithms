# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:          dynamicProgramming
# Author:        xiaohuo
# Date:          2020/4/4
# Prohect_Name:  data_structure
# IEDA_Name:     PyCharm
# Create_Time:   12:35 
# -------------------------------------------------------------------------------


# def recMc(coinValueList, change):
#     minCoins = change
#     if change in coinValueList:
#         return 1
#     else:
#         for i in [c for c in coinValueList if c<= change]:
#             numCoins = 1 + recMc(coinValueList, change-i)
#             if numCoins < minCoins:
#                  minCoins = numCoins
#         return minCoins

# def recMc(coinValueList, change, knownResult):
#     minCoins = change
#     if change in coinValueList:
#         knownResult[change] = 1
#         return 1
#     elif knownResult[change] > 0:
#         return knownResult[change]
#     else:
#         for i in [c for c in coinValueList if c <= change]:
#             numCoins = 1 + recMc(coinValueList, change - i, knownResult)
#             if numCoins < minCoins:
#                 minCoins = numCoins
#                 knownResult[change] = minCoins
#     return minCoins
#
#
# print(recMc([1, 5, 10, 25], 63, [0]*64))


# def dpMakeChange(coinValueList, change, minCoins):
#     for cents in range(change+1):
#         coinCount = cents
#         for j in [c for c in coinValueList if c<=cents]:
#             if minCoins[cents-j] + 1 < coinCount:
#                 coinCount = minCoins[cents - j]+1
#         minCoins[cents] = coinCount     # 最少硬币数
#
#     return minCoins[change]

# def dpMakeChangePro(coinValueList, change, minCoins, coinsUsed):
#     for cents in range(change+1):
#         coinCount = cents
#         newCoin = 1
#         for j in [c for c in coinValueList  if c<= cents]:
#             if minCoins[cents-j] + 1 < coinCount:
#                 coinCount = minCoins[cents-j] + 1
#                 newCoin = j
#         minCoins[cents] = coinCount
#         coinsUsed[cents] = newCoin
#     return minCoins[change]
#
# def printCoins(coinUsed, change):
#     coin = change
#     while coin > 0:
#         thisCoin = coinUsed[coin]
#         print(thisCoin)
#         coin -= thisCoin
#
#
# if __name__ == '__main__':
#     c1 = [1, 3, 5, 10, 21, 25]
#     coinsUsed = [0]*64
#     coinCount = [0]*64
#     print(dpMakeChangePro(c1, 63, coinCount, coinsUsed))
#     printCoins(coinsUsed, 63)
#     printCoins(coinsUsed, 52)
#     print(coinsUsed)



