# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = {}

        for i, recipe in enumerate(recipes):
            in_degree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)

        queue = deque(supplies)
        result = []
        available = set(supplies)

        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
                    available.add(recipe)

        return result