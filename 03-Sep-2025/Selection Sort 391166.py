# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        
        # Traverse through all array elements
        for i in range(n):
            # Assume the minimum is the first element of unsorted part
            min_idx = i
            
            # Find the index of the minimum element in the remaining array
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap the found minimum element with the first element of unsorted part
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr
