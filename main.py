import sys
import argparse

###(1) todo: добавить возможность менять стиль shadow.txt, thinkertoy > [STRING] [BANNER]
###(1) todo: добавить возможность сохранить в файл который юзер указал > [OPTION] [STRING] [BANNER]
#(0) todo: возможность выводить символы в цветном виде > [OPTION] [STRING] [BANNER]
#(0) todo: возможность justify, align ровнять центр или вправо  > [OPTION] [STRING] [BANNER]

#(0) todo: оптимизровать код, исправить привести в порядок комменты



# подгрузим шаблон
def load_font(file_path):
    font = {}
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        
        char_h = 8  # высота символа
        index = 0  # начинаем с 0
        
        for ascii_code in range(32, 127):  # ASCII-символы
            char = chr(ascii_code)
            char_representation = lines[index : index + char_h]
            font[char] = char_representation
            index += char_h + 1  # переходим к следующему символу
    
    if ' ' not in font:  # если пробела нет
        font[' '] = [' ' * len(font['!'][0]) for _ in range(char_h)]
    
    return font  # возвращаем


# рендерим
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
            # если символа нет добавляем пробелы
            for i in range(8):
                lines[i] += ' ' * len(font[' '][i])
    
    return '\n'.join(lines)  # возвращаем


def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description="Рендеринг ASCII-арт текста.")
    parser.add_argument("input_text", type=str, help="Текст для рендеринга.")
    parser.add_argument("banner", type=str, nargs="?", default="standard", help="BANNER: standard, shadow, thinkertoy")
    parser.add_argument("-o", "--output", type=str, help="Файл для сохранения", default=None)
    args = parser.parse_args()

    banner = args.banner.lower()
    
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
    ascii_art = render_text(args.input_text, font)
    
    # Если указан output_file, записываем результат в файл или выводим в терминал
    if args.output:
        with open(args.output, 'w') as output_file:
            output_file.write(ascii_art)
    else:
        print(ascii_art)


if __name__ == "__main__":
    main()