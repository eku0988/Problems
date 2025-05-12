# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

#{ 
 # Driver Code Starts
import math



# } Driver Code Ends

#Complete this function

class Solution:
    def josephus(self,n,k):
        #Your code here
        # python code to implement Josephus problem 


        # initialize two variables i and ans
        i = 1
        ans = 0
        while(i <= n):
    
            # update the value of ans
            ans = (ans + k) % i
            i += 1
        
        # returning the required answer
        return ans + 1
    
   


#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        n=int(input())
        k=int(input())
        print(Solution().josephus(n,k))
        
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends