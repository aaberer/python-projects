import math


def heapsort(hlist):
    if hlist is None:
        return None
    if not hlist:
        return []

    heap = []

    for item in hlist:
        heap.append(item)
        bubble_up(heap, len(heap) - 1)

    sorted_list = []

    while heap:
        sorted_list.append(heap[0])
        heap[0] = heap[-1]
        heap.pop()
        if heap:
            bubble_down(heap, 0, len(heap))

    return sorted_list


def parent(index):
    return (index - 1) // 2


def rchild(index):
    return 2 * (index + 1)


def lchild(index):
    return 2 * index + 1


def has_left_child(index, size):
    return lchild(index) < size


def has_right_child(index, size):
    return rchild(index) < size


def swap(heap, index1, index2):
    heap[index1], heap[index2] = heap[index2], heap[index1]


def bubble_down(heap, index, size):
    largest = index
    left = lchild(index)
    right = rchild(index)

    if has_left_child(index, size) and heap[left] > heap[largest]:
        largest = left
    if has_right_child(index, size) and heap[right] > heap[largest]:
        largest = right

    if largest != index:
        swap(heap, index, largest)
        bubble_down(heap, largest, size)


def bubble_up(heap, index):
    while index > 0:
        parent_index = parent(index)
        if heap[index] > heap[parent_index]:
            swap(heap, index, parent_index)
            index = parent_index
        else:
            break
