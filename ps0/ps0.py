#################
#               #
# Problem Set 0 #
#               #
#################



#
# Setup
#

class BinaryTree:
    # left : BinaryTree
    # right : BinaryTree
    # key : string
    # temp : int
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.temp = None



#
# Problem 1
#

# Sets the temp of each node in the tree T
# ... to the size of that subtree
def calculate_size(T):
    if T is None: 
        return 0
    else: 
        if T.temp: 
            return T.temp
        else:
            T.temp = calculate_size(T.left) + 1 + calculate_size(T.right)
            return T.temp


#
# Problem 3
#

# Outputs a subtree subT of T of size in the interval [L,U] 
# ... and removes subT from T by replacing the pointer 
# ... to subT in its parent with `None`
def FindSubtree(T : BinaryTree, L : int, U : int): 
    # Instructions:
    # Implement your Part 2 proof in O(n)-time
    # The return value is a subtree that meets the constraints

    # Your code goes here
    # populate temp 

    # check for None
    if T is None or (T.left is None and T.right is None): 
        return None

    calculate_size(T)

    if T.left: 
        if T.left.temp >= L and T.left.temp <= U: 
            subT = T.left 
            T.left = None 
            return subT 
        else: 
            return FindSubtree(T.left, L, U)
    else: 
        if T.right.temp >= L and T.right.temp <= U: 
            subT = T.right 
            T.right = None 
            return subT 
        else: 
            return FindSubtree(T.right, L, U)



