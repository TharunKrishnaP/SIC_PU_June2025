import numpy as np
arr1 = np.arange(12)
print("Order 1x12 ",arr1)
print("Reshaping into 2x6 matrix")
arr2 = arr1.reshape(2,6)
arr3 = arr1.reshape(3,4)
arr4 = arr1.reshape(4,3)
arr5 = arr1.reshape(6,2)
arr6 = arr1.reshape(12,1)

print("Reshaping into Order 2x6 \n",arr2)
print("Reshaping into Order 3x4 \n",arr3)
print("Reshaping into Order 4x3 \n",arr4)
print("Reshaping into Order 6x2 \n",arr5)
print("Reshaping into Order 12x1 \n",arr6)

arr7 = np.arange(1,10).reshape(3,-1)
print("Array 7: \n",arr7)