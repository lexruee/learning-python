# -*- coding: utf-8 -*-

__author__ = "Alexander Rüedlinger"


from hashlib import sha256
from graphviz import Digraph

class Visitor(object):
    
    def __init__(self):
        self._level = 0
        self.stack = []

    def visit_node(self, node):
        self.stack.append(node)
        lnode = node.left
        rnode = node.right
        if lnode:
            self._level += 1        
            self.visit_lnode(lnode)
            lnode.accept(self)
            self._level -= 1        
        
        if rnode:
            self._level += 1        
            self.visit_rnode(rnode)
            rnode.accept(self)
            self._level -= 1        
        self.stack.pop()

    def visit_lnode(self, node):
        pass

    def visit_rnode(self, node):
        pass


class PrintVisitor(Visitor):

    def __init__(self):
        super().__init__()
        self.graph = Digraph(name='MerkleTree', comment='MerkleTree')

    def _short_hash(self, node):
        return 

    def visit_node(self, node):
        h = node.hash[:5]
        if node.is_leaf():
            self.graph.node(node.hash, 'hash: {}, data: {}'.format(h, node.data))
        else:
            self.graph.node(node.hash, 'hash: {}'.format(h))
        super().visit_node(node)

    def visit_lnode(self, node):
        p = self.stack[-1]
        self.graph.edge(p.hash, node.hash)

    def visit_rnode(self, node):
        p = self.stack[-1]
        self.graph.edge(p.hash, node.hash)


class Node(object):

    def __init__(self, data=None):
        self._left = None
        self._right = None
        self._hash = None
        self.data = data

    def accept(self, visitor):
        visitor.visit_node(self)

    def _compute_hash(self):
        if self.is_leaf():
            s = str(self._data)
            self._hash = sha256(bytes(s, 'utf-8')).hexdigest()
        else:
            lh = self._left.hash if self._left else ''
            rh = self._right.hash if self._right else ''
            self._hash = sha256(bytes(lh + rh, 'utf-8')).hexdigest()

    def is_leaf(self):
        return self._data is not None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self._compute_hash()

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value
        self._compute_hash()

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
        self._compute_hash()

    @property
    def hash(self):
        return self._hash

    def __str__(self):
        return '<Node(hash={}, data={})>'.format(self.hash, self._data)

    __repr__ = __str__

