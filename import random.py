import random

damage = random.randint(1,5)
health = 30

def quest1():
    print("\nВы встретили Скелета с мечом")
    global health
    skeleton = 20
    while True:
        
        Sdamage = random.randint(1,6)
        do = input("\nАтаковать или Увернуться?:")
        if do == "Атаковать":
            skeleton = skeleton - damage
            
            if skeleton > 0:
                print(f"У скелета осталось {skeleton} здоровья ")
                health = health - Sdamage
                print(f"Скелет атаковал вас. У вас осталось {health} здоровья")
                
                if health <=0:
                    print("Вы повержены")
                    
            elif skeleton <= 0:
                print("Скелет повержен. Вы получили опыт.")
                break
        elif do == "Увернуться":
            print("Скелет атаковал вас но вы увернулись.")
            
    

while True:
    Quest = input("Из подземелья поблизости начали выходить монстры которые пугают наше поселение. Можешь ли ты нам помочь? :'( (Да, Нет): ")
    if Quest == "Нет":
        print("\nВсе ипугались и ушли, а вы остались одни :(")
        break
    elif Quest == "Да":
        quest1()
    else:
        print("\nНе понел 0-0")
        break