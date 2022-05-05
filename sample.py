import numpy as np
List_sub = [0, 1]

s = [0, 0, 0, 0, 0]
test2 = [0, 0, 0, 0, 0]

b = np.zeros(shape=(10))

for i in range(5): 
    test = np.random.choice(List_sub, 1, p=[0.05, 0.95])
    
    s[i] = test.tolist()
    test2[i] = test

    
    b[i] = test


a = np.zeros(shape=(100))
a[0] = test
print(a)
# print(type(test))
# print(type(a))
print(s)
print(test2)

print(b)
