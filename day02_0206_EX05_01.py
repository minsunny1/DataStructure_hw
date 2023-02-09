import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def store_distance(start):
    current = start
    if current.link == None:
        return

    while current.link != start:
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], ' 편의점, 거리: ', math.sqrt(x*x + y*y))
    print()


def store_list(store_name):
    global current, head, pre

    node = Node()
    node.data = store_name

    if head == None:  # 첫 노드
        head = node
        node.link = head
        return

    # 새 편의점이 첫번째 편의점보다 가깝다면
    x_node, y_node = node.data[1:]
    node_dist = math.sqrt(x_node*x_node + y_node*y_node)
    x_head, y_head = head.data[1:]
    head_dist = math.sqrt(x_head * x_head + y_head * y_head)

    if node_dist < head_dist:
        head = node
        node.link = head
        last = head

        return

