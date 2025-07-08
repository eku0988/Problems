# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emp_map = {emp.id: emp for emp in employees}
    
        def dfs(eid):
            employee = emp_map[eid]
            total = employee.importance
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total
        
        return dfs(id)