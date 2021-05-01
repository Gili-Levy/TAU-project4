# Skeleton file for HW4 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include the ID number of the student submitting the solution (hw4_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# The first ID should be the ID of the student submitting the solution
# For example: SUBMISSION_IDS = ["123456000", "987654000"]
SUBMISSION_IDS = ["316296771"]

############
# QUESTION 2
############

# a

def best_mat_mult_time(L):
	if (len(L)) == 3:  # stop recursive when there are 2 mat left
		return L[0]*L[1]*L[2]

	right = best_mat_mult_time(L[1:])
	left = best_mat_mult_time(L[:len(L)-1])

	if right < left:
		return L[0]*L[1]*L[len(L)-1] + right
	else:
		return left + L[0]*L[len(L)-2]*L[len(L)-1]

#print(best_mat_mult_time([40, 20, 30, 10, 30]))
# b

def best_mat_mult_time_fast(L):
	memo = []
	return best_mat_mult_time_fast_with_memo(L, memo)


def best_mat_mult_time_fast_with_memo(L, memo):
	if L in memo:
		return memo[memo.index(L)+1]

	if (len(L)) == 3:  # stop recursive when there are 2 mat left
		result = L[0]*L[1]*L[2]
		memo.append(L)
		memo.append(result)
		return result

	right = best_mat_mult_time(L[1:])
	if L[1:] not in memo:
		memo.append(L[1:])
		memo.append(right)
	
	left = best_mat_mult_time(L[:len(L)-1])
	if L[:len(L)-1] not in memo:
		memo.append(L[:len(L)-1])
		memo.append(left)

	if right < left:
		return L[0]*L[1]*L[len(L)-1] + right
	else:
		return left + L[0]*L[len(L)-2]*L[len(L)-1]


# c

def best_mat_mult_order(L):
	pass
"""
	if (len(L)) == 3:  # stop recursive when there are 2 mat left
		return (L[0]*L[1]*L[2], [0, 0])

	right = best_mat_mult_time(L[1:])
	left = best_mat_mult_time(L[:len(L)-1])

	if right[0] < left[0]:
		return (L[0]*L[1]*L[len(L)-1] + right, [0, right[1]])
	else:
		return (left + L[0]*L[len(L)-2]*L[len(L)-1], [left[1], len(L)-1])

print (best_mat_mult_order([10,100,10,100]))
"""
def mult_order_to_str(mult_order):
	if type(mult_order) is int:
		return str(mult_order)

	return f"({mult_order_to_str(mult_order[0])}) * ({mult_order_to_str(mult_order[1])})"


############
# QUESTION 3
############

# b
def had_local(n, i, j):
	
	if n==0: # stop recursion at had(0)
		return 0
	
	if i <= (2**(n-1)-1) and j <= (2**(n-1)-1): #block 1
		return had_local(n-1, i, j)
	
	elif i <= (2**(n-1)-1) and j > (2**(n-1)-1):  # block 2
		return had_local(n-1, i, j-2**(n-1))
	
	elif i > (2**(n-1)-1) and j <= (2**(n-1)-1):  # block 2
		return had_local(n-1, i-2**(n-1), j)
	
	elif i > (2**(n-1)-1) and j > (2**(n-1)-1):  # block 4 (opposite matrix)
		if had_local(n-1,i-2**(n-1), j-2**(n-1)) == 0:
			return 1
		else:
			return 0
	
print (had_local(2,0,0))
# d
def had_complete(n): return None  # replace this with your code

############
# QUESTION 4
############

# a


def grid_escape1(B):
	pass  # replace this with your code

# b


def grid_escape2(B):
	pass  # replace this with your code


############
# QUESTION 5
############

# a
def partition(S):
	pass  # replace this with your code


# b
def n_to_k(n, k):
	pass  # replace this with your code


############
# QUESTION 6
############

def distance(s1, s2):
	pass


def distance_fast(s1, s2):
	pass


########
# Tester
########

def test():

	# Q2
	L1 = [100, 10, 100, 10]
	# a
	if best_mat_mult_time(L1) != 20000:
		print("Error in best_mat_mult_time")
	# b
	if best_mat_mult_time_fast(L1) != 20000:
		print("Error in best_mat_mult_time_fast")
	# c
	if mult_order_to_str(best_mat_mult_order(L1)) != "(0) * ((1) * (2))":
		print("Error in best_mat_mult_order")

	# Q3
	# b
	if(had_local(2, 2, 2) != 1):
		print("Error in had_local")
	# d
	if had_complete(1) != [[0, 0], [0, 1]]:
		print("Error in had_complete")

	# Q4
	B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
	B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
	B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]

	# a
	if grid_escape1(B1) is False:
		print("Error in grid_escape1 - B1")
	if grid_escape1(B2) is True:
		print("Error in grid_escape1 - B2")
	if grid_escape1(B3) is True:
		print("Error in grid_escape1 - B3")

	# b
	if grid_escape2(B1) is False:
		print("Error in grid_escape2 - B1")
	if grid_escape2(B2) is False:
		print("Error in grid_escape2 - B2")
	if grid_escape2(B3) is True:
		print("Error in grid_escape2 - B3")

	# Q5
	# a
	if partition([3, 1, 1, 2, 2, 1]) is False:
		print("Error in partition - 1")
	if partition([1, 1, 1]) is True:
		print("Error in partition - 2")

	# b
	if n_to_k(4, 2) != 7:
		print("Error in n_to_k")

	# Q6
	if distance('computer', 'commuter') != 1 or \
			distance('sport', 'sort') != 1 or \
			distance('', 'ab') != 2 or distance('kitten', 'sitting') != 3:
		print("Error in distance")

	if distance_fast('computer', 'commuter') != 1 or \
			distance_fast('sport', 'sort') != 1 or \
			distance_fast('', 'ab') != 2 or distance_fast('kitten', 'sitting') != 3:
		print("Error in distance_fast")
