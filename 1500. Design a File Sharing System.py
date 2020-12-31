class FileSharing:

    def __init__(self, m: int):
        self.heap = [i for i in range(1, m+1)]
        heapq.heapify(self.heap)
        self.files = collections.defaultdict(list)
        self.user_own = collections.defaultdict(list)

    def join(self, ownedChunks: List[int]) -> int:
        current_user = -1
        if self.heap:
            current_user = heapq.heappop(self.heap)
            for file in ownedChunks:
                self.user_own[current_user].append(file)
                self.files[file].append(current_user)
        return current_user
            
    def leave(self, userID: int) -> None:
        heapq.heappush(self.heap, userID)
        for file in self.user_own[userID]:
            self.files[file].remove(userID)
        self.user_own[userID].clear()

    def request(self, userID: int, chunkID: int) -> List[int]:
        if chunkID in self.files and self.files[chunkID]:
            ret = self.files[chunkID][:]
            if userID not in self.files[chunkID]:
                self.files[chunkID].append(userID)
            if chunkID not in self.user_own[userID]:
                self.user_own[userID].append(chunkID)
            return sorted(ret)
        else:
            return []


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)