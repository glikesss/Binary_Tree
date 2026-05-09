import bin_tree as bn
# Creation

def CREATE_EMPTY_TREE():
    def cmp(a, b):
        return True
    tree = bn.create(cmp)
    return True if isinstance(tree, bn.Tree) else False

# Size count
def SIZE_EMPTY_TREE():
    tree = bn.Tree(None)
    return bn.sizeof(tree) == 0


def SIZE_ONE_ELEMENT_TREE():
    def cmp(node, a):
        return bool((node.value & node.key) % 2)

    tree = bn.Tree(cmp)
    bn.insert(tree, (2**2)&(1**3), 6&(2**3))
    return bn.sizeof(tree) == 1


def SIZE_FIVE_ELEMENT_TREE():
    def cmp(node, a):
        return True

    tree = bn.Tree(cmp)
    bn.insert(tree, 1, 1)
    bn.insert(tree, 2, 2)
    bn.insert(tree, 3, 3)
    bn.insert(tree, 4, 4)
    bn.insert(tree, 5, 5)
    return bn.sizeof(tree) == 5

# Insertion
def INSERT_ONE_ELEMENT_TREE():
    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)

    tree = bn.Tree(cmp)
    bn.insert(tree, (2**2)&(1**3), 6&(2**3))
    return True if isinstance(tree.root_node, bn.Node) else False


def INSERT_FIVE_ELEMENT_TREE():
    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)

    tree = bn.Tree(cmp)
    for i in range(5):
        bn.insert(tree, i, i)

    return bn.sizeof(tree) == 5


def INSERT_RETURN_REPLACED_DATA():
    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)

    tree = bn.Tree(cmp)
    bn.insert(tree, 2, 2)
    return bn.insert(tree, 2, 2) == (2,2)

# Deletion
def DELETE_EMPTY_TREE():
    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)

    tree = bn.Tree(cmp)
    return bn.delete(tree, 3) == None

def DELETE_ONE_NODE_TREE():
    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)

    tree = bn.Tree(cmp)
    bn.insert(tree, 1, 1)
    return bn.delete(tree, 1) == (1, 1)


def DELETE_LAST_NODE_TREE():
    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)

    tree = bn.Tree(cmp)
    bn.insert(tree, 1, 1)
    bn.insert(tree, 2, 2)
    return bn.delete(tree, 2) == (2, 2)
    

def DELETE_MIDDLE_NODE_TREE():
    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)

    tree = bn.Tree(cmp)
    bn.insert(tree, 4, 4)
    bn.insert(tree, 2, 2)
    bn.insert(tree, 3, 3)
    bn.insert(tree, 1, 1)
    bn.delete(tree, 2)
    return bn.sizeof(tree) == 3

# Forall func test
def FORALL_EMPTY_TREE_TEST():
    def foo(value, key):
        pass
    tree = bn.Tree(None)
    
    return bn.forall(tree, foo) == None



def FORALL_ORDER_TEST():
    def cmp(key1, key2) -> bool:
        if key1 > key2:
            return -1
        return int(key1 < key2)

    tree = bn.Tree(cmp)
    bn.insert(tree, 4, 4)
    bn.insert(tree, 2, 2)
    bn.insert(tree, 3, 3)
    bn.insert(tree, 1, 1)
    tree_out = []
    def get_tree(value, key):
        tree_out.append(key)
    bn.forall(tree, get_tree)
    return tree_out == [1,3,2,4]


def RUN_ALL_TESTS():
    tests = [CREATE_EMPTY_TREE, SIZE_EMPTY_TREE, SIZE_ONE_ELEMENT_TREE, SIZE_FIVE_ELEMENT_TREE,
    INSERT_ONE_ELEMENT_TREE, INSERT_FIVE_ELEMENT_TREE, DELETE_EMPTY_TREE, DELETE_LAST_NODE_TREE, DELETE_MIDDLE_NODE_TREE,
    DELETE_ONE_NODE_TREE, FORALL_EMPTY_TREE_TEST, FORALL_ORDER_TEST]
    counter = 0
    for is_test_passed in tests:
        passed = is_test_passed()
        print(f"{is_test_passed.__name__}: {"PASSED" if passed else "INVALID"}")
        if passed:
            counter += 1
    print(f"Passed tests:  {counter}")
    print(f"Invalid tests: {len(tests) - counter}")

if __name__ == "__main__":
    RUN_ALL_TESTS()