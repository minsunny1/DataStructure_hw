class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


c = None
stack = []
visit_arr = []
store = ['GS25', 'CU', 'SEVEN11', 'EMART24', 'MINISTOP']
GS25, CU, SEVEN11, EMART24, MINISTOP = 0, 1, 2, 3, 4
honey = [30, 60, 10, 40, 90]

if __name__ == "__main__":
    c = Graph(5)
    c.graph[0][1] = 1; c.graph[0][2] = 1
    c.graph[1][0] = 1; c.graph[1][2] = 1; c.graph[1][4] = 1
    c.graph[2][0] = 1;  c.graph[2][1] = 1;  c.graph[2][4] = 1
    c.graph[3][4] = 1
    c.graph[4][1] = 1;  c.graph[4][2] = 1;  c.graph[4][3] = 1

    print('          ', end=' ')
    for n in range(c.SIZE):
        print(store[n], end='   ')
    print()

    for row in range(c.SIZE):
        print("{0:^10}".format(store[row]), end=' ')
        for col in range(c.SIZE):
            print("{0:^7}".format(c.graph[row][col]), end='')
        print()
    print()
