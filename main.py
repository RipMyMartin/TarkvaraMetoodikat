class Patsient:
    def __init__(self, nimi, vanus, regAeg):
        self.nimi = nimi
        self.vanus = vanus
        self.regAeg = ""

class Hospital:
    def __init__(self):
        self.patsientList = []
        self.docktorList = []

    def PatsientKuvamine(self):
        for index, elem in enumerate(self.patsientList):
            print("id: ", index, "Nimi:", elem.nimi, "Vanus:", elem.vanus)

    def DoctorKuvamine(self):
        for index, elem in enumerate(self.docktorList):
            print("id: ", index, "Nimi:", elem.nimi, "Vanus:", elem.vanus, "Eriala:", elem.eriala)

    def KohtumineTegemine(self):
        PatsientIndex = 0

        PatsientNimi = input("Sisesta patsientNimi")
        DoctorName = input("Sisesta Doc nimi")

        for elem in self.patsientList:
            if elem.nimi == patsientNimi:
                PatsientIndex = self.patsientList.index(elem)


        for elem in self.docktorList:
            if elem.nimi == doctorName and len(elem.aeg) > 0:
                self.patsientList[PatsientIndex].regAeg = elem.aeg[0]

        for elem in self.patsientList:
            print("Nimi:", elem.nimi, "Aeg", elem.regAeg)


                

class Doctor:
    def __init__(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = aeg


Patsient1 = Patsient("Markus", 17)
Patsient2 = Patsient("David", 36)
Patsient3 = Patsient("Gelb", 108)

Doctor1 = Doctor("Martin", 56, "ortopeed", ['10:00', '11:00', '12:00'])
Doctor2 = Doctor("Jakopson", 87,"silmaarst", ['14:00', '18,00', '19,00'])

haigla = Hospital()
haigla.patsientList.append(Patsient1)
haigla.patsientList.append(Patsient2)
haigla.patsientList.append(Patsient3)

haigla.docktorList.append(Doctor1)
haigla.docktorList.append(Doctor2)

print("------------PATSIENT------------")
haigla.PatsientKuvamine()
print("-----------DOCTOR---------------")
haigla.DoctorKuvamine()
