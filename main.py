import sys


#todo: добавить возможность менять стиль shadow.txt, thinkertoy > [STRING] [BANNER]
#todo: добавить возможность сохранить в файл который юзер указал > [OPTION] [STRING] [BANNER]
#todo: возможность выводить символы в цветном виде > [OPTION] [STRING] [BANNER]
#todo: оптимизровать код, исправить



# подгрузим шаблон
def load_txt(file_path): 
    font = {} # словарь
    with open(file_path, 'r') as f:
        lines = f.read().splitlines() # Читаем файл и делим его строки
        
        char_h = 8 #высота
        index = 0 #начинаем c 0
        
        for ascii_code in range(32, 127):
            char = chr(ascii_code)
            char_rep = lines[index : index + char_h]
            font[char] = char_rep
            index += char_h + 1 
    
    if ' ' not in font:     # Если пробела нет добавляем
        font[' '] = [' ' * len(font['!'][0]) for _ in range(char_h)]
    
    return font # Возвращаем


# Рендерим
def render_text(text, font):
    result = ['' for _ in range(8)]  # Записывать строки для картинки

    for char in text:
        if char == '\n':  # Если перенос строки
            print('\n'.join(result))  # Печатаем и очищаем
            result = ['' for _ in range(8)]  # Очищаем, чтобы начать с новой строки
        elif char in font:  # Если символ есть в тхт
            for i in range(8):
                result[i] += font[char][i]  # Добавляем строки св результат
        else:  # Если символа нет просто добавляем пробелы
            for i in range(8):
                result[i] += ' ' * len(font[' '][i]) 

    return '\n'.join(result)  # возвращаем

### 
def main():
    input_text = sys.argv[1] # Получаем текст
    font = load_txt('standard.txt')  # Загружаем из txt
    ascii_art = render_text(input_text, font) # Рендим текст
    print(ascii_art) #выдаем




if __name__ == "__main__":
    main()