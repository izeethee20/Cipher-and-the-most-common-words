def encrypt(text, n):
    encryptedText = []
    input_data = list(text)
    for i in range(n):
        if i > 0 and i != n:
            input_data = list(again)
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
# Abcdefghij

# textForEncrypt = "Abcdefghij"
# num = 2
textForEncrypt = input('Введите входные данные:').lower()
num = input('Введите число конкатенаций:')

encrypt(textForEncrypt, int(num))
