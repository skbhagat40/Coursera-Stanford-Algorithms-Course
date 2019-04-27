# coding: utf-8

# In[5]:


def add_matrices(mat_a, mat_b):
    c = [[0] * len(mat_a[0]) for i in range(len(mat_a))]
    for i in range(len(mat_a)):
        for j in range(len(mat_a[0])):
            c[i][j] = mat_a[i][j] + mat_b[i][j]
    return c


# In[6]:


add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])


# In[64]:


def strassens(mat_a, mat_b):
    if len(mat_a) == 1 and len(mat_b) == 1:
        return [[mat_a[0][0] * mat_b[0][0]]]
    else:
        a, b, c, d, e, f, g, h = [], [], [], [], [], [], [], []
        mid1 = len(mat_a) // 2
        mid2 = len(mat_a[0]) // 2
        for i in range(mid1):
            temp1 = []
            temp2 = []
            for j in range(mid2):
                temp1.append(mat_a[i][j])
                temp2.append(mat_b[i][j])
            a.append(temp1)
            e.append(temp2)

        for i in range(mid1, len(mat_a)):
            temp1 = []
            temp2 = []
            for j in range(mid2):
                temp1.append(mat_a[i][j])
                temp2.append(mat_b[i][j])
            c.append(temp1)
            g.append(temp2)

        for i in range(mid1):
            temp1 = []
            temp2 = []
            for j in range(mid2, len(mat_a[0])):
                temp1.append(mat_a[i][j])
                temp2.append(mat_b[i][j])
            b.append(temp1)
            f.append(temp2)

        for i in range(mid1, len(mat_a)):
            temp1 = []
            temp2 = []
            for j in range(mid2, len(mat_a[0])):
                temp1.append(mat_a[i][j])
                temp2.append(mat_b[i][j])
            d.append(temp1)
            h.append(temp2)
        q1 = add_matrices(strassens(a, e), strassens(b, g))
        q2 = add_matrices(strassens(a, f), strassens(b, h))
        q3 = add_matrices(strassens(c, e), strassens(d, g))
        q4 = add_matrices(strassens(c, f), strassens(d, h))

        res = [[0] * len(mat_a[0]) for i in range(len(mat_a))]
        # copy q1,q2,q3,q4 into res matrix!!
        for i in range(len(q1)):
            for j in range(len(q1[0])):
                res[i][j] = q1[i][j]

        for i in range(len(q2)):
            for j in range(len(q2[0])):
                res[i][j + mid1] = q2[i][j]

        for i in range(len(q3)):
            for j in range(len(q3[0])):
                res[i + mid1][j] = q3[i][j]

        for i in range(len(q4)):
            for j in range(len(q4[0])):
                res[i + mid1][j + mid1] = q4[i][j]

        return res


# In[65]:


strassens([[1, 2, 5, 6], [3, 4, 7, 8], [11, 12, 13, 14], [15, 16, 17, 18]],
          [[1, 2, 5, 6], [3, 4, 7, 8], [11, 12, 13, 14], [15, 16, 17, 18]])

# In[60]:


import numpy as np

a = np.array([[1, 2], [3, 4]])
e = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
g = np.array([[11, 12], [15, 16]])
r = a.dot(e) + b.dot(g)
print(r)
final = np.dot(np.array([[1, 2, 5, 6], [3, 4, 7, 8], [11, 12, 13, 14], [15, 16, 17, 18]]),
               np.array([[1, 2, 5, 6], [3, 4, 7, 8], [11, 12, 13, 14], [15, 16, 17, 18]]))

# In[61]:


final

