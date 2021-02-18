class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        arr = []
        arr.append(first) 
        for i in range(0, n):
            arr.append(encoded[i] ^ arr[i])
        return arr
        