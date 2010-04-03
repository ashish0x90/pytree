__author__ = "Ashish Yadav(ashish.nopc0de@gmail.com)"
__version__ = "1.0.0"

'''
ToDo's:: 
1)Replace current recursive traversal with iterative traversal.
2)Replace existing display() method to display tree in a tree like structure, you know with arcs and stuff..
3)implement appropriate function so that tree be serialized using pickle lib.
4)Write a unit test plan.
'''



from btree import Node,bTree
from operator import xor

class BSearchTree(bTree):
    '''
    A class representing a binarySearchTree.
    
    Example UseCase:

    from pytree.bsearchtree import BSearchTree
    tree_inst = BSearchTree(12) #root node
    tree_inst.insert(20) #couple of inserts
    tree_inst.insert(10)
    tree_inst.insert(50)
    tree_inst.insert(5)
    print tree_inst #display tree
    tree_inst.delete(10) #delete something
    print tree_inst #display tree again

    '''
    __nodes = []

    def __getSuccessor(self,delnode):
        """
        Gets inOrder Successor of a node to be deleted.
        used in deletion of a node which has both the child nodes

        Possible Candidates:
        1)Left leaf node of left subtree of right node child of node to be deleted
        2)Right node of node to be deleted,if it doesn't have a left child        
        """

        if not delnode.right.left:
            if delnode.right.right:
                setattr(delnode.right,'right',delnode.right.right) #make necessary adjustments
            return delnode.right
        else:
            current = delnode.right.left
            parent = delnode.right
            while current.left:
                parent = current
                current = current.left
            
            #before removing this node, take care of it's right child if any
            setattr(parent,'left' ,current.right)
            setattr(current,'right',delnode.right)
            return current

    def __getParentChildReference(self,parent,child):
        '''
        It returns the parent node's reference to one of it's child,
        Or if the child is it's left or right child node
        '''
        if hasattr(parent,'_root'): #if it's a tree(root node), handle it differently
            return "_root"
        elif parent.right == child:
            return "right"
        elif parent.left == child:
            return "left"
        
    def _inOrder(self,node):
        """
        Return nodes in increasing order of their node data a.k.a inorder traversal,
        which is left_node,root,right_node
        """
        if hasttr(node,'left'):
            self._inOrder(node.left) #go left
        if node:
            self.__nodes.append(node) #append root
        if hasattr(node,'right'):
            self._inOrder(node.right) #go right

    def _preOrder(self,node):
        """
        Return nodes in preorder fashion a.k.a Preorder traversal or Depth First traversal
        """
        if node:
            self.__nodes.append(node) #append root
        if hasattr(node,'left'):
            self._preOrder(node.left) #go left
        if hasattr(node,'right'):
            self._preOrder(node.right) #go right

    def getIterator(self,root=None,iterate = '_inOrder'):
        '''
        Follow InOrder tree traversal(default) starting from the given root
        iterator :: _inOrder,_preOrder
        '''
        if not root:
            root = self.getRoot()
        self.__nodes = []
        getattr(self,iterate)(root)
        return self.__nodes
            
    def find(self,data,return_parent=False):
        """
        if a matching Node found: Returns Matching node
        if return_parent is True, returns tuple (matching_node,parent_node)
        """
        current = self.getRoot()
        parent=self
        while current:
            if current.data == data: 
                break
            elif data > current.data: 
                parent = current
                current =  current.right #go right
            elif data < current.data: 
                parent = current
                current =  current.left #go left
        
        if return_parent:
            return parent,current
        else:
            return current

    def findall(self,data,return_parent=False):
        """
        Similar to find, but returns all the matching nodes (optionally their parents)
        if a matching Node found: Returns Matching node
        if return_parent is True, returns tuple (matching_node,parent_node)
        """
        ret = []
        current = self.getRoot()
        parent=self
        while current:
            if current.data == data: 
                ret.append([parent,current])
                parent = current
                current = current.right #All the matching nodes will be at the right sub-tree
            elif data > current.data: 
                parent = current
                current =  current.right #go right
            elif data < current.data: 
                parent = current
                current =  current.left #go left

        if return_parent:
            return ret
        else:
            return [each[-1] for each in ret]

    def insert(self,data):
        '''
        Inserts a new node.
        '''
        if not self.getRoot(): #if tree is empty, create root first
            self.setRoot(data)
        else:
            parent,match_node = self.find(data,return_parent=True) 
            node = Node(data)
            if match_node: #if duplicate key is present
                node.right = match_node.right #shift existing twin's node right subtree as new node's right subtree
                match_node.right = node #Insert twin node as existing twin node's right child
            elif data > parent.data: #node to be parent's right child
                assert(not parent.right)
                parent.right = node
            elif data < parent.data: #node to be parent's right child
                assert(not parent.left)
                parent.left = node
    
    def delete(self,data):
        '''
        Now the complex stuff ;), Node Deletion..

        We have to consider three different types of cases here:-
        i)Deleting a node with no child 
        ii)Deleting a node with one child
        iii)Deleting a node with both the childs ->yeah this is the complex one!!
        
        Also setting the nodes explicitely None, so that they can be garbage collected
        '''
        parent,node = self.find(data,True)
        if not node:
            raise Exception('None of the matching nodes were found to be deleted')

        parent_node_dir = self.__getParentChildReference(parent,node)

        #case i)
        if not (node.right or node.left):
            setattr(parent,parent_node_dir,None)
            del node                 #just delete this node, that's all

        #case ii)
        elif xor(bool(node.right),bool(node.left)):
            if node.right: #Node to be deleted only has the right child
                setattr(parent,parent_node_dir,node.right) #shift node.right subtree to it's parent
            else:
                setattr(parent,parent_node_dir,node.left) #shift node.left subtree to it's parent
            del node 

        #case iii)
        else:  #have Both the child nodes
            successor_node = self.__getSuccessor(node)
            setattr(parent,parent_node_dir,successor_node)
            setattr(successor_node,'left',node.left)
            del node

    def testInst(self):
        tree_inst = BSearchTree(12) #node
        tree_inst.insert(20)
        tree_inst.insert(10)
        tree_inst.insert(50)
        tree_inst.insert(5)
        tree_inst.insert(10)
        tree_inst.insert(13)
        tree_inst.insert(15)
        return tree_inst
            
