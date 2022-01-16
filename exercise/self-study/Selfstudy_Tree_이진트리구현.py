"""
클래스로 Node 와 Tree 를 구현하고,
Tree의 메소드로
    - 노드 삽입                                     O
    - 노드 삭제
    - 노드 탐색                                     O
    - 노드 갯수 구하기                               O
    - 트리의 깊이 구하기                             O
    - 전위, 후위, 중위 순회 알고리즘 구현하기          O

를 구현한다.


"""


class TreeNode:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def is_terminal(self):
        if not self.get_left_child() and not self.get_right_child():
            # print(self.get_data(), "노드는 터미널 노드입니다")
            return True

        else:
            # print(self.get_data(), "노드는 터미널 노드가 아닙니다")
            return False

    def show_node(self):
        print("----------------")
        print("데이터: ", self.data)
        if self.get_left_child():
            print("왼쪽 child: ", self.get_left_child().get_data())
        else:
            print("왼쪽 child: 없음")

        if self.get_right_child():
            print("오른쪽 child: ", self.get_right_child().get_data())
        else:
            print("오른쪽 child: 없음")

        print("----------------")

    def count(self):
        print(self.get_data(), "번 노드")
        if self.get_left_child():
            l_count = self.left.count()
        else:
            l_count = 0

        if self.get_right_child():
            r_count = self.right.count()
        else:
            r_count = 0

        return l_count + r_count + 1

    def depth_count(self):
        print(self.get_data(), "번 노드")
        if self.get_left_child():
            l_depth = self.left.depth_count()

        else:
            l_depth = 0

        if self.get_right_child():
            r_depth = self.get_right_child().depth_count()
        else:
            r_depth = 0

        return max(l_depth, r_depth) + 1

    def rec_prefix_traverse(self):
        if self.get_left_child():
            left_child = self.get_left_child()
            left_child.rec_prefix_traverse()
            print(self.data, "번 노드")
        else:
            print(self.data, "번 노드")

        if self.get_right_child():
            right_child = self.get_right_child()
            right_child.rec_prefix_traverse()

    def rec_infix_traverse(self):
        print(self.data, "번 노드")
        if self.get_left_child():
            left_child = self.get_left_child()
            left_child.rec_infix_traverse()

        if self.get_right_child():
            right_child = self.get_right_child()
            right_child.rec_infix_traverse()

    def rec_postfix_traverse(self):
        if self.get_left_child():
            left_child = self.get_left_child()
            left_child.rec_postfix_traverse()

        if self.get_right_child():
            right_child = self.get_right_child()
            right_child.rec_postfix_traverse()

        print(self.data, "번 노드")


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root_node(self):
        return self.root

    def get_total_node(self):
        node = self.get_root_node()
        res = 0
        if not node:
            return 0
        if node:
            res = node.count()

        print("노드의 갯수: ", res)
        return res

    def get_depth(self):
        node = self.get_root_node()

        res = node.depth_count()
        print("트리의 깊이: ", res)
        return res

    def insert_node(self, item):
        # print("------------")
        # print(item, "삽입")
        inserted_node = TreeNode(item)
        if not self.root:
            self.root = inserted_node
            # print("첫 노드 삽입")
            # print("root: ", self.root.get_data())

        else:
            node = self.root
            while True:
                # print("비교하려는 노드: ", node.get_data())
                if item > node.get_data():
                    if node.get_right_child():
                        node = node.get_right_child()
                    else:
                        node.set_right_child(inserted_node)
                        break

                elif item < node.get_data():
                    if node.get_left_child():
                        node = node.get_left_child()
                    else:
                        node.set_left_child(inserted_node)
                        break

                else:
                    # print("삽입하려한", item, "은 이미 Tree에 있습니다")
                    break

    def delete_node(self, item):
        print("item: ", item)
        flag = self.search_node(item)
        if not flag:
            print(item, "값을 가진 노드가 없습니다")
            return

        else:
            deleted_node = None
            parent = self.get_root_node()

            while parent:
                print("parent: ", parent.get_data())
                if parent and item < parent.get_data():
                    child = parent.get_left_child()
                    if child and child.get_data() == item:
                        deleted_node = child
                        break
                    else:
                        parent = child

                elif parent and item > parent.get_data():
                    child = parent.get_right_child()
                    if child and child.get_data() == item:
                        deleted_node = child
                        break
                    else:
                        parent = child

                else:
                    deleted_node = parent
                    break

            print("지워질 노드: ", deleted_node.get_data())
            print("지워질 노드의 부모: ", parent.get_data())

            # 루트 노드 삭제하는 경우
            if deleted_node.data == self.get_root_node().data:
                temp_parent = deleted_node
                temp_child = deleted_node.get_right_child()

                while True:
                    if not temp_child.get_left_child():
                        cand_node = temp_child
                        break
                    else:
                        temp_parent = temp_child
                        temp_child = temp_child.get_left_child()

                print("삭제할 노드: ", deleted_node.data)
                print("계승자 노드: ", cand_node.data)
                print("계승자 노드의 부모 노드: ", temp_parent.data)

                temp_parent.set_left_child(None)
                deleted_node.set_data(cand_node.data)

            elif deleted_node.is_terminal():
                left = parent.get_left_child()
                right = parent.get_right_child()

                if left and parent.get_left_child().get_data() == item:
                    parent.set_left_child(None)
                if right and parent.get_right_child().get_data() == item:
                    parent.set_right_child(None)

            # 자식 1개, 왼쪽
            elif deleted_node.get_left_child() and not deleted_node.get_right_child():
                deleted_node.set_data(deleted_node.get_left_child().get_data())
                deleted_node.set_left_child(None)

            # 자식 1개, 오른쪽
            elif not deleted_node.get_left_child() and deleted_node.get_right_child():
                deleted_node.set_data(deleted_node.get_right_child().get_data())
                deleted_node.set_right_child(None)

            # 자식 2개인 경우, 오른쪽 서브트리에서 가장 작은 값을 뽑아서, 그 값을 del
            else:
                temp_parent = deleted_node
                temp_child = deleted_node.get_right_child()

                while True:
                    if not temp_child.get_left_child():
                        cand_node = temp_child
                        break
                    else:
                        temp_parent = temp_child
                        temp_child = temp_child.get_left_child()

                print("계승자 노드: ", cand_node.data)
                # print("계승자 노드의 자식 노드: ", cand_node.get_right_child().data)

                if parent.get_left_child().data == deleted_node.data:
                    deleted_node.set_data(cand_node.data)
                    deleted_node.set_right_child(cand_node.get_right_child())
                    parent.set_left_child = deleted_node
                else:
                    deleted_node.set_data(cand_node.data)
                    deleted_node.set_right_child(cand_node.get_right_child())
                    parent.set_right_child = deleted_node







    def search_node(self, item):
        node = self.get_root_node()

        while node:
            if item == node.get_data():
                # print(item, "값을 가진 노드가 있습니다")
                return node
                break

            elif item < node.get_data():
                node = node.get_left_child()

            else:
                node = node.get_right_child()
        else:
            print(item, "값을 가진 노드가 없습니다")
            return False

    def prefix_traverse(self):
        print("----------전위 순회----------")
        node = self.get_root_node()
        node.rec_prefix_traverse()

    def infix_traverse(self):
        print("----------중위 순회----------")
        node = self.get_root_node()
        node.rec_infix_traverse()

    def postfix_traverse(self):
        print("----------후위 순회----------")
        node = self.get_root_node()
        node.rec_postfix_traverse()

    def show_tree(self):
        node = self.get_root_node()
        # print("root 노드: ", node.get_data())

        start = node
        queue = []
        if node.get_left_child():
            queue.append(node.get_left_child())
        if node.get_right_child():
            queue.append(node.get_right_child())

        # print("queue: ", queue)
        print("\t", node.get_data())
        temp = []
        for a in queue:
            temp.append(a.get_data())
        print("\t", *temp)
        while queue:
            new_arr = []
            for idx in queue:
                node = idx

                if node.get_left_child():
                    left_child = node.get_left_child()
                    new_arr.append(left_child)

                if node.get_right_child():
                    right_child = node.get_right_child()
                    new_arr.append(right_child)

            queue = new_arr
            data_list = []

            for x in new_arr:
                data_list.append(x.get_data())

            if data_list:
                print("\t", *data_list)


if __name__ == '__main__':
    print("main 함수 시작")
    bt = BinaryTree()

    arr = [5, 3, 7, 2, 4, 6, 8, 1, 9]
    for i in arr:
        bt.insert_node(i)

    print("트리 생성 완료")

    print("삭제 전 트리")
    bt.show_tree()

    bt.delete_node(5)
    print("\n\n삭제 후 트리")
    bt.show_tree()





