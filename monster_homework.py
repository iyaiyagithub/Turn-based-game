import random
import keyboard

class Player:
    def __init__(self , name , hp ):
        self.name = name
        self.hp = hp
    
    def attack(self , enemy, normal , magic):
        self.normal = normal
        self.magic = magic
        damage = normal or magic
        # damage 변수값을 입력값의 조건에 따라서 normal  혹은 magic으로 바꾸고 싶다
        enemy.hp = max(enemy.hp - damage, 0)

      

    def status(self):
        print(f"{self.name}님의 hp는 {self.hp}입니다" )
        


class Monster:
    def __init__(self , name , hp):
        self.name = name
        self.hp = hp

    def attack (self, other , hit):
        self.hit = hit 
        other.hp = max(other.hp - hit , 0 )

    def status(self):
        print(f"{self.name}의 hp는 {self.hp}입니다" )

P = Player( "플레이어", 100)
M = Monster("몬스터" , 100)

def attack_method():
    # 선택값 받기
    Method = input()
    if  keyboard.is_pressed("1"):
        P.normal 
        #플레이어 어택과 몬스터 어택을 비교해서 큰 캐릭터가 공격하고 hp 깎인 거 출력

    elif keyboard.is_pressed("2") :
        P.magic
        #플레이어 어택과 몬스터 어택을 비교해서 큰 캐릭터가 공격하고 hp 깎인 거 출력
    else:
        print("1, 2 중에 하나만 ㅋ")
        return attack_method()

     


print("이름을 입력해주세요.")
Username = input()
print(f"당신의 이름은{Username}")








def game():
    while True:
        

        P = Player( Username , 100)
        M = Monster("몬스터" , 100)

        P.status()
        M.status()

        print("공격 방법을 선택해주세요.\n"
              "1. 일반공격\n"
              "2.마법공격\n")
        
        attack_method()
        
        


        
        
    

    

        M.attack(P,random.randint(0,10))
        P.attack( M, random.randint(0,5) , random.randint(5,10))

        print(P.name, P.hp)
        print(P.normal , P.magic)

    


game()
