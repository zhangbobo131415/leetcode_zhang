class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(0)
        self.recon_core(pre, tin, 0, len(pre)-1, 0, len(tin)-1, root)
        return root

    def recon_core(self, pre, tin, start_pre, end_pre, start_tin, end_tin, root):
        root.val = pre[start_pre]
        if start_pre == end_pre:
            root.val = pre[start_pre]
            return
        index = tin.index(pre[start_pre])
        print(index)
        # 跳过，一些判断，先写主干
        if index == start_tin:
            root.left = None
            root.right = TreeNode(pre[start_pre + 1])
            self.recon_core(pre, tin, start_pre+1, end_pre,
                            start_tin+1, end_tin, root.right)
        elif index == end_tin:
            root.right = None
            root.left = TreeNode(pre[start_pre + 1])
            self.recon_core(pre, tin, start_pre+1, end_pre,
                            start_tin, end_tin-1, root.left)
        else:
            root.left = TreeNode(pre[start_pre + 1])
            root.right = TreeNode(pre[start_pre+index - start_tin+1])
            self.recon_core(pre, tin, start_pre+1, start_pre +
                            index - start_tin, start_tin, index-1, root.left)
            self.recon_core(pre, tin, start_pre+index - start_tin +
                            1, end_pre, index+1, end_tin, root.right)


test = Solution()
test.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7])
