from collections import Counter


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
    result0 = []
    result = []
    temp = []
    for i in range(len(mass)):
        if (mass[i] and mass[i].strip()) == False \
                or mass[i].isnumeric() == True \
                or any(map(str.isdigit, mass[i])) == True:
            pass
        elif "'" in mass[i]:
            # print('GJ! --> ', mass[i])
            temp.append(mass[i])
    # print(temp)
    temp1 = Counter(temp)
    # print(temp1)
    temp2 = temp1.values()
    # print(temp2)
    val = list(temp1.values())
    res = []
    for i in range(3):
        tmp = max(val)
        if tmp < 2:
            print('Something went wrong...', result0)
            return result0
        else:
            res.append(tmp)
            val.remove(tmp)
            # print(res)
            result.append(list(temp1.keys())[i])
    print('Result: ', result)
    # i = 0
    # while i < 3:
    #     if int(list(temp2)[i]) < 2:
    #         print(int(list(temp1.values())[i]), i, temp1.values())
    #         print(result0)
    #         return result0
        # print(list(temp1.keys())[i])
        # result.append(list(temp1.keys())[i])
        # i += 1
    # for i in range(len(temp)):
    #     for j in range(len(temp) - 1, 0, -1):
    #         print(i, j, temp[j])
    #         if i!=j and temp[i] == temp[j]:
    #             count[i] =
    return result


# print('===Шифр моноподстановки===')
# textForEncrypt = input(' Введите входные данные:')
# num = int(input(' Введите число конкатенаций:'))
#
# textForDecrypt = encrypt(textForEncrypt, num)[num - 1]
# if (textForDecrypt and textForDecrypt.strip()) != False:
#     print('Decrypt:')
#     decrypt(textForDecrypt, num)
# print('===============================')


textForDef = "hi9, h9'ow a're 'you hi y'o'u a're  a're a're a're a're  'you 'you 7are8 'are  'are 'you hi, ,8'8   , &f ?are"

print('===============================')
mostCommon(textForDef)
print('===============================')
