#pandas series

import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print("\n")

print(s2)


#indexing and selection series

print("\n")

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print("\n")

print(marks[['Math', 'Chemistry']])


#boolean masking  in series
print("\n")

scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)


#handling missing data in series
print("\n")

data = pd.Series([10, None, 30, None])

print(data.isnull())
print("\n")

print(data.fillna(0))

#vectorized string operations
print("\n")

names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print("\n")

print(names.str.contains('a'))