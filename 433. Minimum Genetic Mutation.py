class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        if start == end:
            return 0
        mode = collections.defaultdict(list)
        for gen in bank:
            for i in range(len(gen)):
                mode[gen[:i] + "*" + gen[i + 1:]].append(gen)
        seen = set()
        queue = [start]
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur == end:
                    return step
                for i in range(len(cur)):
                    m = cur[:i] + "*" + cur[i + 1:]
                    if m in seen:
                        continue
                    seen.add(m)
                    can = mode[m]
                    if can:
                        for next_gen in can:
                            queue.append(next_gen)
            step += 1
        return -1