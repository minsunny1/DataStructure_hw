def is_stack_full():
    global stone_number, top, stack
    if top >= stone_number - 1:
        return True
    else:
        return False


def is_stack_empty():
    global stone_number, top, stack
    if top == -1:
        return True
    else:
        return False


def go_forest_put_stone(data):
    global stone_number, top, stack
    if is_stack_full():
        print("돌을 다 썼음")
        return None
    top += 1
    stack[top] = data


def go_home_pick_stone():
    global stack, top, stone_number
    if is_stack_empty():
        print("돌을 다 주웠음")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


stone_number = int(input("돌의 개수: "))
stack = [None for _ in range(stone_number)]
top = -1

if __name__ == "__main__":
    for i in range(stone_number):
        data = input("돌 이름: ")
        go_forest_put_stone(data)
        print(f'top = {top}')
        print(f'놓고 온 돌 = {stack}')

    for i in range(stone_number, 0, -1):
        go_home_pick_stone()
        print(f'줍고 남은 돌 = {stack}')



