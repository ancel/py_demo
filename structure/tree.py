from abc import ABCMeta,abstractclassmethod,abstractmethod

class Node(object):
    """docstring for Node"""
    def __init__(self, data):
        super(Node, self).__init__()
        self.__data = data
        self.__parent = None
        self.__children = []

    def add_child(self, child):
        child.parent = self
        self.__children.append(child)

    def is_leaf(self):
        if None==self.__children or len(self.__children)==0:
            return True
        return False

    @property
    def data(self):
        return self.__data

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def children(self):
        return self.__children

        
class StorageNode(Node):
    """docstring for StorageNode"""
    def __init__(self, data):
        super(StorageNode, self).__init__(data)
        self.__cache = dict()

    def save(self, key, value):
        self.__cache[key] = value

    def contain(self, key):
        if key in self.__cache:
            return True
        return False
        
    def delete(self, key):
        del self.__cache[key]

    def pop(self, key):
        return self.__cache.pop(key)

    def get(self, key):
        return self.__cache[key]

    def clear(self):
        self.__cache.clear()

class ProcessNode(Node):
    """docstring for ProcessNode"""
    def __init__(self, data):
        super(ProcessNode, self).__init__(data)

    def process(self, obj):
        return False, None

class Tree(object):
    """docstring for Tree"""
    def __init__(self, root):
        super(Tree, self).__init__()
        self.__root = root

    @property
    def root(self):
        return self.__root

    def s_print(self):
        self._print(self.__root)

    def _print(self, node, level=0):
        print("-"*level+node.data)
        level += 1
        for child in node.children:
            self._print(child, level)


class Forest(object):
    """docstring for Forest"""
    def __init__(self):
        super(Forest, self).__init__()
        self.__trees = []

    def add_tree(self, tree):
        self.__trees.append(tree)

    @property
    def trees(self):
        return self.__trees

    def s_print(self):
        for tree in self.__trees:
            tree.s_print()

class ForestParser(object):
    """docstring for ForestParser"""
    def __init__(self, expression):
        super(ForestParser, self).__init__()
        self.expression = expression
        

    def get_node(self, node_id):
        return Node(node_id)

    def get_forest(self):
        roots = []
        root = Node('root')
        roots.append(root)
        self.parse_nodes(self.expression, roots)
        forest = Forest()
        for tree_root in root.children:
            tree_root.parent = None
            forest.add_tree(Tree(tree_root))

        return forest

    """
        将一个字符串解析为forest，
        例如1-[2-[3-4,5]-6-7,8-10,9],表达的树形结构如下
        1
        -2
        --3
        ---4
        ----6
        -----7
        --5
        ---6
        ----7
        -8
        --10
        -9
        解析方式
        1、先按逗号解析所有子表达式
        2、所有字表达式按短杠解析各链表表达式并串联
        3、各链表表达式调用本方法递归进行解析，直到解析到数字id为止
    """
    
    def parse_nodes(self, expression, nodes):
        if expression.startswith('[') and expression.endswith(']'):
            expression = expression[1:-1] 
        if ''==expression:
            return None
        if expression.isdigit():
            child_node = self.get_node(expression)
            child_nodes = []
            child_nodes.append(child_node)
            for node in nodes:
                node.add_child(child_node)
            return child_nodes

        child_expressions = []
        child_expression_stack = []
        middle_backet_stack = []
        for c in iter(expression):
            if ','==c and len(middle_backet_stack)==0:
                child_expressions.append("".join(child_expression_stack))
                child_expression_stack.clear()
                continue
            if '['==c:
                middle_backet_stack.append(c)
            elif ']'==c:
                middle_backet_stack.pop()
            child_expression_stack.append(c)
        if len(child_expression_stack)>0:
            child_expressions.append("".join(child_expression_stack))

        children_nodes = []
        for child_expression in child_expressions:
            expression_stack = []
            middle_backet_stack = []
            current_nodes = nodes
            for c in iter(child_expression):
                if '-'==c and len(middle_backet_stack)==0:
                    current_nodes = self.parse_nodes("".join(expression_stack), current_nodes)
                    expression_stack.clear()
                    continue
                if '['==c:
                    middle_backet_stack.append(c)
                elif ']'==c:
                    middle_backet_stack.pop()
                expression_stack.append(c)
            if len(expression_stack)>0:
                current_nodes = self.parse_nodes("".join(expression_stack), current_nodes)
                expression_stack.clear()
            children_nodes = children_nodes+current_nodes
        return children_nodes
        

        

class SimpleNode(Node):
    """docstring for SimpleNode"""
    def __init__(self, data):
        super(SimpleNode, self).__init__(data)

    def process(self, msg):
        if self.data=='root' or self.data=='second_2' or self.data=='third_2':
            return True, msg
        return False, None

        

if __name__ == '__main__':
    expression = '1-[2-[3-4,5]-6-7,8-10,9]'
    # tree_s = '1-2,3,4'
    root_node = Node('root')
    forest_parser = ForestParser(expression)
    forest = forest_parser.get_forest()
    forest.s_print()
