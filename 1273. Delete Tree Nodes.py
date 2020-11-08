class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree = collections.defaultdict(list)
        for n, p in enumerate(parent):
            tree[p].append(n)
        for i in range(nodes):
            if i not in tree:
                tree[i] = []

        def helper(node):
            nodes_sum = value[node]
            nodes_num = 1
            for child in tree[node]:
                c_sum, c_num = helper(child)
                nodes_sum += c_sum
                nodes_num += c_num

            if nodes_sum == 0:
                return 0, 0
            else:
                return nodes_sum, nodes_num

        return helper(0)[1]