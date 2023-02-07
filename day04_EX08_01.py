def is_queue_full():
    global size, queue, front, rear
    if rear != size - 1:
        return False
    elif (rear == size - 1) & (front == -1):
        return True
    else:
        for i in range(front + 1, size):
            queue[i - 1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


def is_queue_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enqueue(name):
    global size, queue, front, rear
    if is_queue_full():
        print("대기줄이 꽉 찼습니다.")
        return None
    rear += 1
    queue[rear] = name


def dequeue():
    global size, queue, front, rear
    if is_queue_empty():
        print("대기손님이 없습니다.")
        return None
    front -= 1
    name = queue[front]
    return name


def shift():
    global size, queue, front, rear
    for i in range(front + 1, size):
        print(f'{queue[front + 1]} 님 식당에 들어감')
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1


size = int(input("대기 가능 인원: "))
front = rear = -1
queue = [None for _ in range(size)]

if __name__ == "__main__":
    while not is_queue_full():
        name = input("대기할 손님 이름: ")
        enqueue(name)
        print(f'대기 줄 상태: {queue}')

    while not is_queue_empty():
        shift()
        # print(f'{queue[front]} 님 식당에 들어감')


