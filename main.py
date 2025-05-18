memo = {}
parent = []
size = []

def initialize(n):
    global parent, size
    parent = list(range(n))
    size = [1] * n

def find(x):
    root = x
    if parent[root] != root:
        parent[root] = find(parent[root])
        root = parent[root]
    return root

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    should_union = root_x != root_y
    if should_union:
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]

def get_size(x):
    return size[find(x)]

def partition_count(n):
    result = 0
    if n in memo:
        result = memo[n]
    elif n == 0:
        result = 1
    elif n < 0:
        result = 0
    else:
        k = 1
        pentagonal1 = 0
        pentagonal2 = 0
        continue_loop = True
        while continue_loop:
            pentagonal1 = k * (3 * k - 1) // 2
            pentagonal2 = k * (3 * k + 1) // 2
            continue_loop = not (pentagonal1 > n and pentagonal2 > n)
            if continue_loop:
                sign = -1 if k % 2 == 0 else 1
                result += sign * partition_count(n - pentagonal1)
                result += sign * partition_count(n - pentagonal2)
                k += 1
        memo[n] = result % 1000000007
        result = memo[n]
    return result

def process_operations(n, operations):
    initialize(n)
    results = []
    for op in operations:
        if op[0] == "union":
            union(op[1] - 1, op[2] - 1)
        elif op[0] == "partitions":
            set_size = get_size(op[1] - 1)
            results.append(partition_count(set_size))
    return results

def main():
    global memo
    memo = {}
    try:
        t = int(input())
        for _ in range(t):
            n, m = map(int, input().split())
            operations = []
            for _ in range(m):
                op = input().split()
                if op[0] == "union":
                    operations.append(["union", int(op[1]), int(op[2])])
                elif op[0] == "partitions":
                    operations.append(["partitions", int(op[1])])
            results = process_operations(n, operations)
            for result in results:
                print(result)
    except EOFError:
        pass

def main_from_file(filename):
    global memo
    memo = {}
    with open(filename, 'r') as f:
        t = int(f.readline().strip())
        for _ in range(t):
            n, m = map(int, f.readline().strip().split())
            operations = []
            for _ in range(m):
                op = f.readline().strip().split()
                if op[0] == "union":
                    operations.append(["union", int(op[1]), int(op[2])])
                elif op[0] == "partitions":
                    operations.append(["partitions", int(op[1])])
            results = process_operations(n, operations)
            for result in results:
                print(result)

if __name__ == "__main__":
    main()
