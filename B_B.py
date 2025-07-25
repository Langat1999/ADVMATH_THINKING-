#0/1 Knapsack Problem via Branch-and-Bound
#Problem: Given items with weights and values and a knapsack with a weight capacity, determine the maximum total value obtainable without exceeding the capacity.
#Node Representation: Each node represents a decision point—items included so far, total weight, total profit—and an upper bound of future profit.
#Bound Calculation: For a node, we estimate the best possible outcome by taking as many of the remaining items (or fractions) as possible (even though only whole items can finally be selected).
#Branching: For each decision node, the algorithm creates two child nodes: one that includes the next item and one that excludes it.
#Pruning: Nodes whose bound is less than the current maximum profit are dropped from further consideration.
#This example illustrates the branch-and-bound technique to systematically search for a solution while avoiding unnecessary calculations
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level      # Level in the decision tree (index of item being considered)
        self.profit = profit    # Total profit accumulated
        self.weight = weight    # Total weight accumulated
        self.bound = bound      # Upper bound on maximum profit achievable from this node

def bound(node, n, capacity, items):
    """Compute the upper bound on the maximum profit in the subproblem defined by this node."""
    if node.weight >= capacity:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    totweight = node.weight

    # Take items in order while under the capacity
    while j < n and totweight + items[j][0] <= capacity:
        totweight += items[j][0]
        profit_bound += items[j][1]
        j += 1

    # If there is still capacity, take fraction of the next item
    if j < n:
        profit_bound += (capacity - totweight) * items[j][1] / items[j][0]
    return profit_bound

def knapsack_branch_and_bound(capacity, items):
    """Solve the 0/1 knapsack problem using branch and bound.
       items: list of tuples (weight, profit). Items are sorted by profit/weight ratio descending."""
    
    items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    n = len(items)
    max_profit = 0
    queue = []

    # Start with a dummy node at level -1
    v = Node(level=-1, profit=0, weight=0, bound=0)
    v.bound = bound(v, n, capacity, items)
    queue.append(v)

    while queue:
        v = queue.pop(0)  # Pop the first node (BFS style)
        if v.level == n - 1 or v.bound <= max_profit:
            continue

        u_level = v.level + 1

        # Case 1: Include the next item
        u = Node(
            level=u_level,
            profit=v.profit + items[u_level][1],
            weight=v.weight + items[u_level][0],
            bound=0
        )
        if u.weight <= capacity and u.profit > max_profit:
            max_profit = u.profit

        u.bound = bound(u, n, capacity, items)
        if u.bound > max_profit:
            queue.append(u)

        # Case 2: Exclude the next item
        u2 = Node(
            level=u_level,
            profit=v.profit,
            weight=v.weight,
            bound=0
        )
        u2.bound = bound(u2, n, capacity, items)
        if u2.bound > max_profit:
            queue.append(u2)

    return max_profit

# Define items as (weight, profit)
items = [(2, 40), (3, 50), (5, 100), (1, 20)]
capacity = 5
result = knapsack_branch_and_bound(capacity, items)
print("Maximum profit for the knapsack problem:", result)