logs = []

def logi(logs):
    jag = 0
    kor = 0
    liit = 0
    lah = 0
    for elem in logs:
        if elem == 'liitumine':
            liit += 1
        elif elem == 'lahutamine':
            lah += 1
        elif elem == 'korrutamine':
            kor += 1
        elif elem == 'jagamine':
            jag += 1

    return[liit, lah, kor, jag]

def liitumine(a, b):
    logs.append('liitumine')
    if isinstance (a, str) or isinstance(b, str):
        print("vale tüüp")
        return ""
    return a + b

def lahutamine(a, b):
    logs.append('lahutamine')
    if isinstance (a, str) or isinstance(b, str):
        print("vale tüüp")
        return ""
    return a - b

def korrutamine(a, b):
    logs.append('korrutamine')
    if isinstance (a, str) or isinstance(b, str):
        print("vale tüüp")
        return ""
    return a * b

def jagamine(a, b):
    logs.append('jagamine')
    try:
        if isinstance (a, str) or isinstance(b, str):
            print("vale tüüp")
            return ""
        return a / b
    except ZeroDivisionError:
        print("ei saa jagada")

print("liitumine:" , (liitumine(5, "1")))
print("lahutamine:" , (lahutamine(5,1)))
print("korrutamine:" , (korrutamine(5,5)))
print("jagamine:" , (jagamine(10,7)))
print(logi(logs))
