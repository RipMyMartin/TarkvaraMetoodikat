import random
import time

food = 5
energy = 5
health = 10
days_left = 7

def status():
    print(f"\n📊 Staatus:")
    print(f"🍞 Toit: {food}")
    print(f"⚡ Energia: {energy}")
    print(f"❤️ Tervis: {health}")
    print(f"📅 Päevi jäänud: {days_left}\n")

def event():
    global health, food, energy
    roll = random.randint(1, 4)
    if roll == 1:
        print("⚠️ Sattusid röövlite otsa! Kaotasid 2 tervist.")
        health -= 2
    elif roll == 2:
        print("🍀 Leidsid varjupaiga, taastad 1 tervist.")
        health += 1
    elif roll == 3:
        print("🌧 Kaotasid natuke toitu vihma tõttu.")
        food = max(food - 1, 0)
    elif roll == 4:
        print("😴 Jäid väsinuks, energia -1.")
        energy = max(energy - 1, 0)

def player_choice():
    global food, energy, health
    print("Valikud:\n1. Puhka (kasutab toitu, taastab energiat)\n2. Liigu edasi (kasutab energiat)\n3. Riskige (võib juhtuda sündmus)")
    choice = input("👉 Tegevus (1/2/3): ")
    if choice == "1":
        if food > 0:
            food -= 1
            energy += 2
            print("😌 Puhkasid, energia taastatud.")
        else:
            print("❌ Pole piisavalt toitu!")
    elif choice == "2":
        if energy > 0:
            energy -= 1
            print("🚶‍♂️ Liikusid edasi.")
        else:
            print("❌ Pole piisavalt energiat!")
            health -= 1
    elif choice == "3":
        print("🎲 Riskid...")
        event()
    else:
        print("❓ Tundmatu valik, päev möödub ilma tegevuseta.")

def game_over():
    return health <= 0 or (food <= 0 and energy <= 0)

def main():
    global days_left
    print("🎮 Tere tulemast mängu: Sundöö (The Purge)!")
    while days_left > 0 and not game_over():
        status()
        player_choice()
        days_left -= 1
        time.sleep(1)

    status()
    if health > 0:
        print("🏆 Ellu jäid! Sundöö on läbi.")
    else:
        print("💀 Surid enne kui Sundöö lõppes.")

if __name__ == "__main__":
    main()
