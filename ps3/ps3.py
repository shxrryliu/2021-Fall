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
        if BinarySearchTree.search(self, key) is None:
            return self
        
        # decrease size by 1 for every node on access path
        self.size -= 1

        if key < self.key: 
            self.left = self.left.delete(key)
        elif key > self.key: 
            self.right = self.right.delete(key)
        else: 
            # nodes with one or zero children
            if self.left is None: 
                self = self.right 
                return self 
            elif self.right is None: 
                self = self.left 
                return self
            # nodes with two children, gotta rotate shebangalang
            else:
                temp = findmax(self.left)
                self.key = temp.key 
                self.left = self.left.delete(temp.key)
        return self

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
    
    Execute: NodeFor10.rotate("R", "L") -> Outputs: NodeFor10

    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if direction == "R": 
            if child_side == "L":
                temp = self.left.right
                self.right = self 
                self.left = temp
                return self
            else:
                return 
        else: 
            return
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self

