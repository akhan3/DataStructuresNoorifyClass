from array import array


class MyArray(object):
	def __init__(self, typecode='i', *args):
		self._typecode = typecode
		initial_values = [arg for arg in args]
		self._arr = array(typecode, initial_values)
		self._capacity = len(initial_values)
		self._size = len(args)

	def get(self, index):
		return self._arr[index]

	def set(self, index, value):
		self._arr[index] = value

	def size(self):
		return self._size

	def append(self, value):
		self._size += 1
		
		if self._size > self._capacity:
			self._arr = self._expand_capacity(self._arr)

		self._arr[self._size-1] = value

		return self

	def remove(self, value):
		index = -1
		for i in range(self._size):
			if self._arr[i] == value:
				index = i
				break;

		if index == -1:
			raise ValueError("Value not found in array.")

		k = index + 1
		while k < self._size:
			self._arr[k-1] = self._arr[k]
			k += 1

		self._size -= 1

		return self

	def insert(self, index, value):
		self._size += 1

		if self._size > self._capacity:
			self._arr = self._expand_capacity(self._arr)

		i = self._size - 1
		while i > index:
			self._arr[i] = self._arr[i-1]
			i -= 1
		
		self._arr[index] = value

	def pop(self, index = -1):
		if index == -1 and self._size == 0:
			raise IndexError("Array is empty.")

		if index >= self._size:
			raise IndexError("Index out of bounds.")

		if index > -1:
			k = index + 1
			while k < self._size:
				self._arr[k-1] = self._arr[k]
				k += 1

		self._size -= 1

	def _expand_capacity(self, current_arr):
		if len(current_arr) == 0:
			new_arr = array(self._typecode, [-1])
		else:
			new_arr = array(self._typecode, [i for i in range(2 * len(current_arr))])
		
		for j in range(len(current_arr)):
			new_arr[j] = current_arr[j]

		return new_arr

	def __str__(self):
		return "arr={} size={} capacity={}".format(self._arr, self._size, self._capacity)


# myarray = MyArray('i', 10, 20 ,30)
# myarray.append(40)
# print(myarray)

# myarray = MyArray('i', 10, 20 ,30)
# myarray.insert(1, 50)
# print(myarray)

# # 10, 50, 20, 30