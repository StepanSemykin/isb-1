def encryption(string: str, key: str):
    
    len_key = len(key)
    string += ' ' * (len_key - len(string) % len_key)
    matrix = [[] for _ in range(len_key)]
    
    for st in range(len(string) // len_key):
        for j, sub_key in enumerate(key):
            matrix[j].append(string[st * (len_key) + int(sub_key) - 1])
    
    # for i in matrix:
    #     print(*i)
    
    return(''.join(''.join(i) for i in matrix))
 
def decryption(string: str, key: str):
    
    len_key = len(key)
    matrix = [['' for _ in range(len_key)] for _ in range(len(string) // len_key)]
    
    st = iter(string)
    
    for sub_key in key:
        for i in range(len(string) // len_key):
            matrix[i][int(sub_key) - 1] = next(st)
    
    # for i in matrix:
    #     print(*i)
    
    return(''.join(''.join(i) for i in matrix))

if __name__ == "__main__":
    with open("D:\\lab_oib\\isb-1\\isb-1\\Text.txt", "r", encoding = "utf-8") as f:
        text = f.read() 
    
    text = encryption(text, '58137462')
    
    with open("D:\lab_oib\isb-1\isb-1\Text_enc.txt", "w", encoding = "utf-8") as f:
        f.write(text) 

    with open("D:\lab_oib\isb-1\isb-1\Key.txt", "w", encoding = "utf-8") as f:
        f.write('58137462')    

# Шифр вертикальной перестановки
# key = '58137462'        