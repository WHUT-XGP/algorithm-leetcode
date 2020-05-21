# -*- coding = utf-8 -*-
# @Time : 2020/5/17 21:26
# @Author : AX
# @File : 部分和.py
# @Software: PyCharm


'''
求解部分和问题
题目内容：
给出N个正整数组成的数组A，求能否从中选出若干个，使他们的和为K。如果可以，输出："YES"，否则输出"NO"。
输入格式:
第1行：2个数N、K, N为数组的长度, K为需要判断的和(2 ≤N ≤ 20，1 ≤ K ≤ 10^9)
第2 到第 N + 1行：每行1个数，对应数组的元素A[i] (1 ≤ A[i]≤ 10^6)
输出格式：
如果可以，输出："YES"，否则输出"NO"。
样例输入
4 13
1
2
4
7
样例输出
YES
输入样例：
5 9
1
2
3
4
5
输出样例：
YES

'''
'''
一.遍历寻找所有可能性
二.剪枝：如果已经大于或等于，则该方向就不再寻找
三.比较所有结果叶子节点，查看是否有相等
'''

# 引入队列
from collections import deque
def main():
    while True:
        n = int(input())
        target = int(input())
        queue = deque([])
        arr = []
        for i in range(n):
            arr.append(int(input()))
        print(queue)
        print(arr)

if __name__ == '__main__':
    main()