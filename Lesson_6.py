# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
# приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9

# Select = []
# Stroka = '20 + 14 * 2 - 13 * 5 + 14 / 2 + 10 - 5'
# Select = list(Stroka.split())
# print(Select)

# def mylt(x, y):
#     return int(x)*int(y)
  
# def subtract(x, y):
#     return int(x)-int(y)
    
# def div(x, y):
#     return float(x)/float(y)

# i = 0
# while i < len(Select):
#     if Select[i] == "*":
#         x = mylt(Select[i-1], Select[i+1])
#         b = str(x)
#         del Select[i-1:i+2]
#         Select.insert(i-1, b)
#     if Select[i] == "/":
#         u = div(Select[i-1], Select[i+1])
#         u = str(int(u))
#         del Select[i-1:i+2]
#         Select.insert(i-1, u)
#     i += 1
# print(Select)
# i = 0
# while i < len(Select):
#     if Select[i] == "-":
#         t = subtract(Select[i-1], Select[i+1])
#         c = str(int(t))
#         Select.insert(-1, c)
#         del Select[i-1:i+2]
#     i += 1
# print(Select)

# num_list = []
# for i in Select:
#     if i is not '+':
#         num_list.append(int(i))
# print(num_list)
# print(f'\nРезультат вычисления исходного выражения: {sum(num_list)}')

#____________________________________________________________________________

# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# - входные и выходные данные хранятся в отдельных файлах
#Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, 
# а втором файлике — сжатая версия этого текста)

def to_compress():
    with open('for_compress.txt', 'r') as txt:
        text = txt.read()
        txt.close()
    count = 1
    rle_text = text[0]
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            if count != 1:
                rle_text += str(count)
            rle_text += text[i]
            count = 1
    if count != 1:
        rle_text += str(count)
    with open('compressed.txt', 'w') as txt:
        txt.write(rle_text)
        txt.close()
    print('File compressed')

def to_decompress():
    with open('compressed.txt', 'r') as txt:
        ziped_text = txt.read()
        txt.close()
    num = ''
    unrle_text = ''
    current_letter = ziped_text[0]
    for i in range(1, len(ziped_text)):
        if ziped_text[i].isdigit():
            num = str(num) + str(ziped_text[i])
        else:
            if num == '':
                num = 1
            unrle_text = unrle_text + (current_letter * int(num))
            current_letter = ziped_text[i]
            num = ''
    with open('for_compress.txt', 'w') as txt:
        txt.write(unrle_text)
        txt.close()
    print('File restored')


action = input('Enter "1" to compress, "2" to recover\n')
if action == "1":
    to_compress()
elif action == "2":
    to_decompress()
else:
    print('You can only choose 1 or 2')


