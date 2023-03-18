from avltree import *
from algo1 import *
from linkedlist import *
from binarytree import *

class LinkedList:
  head=None
class AVLTree:
	root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

B = AVLTree()

"""insert(B,6,6)
insert(B,4,4)
insert(B,5,5)
insert(B,3,3)
insert(B,7,7)"""

"""insert(B,6,6)
insert(B,4,4)
insert(B,5,5)
insert(B,7,7)
insert(B,3,3)
insert(B,2,2)"""

insert(B,5,5)
insert(B,7,7)
insert(B,3,3)
insert(B,2,2)
insert(B,1,1)
current = B.root

