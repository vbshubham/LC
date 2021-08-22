#
# Complete the 'get_friends_count' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num_of_people
#  2. STRING_ARRAY friends
def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, u, v):
    x, y = find(parent, u), find(parent, v)
    if x != y:
        parent[x] = y


def get_friends_count(num_of_people, friends):
    parent = {v: v for v in range(1, num_of_people + 1)}
    for _ in range(len(friends)):
        u, v = map(int, input().split(' '))
        union(parent, u, v)

    set_counts = {}
    for v in parent:
        group = find(parent, v)
        set_counts[group] = set_counts.get(group, 0) + 1

    ans = sum([int(n * (n - 1) / 2) for n in set_counts.values()])
    return ans
