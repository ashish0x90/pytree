
__author__ = "Ashish Yadav(ashish.nopc0de@gmail.com)"
__version__ = "1.0.0"

class Node(object):
    '''
    Class representing a member node
    '''
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node(Data = %s ,Left Node= %s ,Right Node = %s) <%s>'%(self.data,
                                                                      '%s <%s>'%(getattr(self.left,'data',None),
                                                                               hex(id(self.left))) if self.left else None ,
                                                                      '%s <%s>'%(getattr(self.right,'data',None),
                                                                               hex(id(self.right))) if self.right else None ,
                                                                      hex(id(self)))

class bTree(object):        
    '''
    Class representing a Simple Binary Tree
    There is really no use of using binary trees without effecient searching available,
    This class just represents how a binary tree should look like.
    '''
    def __init__(self,root_data):
        self.__key = 1
        self._root = Node(root_data)

    def getRoot(self):
        return self._root

    def setRoot(self,data):
        self._root = Node(data)

    def insert(self,data):
        raise NotImplementedError

    def delete(self,data):
        raise NotImplementedError

    
