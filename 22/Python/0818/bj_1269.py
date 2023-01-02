# 대칭 차집합
A, B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

print(len(A_set ^ B_set))

# 교집합
# set1 = set([1, 2, 3, 4, 5, 6])
# set2 = set([3, 4, 5, 6, 8, 9])
#
# print(set1 & set2)
# print(set1.intersection(set2))
#
# {3, 4, 5, 6}
# {3, 4, 5, 6}

# 합집합
# set1 = set([1, 2, 3, 4, 5, 6])
# set2 = set([3, 4, 5, 6, 8, 9])
#
# print(set1 | set2)
# print(set1.union(set2))
#
# {1, 2, 3, 4, 5, 6, 8, 9}
# {1, 2, 3, 4, 5, 6, 8, 9}

# 차집합
# set1 = set([1, 2, 3, 4, 5, 6])
# set2 = set([3, 4, 5, 6, 8, 9])
#
# print(set1 - set2)
# print(set1.difference(set2))
#
# {1, 2}
# {1, 2}

# set.add(1개) / set.update(여러 개)