class Tree:
    def __init__(self, cmp_func):
        self.cmp_func = cmp_func
        self.root_node = None


class Node:
    def __init__(self, value, key):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.height = 1


def create(cmp_func):
    if callable(cmp_func):
        return Tree(cmp_func)
    else:
        return None


def insert(tree, value, key):
    if not isinstance(tree, Tree): return None
    if tree.root_node == None:
        tree.root_node = Node(value, key)
        return None

    def insert_node(node, value, key, cmp_func):
        if node == None:
            return Node(value, key), None
        direction = cmp_func(key, node.key)
        r = None
        if direction == -1:
            t = insert_node(node.left, value, key, cmp_func)
            node.left, r = t[0], t[1]
        elif direction == 1:
            t = insert_node(node.right, value, key, cmp_func)
            node.right, r = t[0], t[1]
        
        elif direction == 0:
            r = node.value
            node.value = value
            node.key   = key
            return node, r

        # Balansing

        node.height = 1 + max(get_height(node.left), get_height(node.right))
        balance = get_balance(node)

        if tree.root_node == node:
            if   balance > 1: tree.root_node = node.left
            elif balance < -1: tree.root_node = node.right

        # Left Left
        if balance > 1 and get_balance(node.left) >= 0:
            return right_rotate(node), r

        # Left Right
        if balance > 1 and get_balance(node.left) < 0:
            node.left = left_rotate(node.left)
            return right_rotate(node), r

        # Right Right
        if balance < -1 and get_balance(node.right) <= 0:
            return left_rotate(node), r

        # Right Left
        if balance < -1 and get_balance(node.right) > 0:
            node.right = right_rotate(node.right)
            return left_rotate(node), r
                    
        return node, r




    return insert_node(tree.root_node, value, key, tree.cmp_func)[1]


                                      


def right_rotate(node):
    temp_node1 = node.left
    temp_node2 = temp_node1.right

    node.left = temp_node2
    temp_node1.right = node
    node.height = 1 + max(get_height(node.left), get_height(node.right))

    temp_node1.height = 1 + max(get_height(temp_node1.left), get_height(temp_node1.right))

    return temp_node1

def left_rotate(node):
    temp_node1 = node.right
    temp_node2 = temp_node1.left

    node.right = temp_node2
    temp_node1.left = node

    node.height = 1 + max(get_height(node.left),
                          get_height(node.right))

    temp_node1.height = 1 + max(get_height(temp_node1.left),
                                get_height(temp_node1.right))

    return temp_node1


def get_height(node):
    if not node:
        return 0
    return node.height
    

def get_balance(node):
    return get_height(node.left) - get_height(node.right) 


def foreach(tree, func):
    if not isinstance(tree, Tree):
        return None
    if tree.root_node is None:
        return None

    def foreach_node(node, func):
        if node.left != None:
            foreach_node(node.left, func)
        if node.right != None:
            foreach_node(node.right, func)
        func(node)

    foreach_node(tree.root_node, func)


def delete(tree, key):
    if not isinstance(tree, Tree):
        return None

    if tree.root_node is None:
        return None

    def delete_node(node, key, cmp_func):


        if node is None:
            return node, None
        r = None
        direction = cmp_func(key, node.key)

        if direction == -1:
            node.left,  r = delete_node(node.left, key, cmp_func)
        elif direction == 1:
            node.right, r = delete_node(node.right, key, cmp_func)
        elif direction == 0:
            if node.left is None:
                temp = node.right
                r = node.value
                node = None
                return temp, r
            elif node.right is None:
                temp = node.left
                r = node.value
                node = None
                return temp, r
            
            r = node.value
            temp = min_value_node(node.right)
            node.value = temp.value
            node.right = delete_node(node.right, temp.value, cmp_func)[0]
        return node, r

    if tree.root_node.key == key:
        temp_node = Node(None, None)
        temp_node.left = tree.root_node
        temp_node.left, r = delete_node(temp_node.left, key, tree.cmp_func) 
        tree.root_node = temp_node.left
        return r

    return delete_node(tree.root_node, key, tree.cmp_func)[1]


def min_value_node(node):
    temp_node = node
    while temp_node.left is not None:
        temp_node = temp_node.left
    return temp_node


def clear(tree):
    if not isinstance(tree, Tree): return None
    if tree.root_node == None:
        return 0
    def clear_node(node):
        if node.left != None:
            clear_node(node.left)
        if node.right != None:
            clear_node(node.right)
        
        node.left = None
        node.right = None
        node = None

    clear_node(tree.root_node)
    tree.root_node = None

def sizeof(tree):
    if not isinstance(tree, Tree): return -1
    if tree.root_node == None:
        return 0
    def size_node(node):
        size = 1
        if node.left != None:
            size += size_node(node.left)
        if node.right != None:
            size += size_node(node.right)
        else:
            return 1
        return size

    return size_node(tree.root_node)
 

def find(tree, key):
    if not isinstance(tree, Tree): return -1
    if tree.root_node == None:
        return None
    def find_node(node, key):
        res = None
        if node.left != None:
            res = find_node(node.left, key)
        if node.right != None and res == None:
            res = find_node(node.right, key) 
        if node.key == key:
            res = node.value 
        return res
    return find_node(tree.root_node, key)

def main():
    def cmp_func(key1, key2):
        if key1 < key2: return -1
        return int(key1 > key2)

    a = create(cmp_func)

    for i in range(7):
        insert(a, i, i)
    
    def print_all(node):
        print(node.value)

    foreach(a, print_all)
    print(f"________________________")
    print(f"Size {sizeof(a)}")
    print(f"________________________")
    print(f"DELETED: {delete(a, 3)}")
    foreach(a, print_all)
    print(f"________________________")
    print(f"Size {sizeof(a)}")
    print(f"Node founded {find(a, 1)}")
    clear(a)
    print(f"________________________")
    print(f"Size {sizeof(a)}")
    print(f"________________________")



if __name__ == "__main__":
    main()
