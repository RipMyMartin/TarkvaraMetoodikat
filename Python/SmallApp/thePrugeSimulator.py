### **Projekti idee:**

"""Loome konsoolirakenduse, mis simuleerib “Sundöö” (The Purge) stsenaariumi, kus kasutaja peab tegema otsuseid,
et ellu jääda kindla aja jooksul.Mängus on eesmärk ellu jääda, hallates ressursse,
vältides ohte ja tehes strateegilisi otsuseid.
See projekt võimaldab iteratiivset arendamist, kus me lisame samm-sammult uusi funktsioone 
ja arutame iga iteratsiooni lõpus.
"""

### Iteratsioonid ja Arutelupunktid

### **Sprint 1: Põhistruktuuri ja Algandmete Loomine**

"""
**1.1 Koodi kirjutamine**

- **Eesmärk:** Luua põhistruktuur, kus kasutajal on teatud ressursid (nt toiduvarud ja energiatase) ja eluaeg (mänguaeg), mille jooksul tuleb ellu jääda.
"""

"""**1.2 Arutelupunktid**

- **Arutelu:** Kas loodud struktuur on piisav baastaseme ellujäämissimulaatoriks?
- **Scrum-praktika:** Iga sprindi lõpus vaatame üle, kas meie töö täidab eesmärki ja mida saame täiustada.
- **Tagasiside:** Kas meeskond soovitab lisada uusi elemente, näiteks rohkem ressursse või rohkem võimalusi tervise taastamiseks?
"""
### **Sprint 2: Ohtude ja Valikute Lisamine**

"""
**2.1 Koodi kirjutamine**

- **Eesmärk:** Lisada mängijale valikud ja ohtude simulatsioon, näiteks juhuslikud sündmused, mis võivad vähendada tervist.
- **Tegevused:**
    - Loome funktsiooni “event()”, mis simuleerib juhuslikke sündmusi.
    - Igal mängukäigul saab mängija valida, kas puhata (kasutab toitu), liikuda edasi või riskida.
"""

"""
**2.2 Arutelupunktid**

- **Arutelu:** Kuidas lisada põnevust ja ohtu, et mäng oleks huvitavam? Kas peaksime lisama juhuslikke sündmusi, nagu tervise taastamine või rohkem ressursse?
- **Scrum-praktika:** Kas meeskonnal on ettepanekuid sprindi iteratsiooni parandamiseks, näiteks lisada rohkem valikuid või muuta sündmuste tõenäosust?
- **Tagasiside:** Mida õppisime ohtude lisamisest ja kuidas see muudab mängukogemust?
"""
### **Sprint 3: Ellujäämismängu Pikendamine ja Valikute Täiustamine**

"""
**3.1 Koodi kirjutamine**

- **Eesmärk:** Lisada mängijale rohkem valikuid ja mänguaja mõõdik.
- **Tegevused:**
    - Lisame mänguaja loenduri ja määrame tingimused, mille järgi mäng lõpeb.
    - Loome lisafunktsioone, näiteks võimaluse varuda ressursse.
"""
"""
**3.2 Arutelupunktid**

- **Arutelu:** Kuidas erinevad valikud mängija ellujäämist mõjutavad? Kas peaksime lisama veel tegevusi?
- **Scrum-praktika:** Kuidas aitavad igapäevased arutelud meeskonnal paremini otsuseid teha? Arutame, kuidas scrum-praktikad aitasid meil mängu edasi arendada.
- **Tagasiside:** Milliseid iteratsioone peaksime järgmiseks arendama, et mäng oleks veelgi huvitavam ja strateegilisem?

"""
import random

class defence:
    def __init__(self, helmet, chestplate, leggings, boots):
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots

    def randArmorDrop(self):
        self.helmet = random.randint(0, 5)
        self.chestplate = random.randint(0, 5)
        self.leggings = random.randint(0, 5)
        self.boots = random.randint(0, 5)

    
    def isArmorEquipped(self, armor):
        match armor:
            case self.helmet:
                if self.helmet > 0:
                    self.helmet -= 1
                    print("Helmet equipped!")
            case self.chestplate:
                if self.chestplate > 0:
                    self.chestplate -= 1
                    print("Chestplate equipped!")
            case self.leggings:
                if self.leggings > 0:
                    self.leggings -= 1
                    print("Leggings equipped!")
            case self.boots:
                if self.boots > 0:
                    self.boots -= 1
                    print("Boots equipped!")
            case _:
                print("Invalid armor type!")
    
        armor_status = {
            "Helmet": "IS EQUIPPED" if self.helmet > 0 else "NOT EQUIPPED",
            "Chestplate": "IS EQUIPPED" if self.chestplate > 0 else "NOT EQUIPPED",
            "Leggings": "IS EQUIPPED" if self.leggings > 0 else "NOT EQUIPPED",
            "Boots": "IS EQUIPPED" if self.boots > 0 else "NOT EQUIPPED",
        }
    
        print("Armor status:")
        for part, status in armor_status.items():
            print(f"[{part.upper()}] : : [{status}]")
        

class Player:
    """
    Player has in start:

    - 10 HP
    - 10 Energy
    - 10 Food
    - 0 Defence
    - 0 Attack

        """
    def __init__(self, hp, energy, food, defence):
        self.hp = hp
        self.energy = energy
        self.food = food
        self.defence = defence

        self.helmet = 0
        self.chestplate = 0
        self.leggings = 0
        self.boots = 0

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 3
            print("You rested and gained (3 energy)!!!")
        else:
            print("You don't have enough food to rest!!!")
