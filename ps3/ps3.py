class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: string
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Problem 1 #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)
        return None



    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree

    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        # increase size by 1 for every node on access path
        self.size += 1
        if self.key is None:
            self.key = key
            self.size = 1
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        return self

    
    ####### Problem 2 #######

    '''
    Deletes a key from the tree
    Returns the root of the tree or None if the tree has no nodes   
    '''
    def delete(self, key):
        # create helper function to find max 
        def findmax(node): 
            current = node 
            while (current.right is not None): 
                current = current.right 
            return current

        # check to see if node is in the tree
        if self.search(key) is None:
            return self
        
        # decrease size by 1 for every node on access path
        def helper(self, key):
            if self is None: 
                return self
            
            self.size -= 1
            if key < self.key: 
                self.left = helper(self.left, key)
            elif key > self.key: 
                self.right = helper(self.right, key)
            else: 
                # nodes with one or zero children
                if self.left is None: 
                    return self.right 
                elif self.right is None: 
                    return self.left
                # nodes with two children, gotta rotate shebangalang
                else:
                    new = findmax(self.left)
                    new.right = self.right
                    new.left = helper(self.left, new.key)
                    new.size = self.size - 1
                    return new
            return self
        
        return helper(self, key)
    

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)

    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on

    Returns: the root of the tree/subtree

    Example:

    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10

    Output Graph
      10
        \
        12
        /
       11 
    '''

    def rotate(self, direction, child_side):
        # store sizes
        size_r = 0 if self.right is None else self.right.size
        size_l = 0 if self.left is None else self.left.size

        if direction == "L":
            if child_side == "R":
                # store sizes
                size_rr = self.right.right.size
                if self.right.right.left: 
                    size_rrl = self.right.right.left.size 
                else: 
                    size_rrl = 0

                # perform rotation 
                temp = self.right.right
                self.right.right = temp.left
                temp.left = self.right 
                self.right = temp

                # recalculate sizes 
                self.right.size = size_r
                self.right.left.size = size_r - size_rr + size_rrl
            else: #child_side == "L"
                # store sizes 
                size_lr = self.left.right.size 
                if self.left.right.left: 
                    size_lrl = self.left.right.left.size 
                else: 
                    size_lrl = 0

                # perform rotation
                temp = self.left 
                temp2 = self.left.right 
                temp.right = temp2.left 
                temp2.left = temp 
                self.left = temp2

                # recalculate sizes
                self.left.size = size_l
                self.left.left.size = size_l - size_lr + size_lrl
        else: #direction == "R"
            if child_side == "L": 
                # store sizes 
                size_ll = self.left.left.size 
                size_llr = 0 if self.left.left.right is None else self.left.left.right.size 

                # perform rotation
                temp = self.left.left 
                self.left.left = temp.right 
                temp.right = self.left 
                self.left = temp

                # recalculate sizes
                self.left.size = size_l 
                self.left.right.size = size_l - size_ll + size_llr
            else: # child_side == "R"
                # store sizes 
                size_rl = self.right.left.size
                size_rlr = 0 if self.right.left.right is None else self.right.left.right.size

                #perform rotation
                temp = self.right
                temp2 = self.right.left 
                temp.left = temp2.right
                temp2.right = temp 
                self.right = temp2

                # recalculate sizes
                self.right.size = size_r
                self.right.right.size = size_r - size_rl + size_rlr
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self

