class Node:
    # Вузол двійкового дерева пошуку.

    def __init__(self, key: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.val: int = key


def insert(node: Node | None, key: int) -> Node:
    # Вставляє новий ключ у двійковому дереві. Повертає корінь дерева.
    if node is None:
        return Node(key)

    if key < node.val:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def search(node: Node | None, key: int) -> Node | None:
    if node is None or node.val == key:
        return node

    if key < node.val:
        return search(node.left, key)

    return search(node.right, key)


def find_max(node: Node | None) -> int | None:
    # Повертає найбільше значення у двійковому дереві або None, якщо дерево порожнє.
    if node is None:
        return None

    current = node
    while current.right is not None:
        current = current.right

    return current.val


if __name__ == "__main__":
    # Побудова дерева
    root: Node | None = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    # Пошук значення
    value_to_find = 4
    result = search(root, value_to_find)

    if result is not None:
        print(f"У дереві знайдено значення {result.val}")
    else:
        print(f"У дереві не знайдено значення {value_to_find}")

    # Пошук максимального значення
    max_value = find_max(root)
    print(f"Найбільше значення у дереві: {max_value}")
