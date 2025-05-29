# Problem: Tower of Hanoi  - https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

class Solution:
    def towerOfHanoi(self, n, from_rod, to_rod, aux_rod):
        if n == 0:
            return
        self.towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
        print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
        self.towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
