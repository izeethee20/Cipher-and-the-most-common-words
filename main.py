def encrypt(text, n):
    if bool(text and text.strip()) == False or None or n <= 0:
        print(text)
        return text
    print('Encrypt:')
    print(textForEncrypt)
    encryptedText = []
    input_data = list(text.lower())
    for i in range(n):
        if i > 0 and i != n:
            input_data = list(again.lower())
        encryptedText1 = []
        res = []
        res1 = []
        mass = []
        for j in range(len(text)):
            mass.append(input_data[j])
            if (j + 1) % 2 == 0:
                res.append(mass[j])
            else:
                res1.append(mass[j])
        for k in range(len(res1)):
            res.append(res1[k])
        encryptedText1.append(''.join(res))
        again = ''.join(encryptedText1)
        encryptedText.append(''.join(encryptedText1))
        print(encryptedText)
    return encryptedText


def decrypt(text, n):
    decryptedText = []
    input_data = list(text)
    print(''.join(input_data))
    for i in range(n):
        if i > 0 and i != n:
            input_data = list(again)
        decryptedText1 = []
        res = []
        mass = []
        count = len(text) // 2
        for j in range(len(text)):
            mass.append(input_data[j])
        for j in range(len(text) // 2):
            res.append(mass[count])
            res.append(mass[j])
            count += 1
        if len(text) % 2 != 0:
            res.append(mass[count])
        decryptedText1.append(''.join(res))
        again = ''.join(decryptedText1)
        decryptedText.append(''.join(decryptedText1))
        print(decryptedText)
    return decryptedText


def mostCommon(text):
    mass = text.split()
    # print(temp)
    temp = []
    for i in range(len(mass)):
        if (mass[i] and mass[i].strip()) == False \
                or mass[i].isnumeric() == True \
                or any(map(str.isdigit, mass[i])) == True:
            print('udalit`', mass[i])
        elif "'" in mass[i]:
            print('GJ! --> ', mass[i])
            temp.append(mass[i])
        else:
            print('udalit`', mass[i])
    print(temp)
    for i in range(len(temp)):
        for j in range(len(temp) - 1, 0, -1):
            print(i, j, temp[j])
            if i!=j and temp[i] == temp[j]:

    return 'result'


# print('===Шифр моноподстановки===')
# textForEncrypt = input(' Введите входные данные:')
# num = int(input(' Введите число конкатенаций:'))
#
# textForDecrypt = encrypt(textForEncrypt, num)[num - 1]
# if (textForDecrypt and textForDecrypt.strip()) != False:
#     print('Decrypt:')
#     decrypt(textForDecrypt, num)
# print('===============================')


textForDef = "hi9, h9'ow 'you hi y'o'u a're a're  'you 7are8 'are 'you hi, ,8'8   , &f ?are"

mostCommon(textForDef)
print('===============================')
