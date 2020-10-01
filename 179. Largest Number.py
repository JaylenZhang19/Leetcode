class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_list = list(map(str, nums))
        str_list.sort(key=functools.cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        return "0" if "".join(str_list)[0] == "0" else "".join(str_list)