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
	if L == []:
		return 0
	i = 1
	j = len(L)-1
	return M(L,i,j)
	
def M(L,i,j):
	if i == j:  # mat times itself
		return 0
	
	mini = "not assigned"
	current_check = 0
	for k in range (i,j):
		# recursive call for Ai-Ak+Ak-Aj w/ multipication of pair
		current_check = M(L, i, k) + M(L, k+1, j) + L[i-1]*L[k]*L[j]
		if mini == "not assigned": # first assign
			mini  = current_check
		elif current_check < mini:
			mini = current_check
	
	return mini
	
# b

def best_mat_mult_time_fast(L):
	if L == []:
		return 0
	memo = {}
	i = 1
	j = len(L)-1
	return M2(L, i, j, memo)

def M2(L, i, j, memo):
	
	if (i,j) in memo:
		return memo[(i,j)]
	if i == j:  # mat times itself
		memo[(i,j)] = 0
		return memo[(i, j)]

	memo[(i, j)] = "not assigned"
	current_check = 0
	for k in range(i, j):
		# recursive call for Ai-Ak+Ak-Aj w/ multipication of pair
		current_check = M2(L, i, k, memo) + M2(L, k+1, j, memo) + L[i-1]*L[k]*L[j]
		if memo[(i, j)] == "not assigned":  # first assign
			memo[(i, j)] = current_check
		elif current_check < memo[(i, j)]:
			memo[(i, j)] = current_check
	
	return memo[(i, j)]


def best_mat_mult_order(L):
	if L == []:
		return []
	memo = {}
	i = 1
	j = len(L)-1
	memo[(0,0)] = L
	return mult_order_to_str(M3(L, i, j, memo)[1])


def M3(L, i, j, memo):

	if (i, j) in memo:
		return memo[(i, j)]
	if i == j:  # mat times itself
		memo[(i, j)] = (0,i)
		return memo[(i, j)]

	memo[(i, j)] = "not assigned"
	current_check = 0
	for k in range(i, j):
		# recursive call for Ai-Ak+Ak-Aj w/ multipication of pair -- returns tuples
		sum_left, tree_left = M3(L, i, k, memo)
		sum_right, tree_right = M3(L, k+1, j, memo)
		current_check = sum_left + sum_right + L[i-1]*L[k]*L[j]
		if memo[(i, j)] == "not assigned" or current_check < memo[(i, j)][0]:
			memo[(i, j)] = (current_check, [tree_left, tree_right])

	return memo[(i, j)]

def mult_order_to_str(mult_order):
    if type(mult_order) is int:
        return str(mult_order)

    return f"({mult_order_to_str(mult_order[0])}) * ({mult_order_to_str(mult_order[1])})" 

print (best_mat_mult_order([10,100,10,100]))
############
# QUESTION 3
############

# b


def had_local(n, i, j):
	if n==0: # stop recursion at had(0)
		return 0
	
	if i <= (pow(2,n-1)-1) and j <= (pow(2,n-1)-1): #block 1
		return had_local(n-1, i, j)
	
	elif i <= (pow(2,n-1)-1) and j > (pow(2,n-1)-1):  # block 2
		return had_local(n-1, i, j-2**(n-1))
	
	elif i > (pow(2,n-1)-1) and j <= (pow(2,n-1)-1):  # block 2
		return had_local(n-1, i-2**(n-1), j)
	
	elif i > (pow(2,n-1)-1) and j > (pow(2,n-1)-1):  # block 4 (opposite matrix)
		if had_local(n-1,i-pow(2,n-1), j-pow(2,n-1)) == 0:
			return 1
		else:
			return 0
	

# d
def had_complete(n): 
	create_lst = lambda n : [[had_local(n, i, j) for j in range (pow(2, n))] for i in range (pow(2, n))]
	return create_lst(n)

############
# QUESTION 4
############

# a


def grid_escape1(B):
	if len(B)==1 and len(B[0])==1: # Mat with only one value
		return True
	
	if B == [] or B[0] == [] or B[0][0] == 0:  # end of rows/cols/can't move anywhere
		return False
		
	if ((B[0][0] == (len(B)-1)) and (len(B[0])==1)) or ((B[0][0] == (len(B[0])-1)) and (len(B)==1)):  # WIN in col or row
		return True
	
	if (B[0][0] > (len(B)-1)) and (B[0][0] > (len(B[0])-1)):  # exceeded row and col num 
		return False
	
	row_move = B[B[0][0]:]
	
	col_move = []
	for i in range (len(B)):
		col_move.append(B[i][B[0][0]:])
	
	return grid_escape1(row_move) or grid_escape1(col_move) #crop matrix

#print (grid_escape1([[1]]))
#print (grid_escape1([[0,2,3,1,1],[2,3,1,2,3],[1,3,2,2,3],[0,2,3,2,3]]))

# b
def grid_escape2(B):
	memo = []
	return grid_escape2_with_memo(B, 0, 0, memo)

