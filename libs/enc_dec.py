import time 
encoder_tuples_array = [
    ("a", "'⟩"),
    ("b", "ⴶ"),
    ("c", "⌈'"),
    ("d", ",|̶,"),
    ("e", "⳻'"),
    ("f", "⠕"),
    ("g", "٪"),
    ("h", ",|'"),
    ("i", "'/|"),
    ("j", "|;"),
    ("k", "|'|"),
    ("l", '|"'),
    # "r" поднята над m
    ("r", "_] "), # внимание - пробел
    ("m", "] "),
    # "w" поднята над n
    ("w", "|["),
    ("n", "["),
    # "u" поднята над o --> [uou]
    ("u", "|_|"),
    ("t", ",|"),
    ("o", "| |"),
    ("p", "⌉"),
    ("q", "'||"),
    # "r" ^^ поднята над m
    ("s", ",-'"),
    # "u" поднята над o
    ("v", "|⌊"),
    # "w" ^^ поднята над "n"
    ("x", 'ッ'),
    ("y", "∤"),
    ("z", "×|"),
    ("~", "-_"),
    ("%", "/,,"),
    ("#", ';; ;;'),
    ("^", "' '"),
    ("&", "⁅"),
    ("*", "'"),
    ("(", "「"),
    ("$", '"|,,'),
    (",", "꓾"),
    (")", "」"),
    ("?", "︙")
]

enc = {'a': "'⟩", 'b': "'|'", 'c': "⌈'", 'd': ',|̶,', 'e': "⳻'", 'f': ':∙', 'g': "'⳺", 'h': ",|'", 'i': "'/|", 'j': '|;', 'k': "|'|", 'l': '|"', 'r': '_] ', 'm': '] ', 'w': '|[', 'n': '[', 'u': '|_|', 't': ',|', 'o': '| |', 'p': '⌉', 'q': "'||", 's': ",-'", 'v': '|⌊', 'x': '"/', 'y': '∤', 'z': '×|', '~': '-_', '%': '/,,', '#': ';; ;;', '^': "' '", '&': '⁅', '*': "'", '(': '「', '$': '"|,,', ',': '꓾', ')': '」', '?': '︙'}

def encoder(raw_string):
    start = time.time()
    # !! Преобразование сырой строки в строку с малыми символами!
    # Если в словарь добавляются большие символы - убрать
    raw_string = raw_string.lower().replace('^enc','').strip()
    # строка, которая будет выводиться в конце кодирования
    output_string = ""

    # Вобшем я тут поменял чуть чуть, чтоб ускорить - Линк
    for c in raw_string:
      if c != ' ' and c in enc:
        output_string+=enc[c]
      else:
        output_string+=c
      output_string+=' '

    #for rs_char in raw_string:
    #    
    #    CHAR_IS_FOUNDED = False
    #    # old -> for j in encoder_tuples_array:
    #    # old ->     if rs_char.find(j[0]) != -1:
    #    # old ->         CHAR_IS_FOUNDED = True
    #    # old ->         output_string += rs_char.replace(j[0], j[1])
    #    # old ->         break
    #    # Если символа не нашлось в словаре: он остается таким, каким и был
    #    if not CHAR_IS_FOUNDED:
    #        output_string += rs_char
    #    # Добавление "пробелов" после каждого "символа"
    #    output_string += ' '

def decoder(raw_string):
    # строка, которая будет выводиться в конце декодирования
    output_string = raw_string + ' '
    
    # Непосредственно декодирование
    for decoder_tuple_case in encoder_tuples_array:
        output_string = output_string.replace(decoder_tuple_case[1], decoder_tuple_case[0])

    return '```'+output_string.replace("  ", "Ֆ").replace(" ", "").replace("Ֆ", " ")+'```'
