def decryption(s):
    b = set(list(s))
    d = []

    for i in b:
        d.append([s.count(i) / len(s), i])
        # print(i, s.count(i) / len(s))
    # print(b)
    # print(len(s))
    # print(len(b))
    d.sort()
    # print(d)
    # print()

    s = s.replace(' ', '4')
    s = s.replace('>', ' ')
    s = s.replace('2', 'о')
    s = s.replace('0', 'б')
    s = s.replace('Ф', 'л')
    s = s.replace('a', 'е')
    s = s.replace('Х', 'м')
    s = s.replace('b', 'ж')
    s = s.replace('1', 'н')
    s = s.replace('<', 'ы')
    s = s.replace('А', 'т')
    s = s.replace('Ы', 'ь')
    s = s.replace('r', 'с')
    s = s.replace('Р', 'в')
    s = s.replace('О', 'а')
    s = s.replace('Д', 'п')
    s = s.replace('Е', 'р')
    s = s.replace('7', 'и')
    s = s.replace('9', 'д')
    s = s.replace('4', 'я')
    s = s.replace('У', 'к')
    s = s.replace('t', 'ч')
    s = s.replace('Й', 'щ')
    s = s.replace('М', 'ц')
    s = s.replace('3', 'г')
    s = s.replace('8', 'й')
    s = s.replace('Б', 'у')
    s = s.replace('Л', 'х')
    s = s.replace('Я', 'ю')
    s = s.replace('Ь', 'э')
    s = s.replace('К', 'ф')
    s = s.replace('c', 'з')
    s = s.replace('И', 'ш')
    
    print(s)

    return s


if __name__ == "__main__":

    with open("D:\\lab_oib\\isb-1\\isb-1\\cod2.txt", "r", encoding = "utf-8") as f:
        text = f.read()

    dec = decryption(text)
    print(dec)
    
    with open("D:\\lab_oib\\isb-1\\isb-1\\cod2_decrypted.txt", "w", encoding = "utf-8" ) as f:
        f.write(dec)

        