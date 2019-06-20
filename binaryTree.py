class binaryTree:    

    """ Constructor class for a binary tree """

    def __init__(self, element):
        self.root = element
        self.left = None
        self.right = None
        print("Element method init")
        print(element)

    """ Method for insert left node or new value """

    def setLeft(self,node):
        if self.left == None:
           self.left = binaryTree(node)
           print("new Node setLeft Method --------------")
           print (node)
        else:
            l_instance = binaryTree(node)
            l_instance.left = self.left
            self.left = l_instance
            print("new child setLeft Method --------------")
            print (node)
    
    """ Method for set Right node or new value """
    
    def setRight(self, node):
        if self.right == None:
           self.right = binaryTree(node)
           print("New node  in setRight Method------------")
           print(node)
        else:
            r_instance = binaryTree(node)
            r_instance =self.right
            self.right = r_instance
            print("New child in setRight Method -----------")
            print(node)
    
    def getRightChild(self):
        print("Get Right child--------------------")
        print(self.right)
        return self.right
    
    def getLeftChild(self):
        print("Get Left child--------------------")
        print(self.left)
        return self.left

    def setRoot(self,obj):
        self.root = obj
    
    def getRoot(self):
        return self.root


x = binaryTree(1)
print(x.getRoot())
print(x.setLeft(3))
print(x.setRight(2))