def grid_escape2_with_memo(B, i, j, memo):
	memo.append((i, j))

	if i == len(B)-1 and j == len(B)-1:
		return True
	
	if B[i][j] == 0: # no moves
		return False
	
	if (j+B[i][j] >= len(B)) and (i+B[i][j] >= len(B)) and ((i-B[i][j], j) in memo) and ((i, j-B[i][j]) in memo): # no more moves
		return False
	
	up = False
	if (i+B[i][j] < len(B)) and (i+B[i][j], j) not in memo: # if not out of index/been there already
		up = grid_escape2_with_memo(B, i+B[i][j], j, memo)

	right = False
	if (j+B[i][j] < len(B)) and (i, j+B[i][j]) not in memo: # if not out of index/been there already
		right = grid_escape2_with_memo(B, i, j+B[i][j], memo)

	down = False
	if (i-B[i][j] >= 0) and (i-B[i][j], j) not in memo: # if not out of index/been there already
		down = grid_escape2_with_memo(B, i-B[i][j], j, memo)

	left = False
	if (j-B[i][j] >= 0) and (i, j-B[i][j]) not in memo:  # if not out of index/been there already
		left = grid_escape2_with_memo(B, i, j-B[i][j], memo)

	return up or right or down or left


############
# QUESTION 5
############

# a
def partition(S):
	P = []
	return partition_check(S, P)

def partition_check(S,P):
	if sum(P) > sum(S): # p will never be equal to s
		return None
	elif sum(P) == sum(S): # found it!
		return P
	for i in range (len(S)): 
		new_s = S.copy() # mutable
		new_s.pop(i)
		new_p = P.copy()  # mutable
		new_p.append(S[i])
		check = partition_check(new_s, new_p) # recursion
		if check != None: # if p was found, don't continue the loop
			return check
			
	return None

# b
def n_to_k(n, k):
	memo = {}
	return n_to_k_with_memo(n, k, memo)

def n_to_k_with_memo(n, k, memo):
	if n==k or k==1:
		return 1	
	if (n,k) not in memo:
		memo[(n,k)] = k * n_to_k_with_memo(n-1, k, memo) + n_to_k_with_memo(n-1, k-1, memo)
	return memo[(n,k)]


############
# QUESTION 6
############

def distance(s1, s2):  # s1 is what we want, s2 is what we have
	if s1 == s2: # done (even if they are both empty) -- O(1)
		return 0
	if s2 == "" and s1 != "":  # -- O(1)
		return len(s1) #add
	if s1 == "" and s2 != "":  # -- O(1)
		return len(s2) #remove
	if s1[0] == s2[0]: # continue to the next letter
		return distance(s1[1:],s2[1:]) # -- O(n)
	
	change = 1 + distance(s1[1:], s2[1:])  # -- O(n)
	add = 1 + distance(s1[1:], s2) # -- O(n)
	remove = 1 + distance(s1, s2[1:])  # -- O(n)
	return min(change, add, remove)  # -- O(1)


def distance_fast(s1, s2):
	memo = {}
	return distance_mem(s1,s2,memo)

def distance_mem(s1, s2, memo):  # s1 is what we want, s2 is what we have
	if s1 == s2:  # done (even if they are both empty) -- O(1)
		return 0
	if s2 == "" and s1 != "":  # -- O(1)
		return len(s1)  # add
	if s1 == "" and s2 != "":  # -- O(1)
		return len(s2)  # remove
	
	if (s1,s2) not in memo:
		if s1[0] == s2[0]:  # continue to the next letter
			memo[(s1, s2)] = distance_mem(s1[1:], s2[1:], memo)  # -- O(n)
			return memo[(s1, s2)]

		change = 1 + distance_mem(s1[1:], s2[1:], memo)  # -- O(n)
		add = 1 + distance_mem(s1[1:], s2, memo)  # -- O(n)
		remove = 1 + distance_mem(s1, s2[1:], memo)  # -- O(n)
		memo[(s1,s2)] = min(change, add, remove)  # -- O(1)
	return memo[(s1, s2)]


########
# Tester
########

def test():
	
	# Q2
	L1 = [100,10,100, 10]
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
	if(had_local(2,2,2) != 1):
		print("Error in had_local")
	# d
	if had_complete(1) != [[0,0],[0,1]]:
		print("Error in had_complete")

	  
	# Q4
	B1 = [[1,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,1,2]]
	B2 = [[2,3,1,2], [2,2,2,2], [2,2,3,2], [2,2,2,2]]
	B3 = [[2,1,2,1], [1,2,1,1], [2,2,2,2], [4,4,4,4]]

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
	

	#Q5
	# a
	if partition([3,1,1,2,2,1]) not in [[3,2],[2,3],[3,1,1],[1,3,1],[1,1,3],[1,1,1,2],[1,1,2,1],[1,2,1,1],[2,1,1,1],[1,2,2],[2,1,2],[2,2,1]]:
		print("Error in partition - 1")
	if partition([1,1,1]) is not None:
		print("Error in partition - 2")

	# b
	if n_to_k(4,2) != 7:
		print("Error in n_to_k")


	#Q6
	if distance('computer', 'commuter') != 1 or \
			distance('sport', 'sort') != 1 or \
			distance('', 'ab') != 2 or distance('kitten', 'sitting') != 3:
		print("Error in distance")

	if distance_fast('computer', 'commuter') != 1 or \
			distance_fast('sport', 'sort') != 1 or \
			distance_fast('', 'ab') != 2 or distance_fast('kitten', 'sitting') != 3:
		print("Error in distance_fast")
