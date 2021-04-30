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
	if (len(L)) == 4: # when there are 3 mat left
		for i in range (len(L)):
			op1 = L[0]*L[1]*L[2] + L[0]*L[2]*L[3]
			op2 = L[1]*L[2]*L[3] + L[0]*L[1]*L[3]
		result = min(op1, op2)
		return result
	
	right = best_mat_mult_time(L[1:])
	left = best_mat_mult_time(L[:len(L)])

	if right < left: # 2 mats left
		return L[0]*L[1]*L[len[L]-1] + right
	else:
		return left + L[0]*L[len(L)-2]*L[len(L)-1]


print (best_mat_mult_time([100,10,100,10]))


# b

def best_mat_mult_time_fast(L):
	memo = {}
	return best_mat_mult_time_fast_with_memo(L,memo)


def best_mat_mult_time_fast_with_memo(L, memo):
	if (len(L)) == 4:  # when there are 3 mat left
		for i in range(len(L)):
			op1 = L[0]*L[1]*L[2] + L[0]*L[2]*L[3]
			op2 = L[1]*L[2]*L[3] + L[0]*L[1]*L[3]
		result = min(op1, op2)
		memo[L] = result
		return result

	right = best_mat_mult_time(L[1:])
	memo[L[1:]] = right
	left = best_mat_mult_time(L[:len(L)])
	memo[L[:len(L)]] = left

	if right < left: # 2 mats left
		return L[0]*L[1]*L[len[L]-1] + right
	else:
		return left + L[0]*L[len(L)-2]*L[len(L)-1]

# c


def best_mat_mult_order(L):
	pass  # replace this with your code


def mult_order_to_str(mult_order):
	if type(mult_order) is int:
		return str(mult_order)

	return f"({mult_order_to_str(mult_order[0])}) * ({mult_order_to_str(mult_order[1])})"


############
# QUESTION 3
############

# b
def had_local(n, i, j):
	pass  # replace this with your code


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
