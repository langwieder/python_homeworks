# Открыть файлик с таблицей для транслитерации
f = open("translit.csv", "r", encoding="utf8")

# Словарь, в котором в качестве ключей будут грузинские символы,
# а в качестве значений - грузинские
translit_dic = {}

for line in f:
    segments = line.split("	")
    gruz = segments[0]
    ipa =  segments[2]
    translit_dic[gruz] = ipa


# Текст для транслитерации
text = "ქართული ანბანი"

# Переменная для хранения результата транслитерации
translit = text

# Транслитерация
for key in translit_dic:
    translit = translit.replace(key, translit_dic[key])

# Выводим на экран исходный текст и результат транслитерации
print(text)
print(translit)