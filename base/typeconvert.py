# list -> set
s1 = set([1,2,3])

# tuple -> set
s2 = set((1,2,3))

# set -> list
s3 = list({1,2,3})

# set -> tuple
s4 = tuple({1,2,3})

# list -> iterator
s5 = iter([1,2,3])
print(next(s5))