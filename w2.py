class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def create_node(self, data):
        return Node(data)

    def insert_node(self, parent, child_data):
        if self.root is None:
            self.root = self.create_node(child_data)
            return

        new_node = self.create_node(child_data)
        if parent is None:
            return

        found = False
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.data == parent:
                current.children.append(new_node)
                found = True
                break
            queue.extend(current.children)

        if not found:
            print("Loi: Khong tim thay nut cha!")

    def create_tree(self):
        # Get number of nodes
        print("Nhập số lượng nút: ", end="")
        n = int(input())

        # Create root node
        print("Nhập dữ liệu cho nút gốc: ", end="")
        root_data = int(input())
        self.root = self.create_node(root_data)

        # Create child nodes
        for _ in range(n - 1):
            print("Nhập dữ liệu của nút cha và nút con: ", end="")
            parent_data, child_data = map(int, input().split())
            self.insert_node(parent_data, child_data)

    def breadth_first_search(self, root):
        if root is None:
            return

        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")
            queue.extend(current.children)

# Main program
tree = Tree()
tree.create_tree()

print("\n**Duyệt cây theo chiều rộng (BFS):**")
tree.breadth_first_search(tree.root)