# 딕셔너리 키는 포켓몬 이름, 값은 정수형으로 체력
# 체력순으로 배열하고, 새로운 몬스터 넣어서 정렬
# 딕셔너리는 정렬이 안돼...2차원 리스트로!

def find_insert(monster, health):
    find_pos = -1
    for i in range(len(pokemons)):
        for j in range(len(pokemons[i])):
            comparison = pokemons[i][j]
            test = pokemons[j]
            if health >= test[1]:
                find_pos = i
                break
    if find_pos == -1:
        find_pos = len(pokemons)

    insert_data(find_pos, [monster, health])


def insert_data(pos, monster):
    if pos < 0 or pos > len(pokemons):
        print("out of range!")
        return

    pokemons.append(None)

    for i in range(len(pokemons)-1, pos, -1):
        pokemons[i] = pokemons[i-1]
        pokemons[i-1] = None

    pokemons[pos] = monster


pokemons = [['피카츄', 300], ['꼬부기', 500], ['이상해', 100], ['꼬북왕', 1000]]

if __name__ == "__main__":
    while True:
        monster = input("추가할 몬스터--> ")
        health = int(input("체력--> "))
        find_insert(monster, health)
        print(pokemons)
        print(len(pokemons))

