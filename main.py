import sys

###(1) todo: добавить возможность менять стиль shadow.txt, thinkertoy > [STRING] [BANNER]
#(0) todo: добавить возможность сохранить в файл который юзер указал > [OPTION] [STRING] [BANNER]
#(0) todo: возможность выводить символы в цветном виде > [OPTION] [STRING] [BANNER]
#(0) todo: оптимизровать код, исправить



# подгрузим шаблон
def load_font(file_path):
    font = {}
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        
        char_h = 8  #высота
        index = 0 #начинаем c 0
        
        for ascii_code in range(32, 127):  # ASCII-символы
            char = chr(ascii_code)
            char_representation = lines[index : index + char_h]
            font[char] = char_representation
            index += char_h + 1  # переходим к следующему символу
    
    if ' ' not in font:     # Если пробела нет
        font[' '] = [' ' * len(font['!'][0]) for _ in range(char_h)]
    
    return font #Возвращаем




# Рендерим
def render_text(input_text, font):
    lines = ['' for _ in range(8)]  
    
    for char in input_text:
        if char == '\n':
            lines = ['' for _ in range(8)]
            print('\n'.join(lines))
            continue
        if char in font:
            char_representation = font[char]
            for i in range(8):
                lines[i] += char_representation[i]
        else:
             # Если символа нет добавляем пробелы
            for i in range(8):
                lines[i] += ' ' * len(font[' '][i])
    
    return '\n'.join(lines)   # возвращаем




### 
def main():
    if len(sys.argv) != 3:
        print("Используйте команду: python3 main.py <STR> <BANNER>")
        print("BANNER: standard, shadow, thinkertoy")
        return
    
    input_text = sys.argv[1]
    banner = sys.argv[2].lower()
    
    # Определяем путь к файлу
    font_files = {
        'standard': 'standard.txt',
        'shadow': 'shadow.txt',
        'thinkertoy': 'thinkertoy.txt'
    }
    
    # Проверяем, что указанный BANNER доступен
    if banner not in font_files:
        print(f"Такого BANNER - '{banner}' НЕТ! Доступно: standard, shadow, thinkertoy")
        return
    
    font = load_font(font_files[banner])  # загрузка выбранного шрифта
    ascii_art = render_text(input_text, font)
    print(ascii_art)

if __name__ == "__main__":
    main()