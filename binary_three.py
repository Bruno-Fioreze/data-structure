# Programação Dinâmica - Estruturas de Dados
# Implementação de Árvores e seus algoritmos - by hallpaz
# https://youtube.com/programacaodinamica

from queue import Queue


ROOT = "root"
# Implementando uma Árvore Binária: https://youtu.be/6E169kShoNU
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percurso em ordem simétrica (o correto é "inorder" em inglês)
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            # parênteses são específicos para o nosso exemplo,
            # um percurso em ordem simétrica não precisa deles
            print('(', end='') 
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
    
    # Percurso em PÓS ORDEM em ÁRVORE BINÁRIA: https://youtu.be/QC8oiQnlYos
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    # Percurso em Nível em Árvore Binária: https://youtu.be/UOK7nS2E9xM
    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")