# 딕셔너리 키는 포켓몬 이름, 값은 정수형으로 체력
# 체력순으로 배열하고, 새로운 몬스터 넣어서 정렬
# 딕셔너리는 정렬이 안돼...2차원 리스트로!

def insert_and_arrange(monster, health): # 비교, 정렬
    find_pos = -1  # 맨 뒤
    for i in range(len(pokemons)):
            comparison = pokemons[i][1]
            if health >= comparison:
                find_pos = i
                break
    if find_pos == -1:
        find_pos = len(pokemons)

    insert_data(find_pos, [monster, health])  # 함수 호출


def insert_data(pos, monster): # 몬스터 삽입
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
        print('입력하기 전 pokemons 리스트 내림차순 배열')
        pokemons.sort(key=lambda x: -x[1])
        print(pokemons)
        # print(sorted(pokemons, key=lambda monster: -monster[1]))

        monster = input("추가할 몬스터--> ")
        health = int(input("체력--> "))
        insert_and_arrange(monster, health)
        print('삽입 후 pokemons 리스트 내림차순 배열')
        print(pokemons)
        print('\n')


