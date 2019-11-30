#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (35.96%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 26.8K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#
# class Solution(object):
#     # 本题采用广度遍历方法
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         # 首先给wordList列表中单词去重
#         word_set = set(wordList)
#         word_dict = {}
#         for word in word_set:
#             for index in range(len(word)):
#                 new_word = word[:index]+"_"+word[index+1:]
#                 if new_word not in word_dict:
#                     word_dict[new_word] = [word]
#                 else:
#                     word_dict[new_word].append(word)
#         # 定义当前层的单词集合为beginWord
#         cur_word = [beginWord]
#         # 定义下一层的单词集合
#         next_word = []
#         # 定义从 beginWord 到 endWord 的最短转换序列的长度
#         depth = 1
#         while cur_word:
#             for word in cur_word:
#                 # 如果endWord出现在当前层的cur_word单词集合中，则立即返回该深度
#                 if word == endWord:
#                     return depth
#                 for index in range(len(word)):
#                     new_word = word[:index]+"_"+word[index+1:]
#                     if new_word in word_dict:
#                         for w in word_dict[new_word]:
#                             if w not in next_word:
#                                 next_word.append(w)
#                         del word_dict[new_word]
#             # 如果endWord未出现在当前层的cur_word单词集合中，则深度+1
#             depth += 1
#             cur_word = next_word
#             next_word = []
#         return 0

from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                # print(repr(visited))
                # print(queue)
                all_combo_dict[intermediate_word] = []
        return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "log"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sequence_length = Solution().ladderLength(beginWord, endWord, wordList)
    print(sequence_length)


