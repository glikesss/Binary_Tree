
'''

    func() -> None returns 0 if it completed succesfully or if input value is tecnically correct but meaningless it returns 1
'''

class Node:
    def __init__(self, value=None, parent=None, key=None, left=None, right=None):
        self.left   = left
        self.right  = right
        self.key    = key
        self.value  = value
        self.parent = parent


class Tree:
    def __init__(self, cmp_func):
        self.root_node = None
        self.cmp_func  = cmp_func


def create(cmp_func) -> Tree:
    if not callable(cmp_func):
        return None

    return Tree(cmp_func)


def clear(tree) -> None:
    ### 1-st variant (delete only brances, and root node)
    def clear_delete_branches(node):
        node.left  = None
        node.right = None

    if not isinstance(tree, Tree) and callable(func):
        return None
    temp_list = [True]                                            # List that stores path value (position and depth(by looking at its size-1))
    if tree.root_node != None:                                    # The last element is the direction of 'view' (future planned step)
        temp_node = tree.root_node
    else:
        return None

    while True:                         
        if temp_list[-1]:                                         # Check if last step was left
            if temp_node.left != None:                            # 
                temp_node = temp_node.left                        # Go left
                temp_list.append(True)                            # Add last step at the list end (there it's left)
                continue
            else:
                temp_list[-1] = False                             # Set last step to right
                continue

        else:                                                     
            if temp_node.right != None:                           # Check if it can go further
                temp_node = temp_node.right       
                temp_list.append(True)
            else:
                while not temp_list[-1] and len(temp_list) > 1:  # Go upper and execute the function (func) until 'view' isn't 'to the left'
                    clear_delete_branches(temp_node)
                    temp_node = temp_node.parent
                    temp_list.pop()
                if temp_list[-1]:                                 # Check if it can go on the right      
                    temp_list[-1] = False
                else:                                             # If current node is the root node
                    clear_delete_branches(temp_node)
                    break
    tree.root_node = None


def sizeof(tree) -> int:
    if not isinstance(tree, Tree):
        return -1
    size = [0]
    def count(value, key):
        size[0] += 1

    forall(tree, count)
    return size[0]


def insert(tree: Tree, value: any, key: any) -> None:
    if not isinstance(tree, Tree):
        return None

    node = Node(value=value, key=key)
    
    if tree.root_node == None:
            tree.root_node = node
            return None
    temp_node = tree.root_node


    while True:
        direction = tree.cmp_func(temp_node.key, key)
        if direction == -1:                         # go through the tree by checking tree.cmp_func condition
            if temp_node.left == None or temp_node.left.value == node.value:
                node.parent = temp_node
                temp_node.left = node
                break
            else:
                temp_node = temp_node.left
                continue
        elif direction == 1: 
            if temp_node.right == None or temp_node.right.value == node.value:
                node.parent = temp_node
                temp_node.right = node
                break
            else:
                temp_node = temp_node.right
                continue
        
        temp_node.value = value
        temp_node.key   = key
        return (temp_node.value, temp_node.key)

        
def delete(tree, key) -> any:
    if not isinstance(tree, Tree):
        return None
    if tree.root_node == None:
        return None

    temp_node = tree.root_node

    while key != temp_node.key:
        direction = tree.cmp_func(temp_node.key, key)
        if temp_node == None:
            return None
        
        if direction == -1:
            temp_node = temp_node.left
        elif direction == 1:
            temp_node = temp_node.right
        else:
            break

    if tree.root_node == temp_node:
        tree.root_node = None
        temp_value = temp_node.value
        temp_key   = temp_node.key
    else:
        if temp_node.parent.left == temp_node:
            temp_node.parent.left = None
        else:
            temp_node.parent.right = None

    temp_tree_left_node = Tree(tree.cmp_func)
    temp_tree_left_node.root_node = temp_node.left 
    temp_tree_right_node = Tree(tree.cmp_func)
    temp_tree_right_node.root_node = temp_node.right

    def temp_insert(temp_value, temp_key):
        insert(tree, temp_value, temp_key)
    
    forall(temp_tree_left_node , temp_insert)
    forall(temp_tree_right_node, temp_insert)

    return (temp_node.value, temp_node.key)


def forall(tree, func) -> None:
    if not isinstance(tree, Tree) and callable(func):
        return None
    temp_list = [True]                                            # List that stores path value (position and depth(by looking at its size-1))
    if tree.root_node != None:                                    # The last element is the direction of 'view' (future planned step)
        temp_node = tree.root_node
    else:
        return None

    while True:                         
        if temp_list[-1]:                                         # Check if last step was left
            if temp_node.left != None:                            # 
                temp_node = temp_node.left                        # Go left
                temp_list.append(True)                            # Add last step at the list end (there it's left)
                continue
            else:
                temp_list[-1] = False                             # Set last step to right
                continue

        else:                                                     
            if temp_node.right != None:                           # Check if it can go further
                temp_node = temp_node.right       
                temp_list.append(True)
            else:
                while not temp_list[-1] and len(temp_list) > 1:  # Go upper and execute the function (func) until 'view' isn't 'to the left'
                    if func(temp_node.value, temp_node.key):
                        return 0
                    temp_node = temp_node.parent
                    temp_list.pop()
                if temp_list[-1]:                                 # Check if it can go on the right      
                    temp_list[-1] = False
                else:                                             # If current node is the root node
                    if func(temp_node.value, temp_node.key):
                        return 0
                    return 0


###########################
#######  TEST AREA  ####### 
###########################


def main() -> None:
    def foo(value, key) -> any:
        return print(f"value = {value}  key = {key}")

    def cmp(key1, key2) -> bool:
        if key1 < key2:
            return -1
        return int(key1 > key2)
    tree = create(cmp)


    a = create(cmp)
    # insert(tree, value, key)
    insert(a, 1, 1)
    insert(a, 2, 2)
    insert(a, 3, 3)
    insert(a, 4, 4)
    insert(a, 5, 5)
    insert(a, 6, 6)
    insert(a, 7, 7)

    forall(a, foo)
    print(f"Size = {sizeof(a)}")

    print(f"Deleting (value=3)...")
    delete (a, 3)
    forall(a, foo)
    print("Deleted!")
    print(f"Size = {sizeof(a)}")

    print(f"Clearing...")
    clear(a)
    print(f"Size = {sizeof(a)}")

    forall(a, foo)

if __name__ == "__main__":
    main()
