### ASCII Art Project 

Программа для создания ASCII-арта из текста с поддержкой различных стилей.

#### Функциональность:

1. **Базовый вывод текста в ASCII-арт** — принимает строку и преобразует её в ASCII-арт.
2. 💎 **Выбор стиля** — поддерживает стили: `standard`, `shadow`, и `thinkertoy`
3. 💎 **Запись ASCII-арта в файл** — сохраняет преобразованный текст в указанный файл.

#### Порядок команды: 
[OPTION] [STRING] [BANNER]

- **OPTION** — Опция записи в файл (дополнить позже)
- **STRING** — Текст для преобразования
- **BANNER** — Стиль шрифта: standard, shadow, или thinkertoy.

##### Пример:
```bash
main.py "Salem" standard
main.py --output=somefile.txt "Salem" shadow