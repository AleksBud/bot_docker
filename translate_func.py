def translater(text: str):
    d = {'а':'a', 'А':'A',
         'б':'b', 'Б':'B',
         'в':'v', 'В':'V',
         'г':'g', 'Г':'G',
         'д':'d', 'Д':'D',
         'е':'e', 'Е':'E',
         'ё':'e', 'Ё':'E',
         'ж':'zh', 'Ж':'ZH',
         'з':'z', 'З':'Z',
         'и':'i', 'И':'I',
         'й':'i', 'Й':'I',
         'к':'k', 'К':'K',
         'л':'l', 'Л':'L',
         'м':'m', 'М':'M',
         'н':'n', 'Н':'N',
         'о':'o', 'О':'O',
         'п':'p', 'П':'P',
         'р':'r', 'Р':'R',
         'с':'s', 'С':'S',
         'т':'t', 'Т':'T',
         'у':'u', 'У':'U',
         'ф':'f', 'Ф':'F',
         'х':'kh', 'Х':'KH',
         'ц':'ts', 'Ц':'TS',
         'ч':'ch', 'Ч':'CH',
         'ш':'sh', 'Ш':'SH',
         'щ':'shch', 'Щ':'SHCH',
         'ъ':'ie', 'Ъ':'IE',
         'ы':'y', 'Ы':'Y',
         'ь':'', 'Ь':'',
         'э':'e', 'Э':'E',
         'ю':'iu', 'Ю':'IU',
         'я':'ia', 'Я':'IA'}
    text = text.split()
    for index, word in enumerate(text):
        if word.capitalize() == word:
            for key in d:
                word = word.replace(key, d[key]).capitalize()
                text[index] = word
        else:
            for key in d:
                word = word.replace(key, d[key])
                text[index] = word
    text = ' '.join(text)
    return text