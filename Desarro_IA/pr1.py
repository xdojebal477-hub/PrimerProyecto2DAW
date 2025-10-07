import numpy as np

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array( [ [
                    [1, 2, 3],[4, 5, 6]
                ],
                [
                    [7, 8, 9],[10, 11, 12]
                ],
                [
                    [13, 14, 15],[16, 17, 18]
                ]
                ] )




# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
arr = np.array([[[1, 2], 
                [3, 4]], 
                [[5, 6], 
                [7, 8]]])





print(arr.ndim)
print(arr.shape)
print(d.ndim)
print(d.shape)