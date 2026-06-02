import bin_tree_rec as bn


def CMP(key1, key2):
    if key1 < key2:
        return -1
    return int(key1 > key2)


# =========================
# CREATE TESTS
# =========================

def TEST_CREATE_VALID_FUNC():
    tree = bn.create(CMP)

    return isinstance(tree, bn.Tree)


def TEST_CREATE_INVALID_FUNC():
    return bn.create(123) is None


# =========================
# INSERT TESTS
# =========================

def TEST_INSERT_IN_EMPTY_TREE():
    tree = bn.create(CMP)

    bn.insert(tree, "A", 1)

    return bn.find(tree, 1) == "A"


def TEST_INSERT_SEVERAL_ELEMENTS():
    tree = bn.create(CMP)

    for i in range(10):
        bn.insert(tree, i, i)

    result = True

    for i in range(10):
        result &= (bn.find(tree, i) == i)

    return result


def TEST_INSERT_REPLACE_EXISTING():
    tree = bn.create(CMP)

    bn.insert(tree, "OLD", 1)

    replaced = bn.insert(tree, "NEW", 1)

    return (
        replaced == "OLD" and
        bn.find(tree, 1) == "NEW"
    )


def TEST_INSERT_INVALID_TREE():
    return bn.insert(123, "A", 1) is None


def TEST_INSERT_LEFT_ROTATION():
    tree = bn.create(CMP)

    bn.insert(tree, 1, 1)
    bn.insert(tree, 2, 2)
    bn.insert(tree, 3, 3)

    return (
        bn.find(tree, 1) == 1 and
        bn.find(tree, 2) == 2 and
        bn.find(tree, 3) == 3 and
        bn.sizeof(tree) == 3
    )


def TEST_INSERT_RIGHT_ROTATION():
    tree = bn.create(CMP)

    bn.insert(tree, 3, 3)
    bn.insert(tree, 2, 2)
    bn.insert(tree, 1, 1)

    return (
        bn.find(tree, 1) == 1 and
        bn.find(tree, 2) == 2 and
        bn.find(tree, 3) == 3 and
        bn.sizeof(tree) == 3
    )


# =========================
# FIND TESTS
# =========================

def TEST_FIND_EXISTING_VALUE():
    tree = bn.create(CMP)

    bn.insert(tree, "VALUE", 10)

    return bn.find(tree, 10) == "VALUE"


def TEST_FIND_NON_EXISTING_VALUE():
    tree = bn.create(CMP)

    bn.insert(tree, "VALUE", 10)

    return bn.find(tree, 100) is None


def TEST_FIND_EMPTY_TREE():
    tree = bn.create(CMP)

    return bn.find(tree, 1) is None


def TEST_FIND_INVALID_TREE():
    return bn.find(123, 1) == -1


# =========================
# DELETE TESTS
# =========================

def TEST_DELETE_FROM_EMPTY_TREE():
    tree = bn.create(CMP)

    return bn.delete(tree, 1) is None


def TEST_DELETE_ROOT():
    tree = bn.create(CMP)

    bn.insert(tree, "ROOT", 1)

    deleted = bn.delete(tree, 1)

    return (
        deleted == "ROOT" and
        bn.find(tree, 1) is None and
        bn.sizeof(tree) == 0
    )


def TEST_DELETE_LEAF():
    tree = bn.create(CMP)

    bn.insert(tree, 1, 1)
    bn.insert(tree, 2, 2)

    deleted = bn.delete(tree, 2)

    return (
        deleted == 2 and
        bn.find(tree, 2) is None and
        bn.find(tree, 1) == 1 and
        bn.sizeof(tree) == 1
    )


