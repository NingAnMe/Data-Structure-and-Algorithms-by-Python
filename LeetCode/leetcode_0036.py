#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/14 11:04
@Author  : AnNing
"""
"""有效的数独
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

数独部分空格内已填入了数字，空白格用 '.' 表示。

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
"""
"""算法
1. 判断每一行是否存在相同数字
2. 判断每一列是否存在相同数字
3. 计算每一个小矩形的位置
4. 计算每一个小矩形是否存在相同数字
时间复杂度O(n^2),n为边长，空间复杂度O(n)
"""



class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 检查行
        for i in range(9):
            row_data = board[i]
            if not self.check_right(row_data):
                return False
        # 检查列
        for i in range(9):
            col_data = list()
            for k in range(9):
                col_data.append(board[k][i])
            if not self.check_right(col_data):
                return False
        # 检查9方格
        splices = [(0, 3), (3, 6), (6, 9)]
        for i in splices:
            for k in splices:
                mat_data = list()
                rows = board[i[0]:i[1]]
                for row in rows:
                    mat_data.extend(row[k[0]:k[1]])
                if not self.check_right(mat_data):
                    return False
        return True

    def check_right(self, data):
        d = set()
        for i in data:
            if i == '.':
                continue
            if i in d:
                return False
            else:
                d.add(i)
        return True


if __name__ == '__main__':
    test_data1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    test_data2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    s = Solution()
    print(s.isValidSudoku(test_data1))
    print(s.isValidSudoku(test_data2))