def TEST_DELETE_MIDDLE_ELEMENT():
    tree = bn.create(CMP)

    for i in range(5):
        bn.insert(tree, i, i)

    deleted = bn.delete(tree, 2)

    return (
        deleted == 2 and
        bn.find(tree, 2) is None and
        bn.find(tree, 0) == 0 and
        bn.find(tree, 1) == 1 and
        bn.find(tree, 3) == 3 and
        bn.find(tree, 4) == 4 and
        bn.sizeof(tree) == 4
    )


def TEST_DELETE_NON_EXISTING():
    tree = bn.create(CMP)

    for i in range(5):
        bn.insert(tree, i, i)

    return bn.delete(tree, 100) is None


def TEST_DELETE_INVALID_TREE():
    return bn.delete(123, 1) is None


# =========================
# FOREACH TESTS
# =========================

def TEST_FOREACH_EMPTY_TREE():
    tree = bn.create(CMP)

    result = []

    def collect(node):
        result.append(node.value)

    bn.foreach(tree, collect)

    return len(result) == 0


def TEST_FOREACH_ALL_ELEMENTS():
    tree = bn.create(CMP)

    for i in range(5):
        bn.insert(tree, i, i)

    result = []

    def collect(node):
        result.append(node.value)

    bn.foreach(tree, collect)

    return set(result) == {0, 1, 2, 3, 4}


def TEST_FOREACH_INVALID_TREE():
    def foo(node):
        pass

    return bn.foreach(123, foo) is None


# =========================
# SIZE TESTS
# =========================

def TEST_SIZE_EMPTY_TREE():
    tree = bn.create(CMP)

    return bn.sizeof(tree) == 0


def TEST_SIZE_ONE_ELEMENT():
    tree = bn.create(CMP)

    bn.insert(tree, 1, 1)

    return bn.sizeof(tree) == 1


def TEST_SIZE_SEVERAL_ELEMENTS():
    tree = bn.create(CMP)

    for i in range(10):
        bn.insert(tree, i, i)

    return bn.sizeof(tree) == 10


def TEST_SIZE_INVALID_TREE():
    return bn.sizeof(123) == -1


# =========================
# RUN ALL TESTS
# =========================

def RUN_ALL_TESTS():

    tests = [

        # CREATE
        TEST_CREATE_VALID_FUNC,
        TEST_CREATE_INVALID_FUNC,

        # INSERT
        TEST_INSERT_IN_EMPTY_TREE,
        TEST_INSERT_SEVERAL_ELEMENTS,
        TEST_INSERT_REPLACE_EXISTING,
        TEST_INSERT_INVALID_TREE,
        TEST_INSERT_LEFT_ROTATION,
        TEST_INSERT_RIGHT_ROTATION,

        # FIND
        TEST_FIND_EXISTING_VALUE,
        TEST_FIND_NON_EXISTING_VALUE,
        TEST_FIND_EMPTY_TREE,
        TEST_FIND_INVALID_TREE,

        # DELETE
        TEST_DELETE_FROM_EMPTY_TREE,
        TEST_DELETE_ROOT,
        TEST_DELETE_LEAF,
        TEST_DELETE_MIDDLE_ELEMENT,
        TEST_DELETE_NON_EXISTING,
        TEST_DELETE_INVALID_TREE,

        # FOREACH
        TEST_FOREACH_EMPTY_TREE,
        TEST_FOREACH_ALL_ELEMENTS,
        TEST_FOREACH_INVALID_TREE,

        # SIZE
        TEST_SIZE_EMPTY_TREE,
        TEST_SIZE_ONE_ELEMENT,
        TEST_SIZE_SEVERAL_ELEMENTS,
        TEST_SIZE_INVALID_TREE
    ]

    passed_counter = 0

    for test in tests:

        try:
            passed = test()

        except Exception:
            passed = False

        print(f"{test.__name__}: {'PASSED' if passed else 'FAILED'}")

        if passed:
            passed_counter += 1

    print()
    print(f"Passed tests: {passed_counter}")
    print(f"Failed tests: {len(tests) - passed_counter}")


if __name__ == "__main__":
    RUN_ALL_TESTS()