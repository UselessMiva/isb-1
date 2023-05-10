total=0
with open("task_2_txt", "r", encoding="utf-8") as f:
    string = f.read().split('\n')
    text = "".join(string)
    print(text)
    dict1 = {}
    for l in text:
        if l not in dict1:
            dict1[l] = 1
        else:
            dict1[l] += 1
        total += 1

    dict_probability = {}
    print(total)

    for key in dict1.keys():
        dict_probability[key] = dict1[key] / 642


    dict_probability = sorted(dict_probability.items(), key=lambda x: x[1], reverse=True)
    for c in dict_probability:
        print(*c)

    dict = {}

    text = text.replace(" ", "{")
    text = text.replace("2", " ")
    dict["2"] = " "

    text = text.replace("О", "&")
    text = text.replace("К", "О")
    dict["К"] = "О"

    text = text.replace("Ь", "И")
    dict["Ь"] = "И"

    text = text.replace("Е", "-")
    text = text.replace("t", "Е")
    dict["t"] = "Е"

    text = text.replace("А", "/")
    text = text.replace("Ы", "А")
    dict["Ы"] = "А"

    text = text.replace("<", "В")
    dict["<"] = "В"

    text = text.replace("r", "Н")
    dict["r"] = "Н"

    text = text.replace("Д", "Т")
    dict["Д"] = "Т"

    text = text.replace(">", "С")
    dict[">"] = "С"

    text = text.replace("&", "Р")
    dict["О"] = "Р"

    text = text.replace("М", ">")
    text = text.replace("Б", "М")
    dict["Б"] = "М"

    text = text.replace("Л", "<")
    text = text.replace("Й", "Л")
    dict["Й"] = "Л"

    text = text.replace("Д", "*")
    text = text.replace("Я", "Д")
    dict["Я"] = "Д"

    text = text.replace("Я", "Ё")
    text = text.replace("1", "Я")
    dict["1"] = "Я"

    text = text.replace("К", "7")
    text = text.replace("Ч", "К")
    dict["Ч"] = "К"

    text = text.replace("{", "П")
    dict["{"] = "П"

    text = text.replace(">", "З")
    dict[">"] = "З"

    text = text.replace("0", "Ы")
    dict["0"] = "Ы"

    text = text.replace("Ь", "}")
    text = text.replace("Х", "Ь")
    dict["Х"] = "Ь"

    text = text.replace("У", "!")
    text = text.replace("/", "У")
    dict["/"] = "У"

    text = text.replace("a", "Ч")
    dict["а"] = "Ч"

    text = text.replace("<", "Ж")
    dict["<"] = "Ж"

    text = text.replace("8", "Г")


    text = text.replace("-", "Х")
    dict["-"] = "Х"
    text = text.replace("Ф", "z")
    text = text.replace("c", "Ф")
    dict["с"] = "Ф"

    text = text.replace("3", "Й")
    dict["3"] = "Й"

    text = text.replace(",", "Ю")
    dict["Ь"] = "Я"

    text = text.replace(".", "Б")
    dict["."] = "Б"

    text = text.replace("b", "Ц")
    dict["b"] = "Ц"
    text = text.replace("9", "Ш")
    dict["9"] = "Ш"
    text = text.replace("z", "Щ")
    dict["z"] = "Щ"
    text = text.replace("?", "Э")
    dict["?"] = "Э"
    text = text.replace("7", "К")
    print(text)
    text=text.replace("К","!")
    text=text.replace("Л","К")
    dict["Й"] = "К"
    print(text)
    text=text.replace("А","Q")
    text=text.replace("Т","А")
    dict["Д"] = "А"
    print(text)
    text=text.replace("Н","+")
    text=text.replace("Q","Н")
    dict["Q"] = "Н"
    print(text)
    text = text.replace("Е", "_")
    text = text.replace("О", "Е")
    dict["К"] = "Е"
    text = text.replace("И", "[")
    text = text.replace("_", "И")
    dict["t"] = "И"
    text= text.replace("Ш","<")
    text=text.replace("Ц","Ш")
    dict["b"] = "Ш"
    text=text.replace("Л",">")
    text=text.replace("!","Л")
    dict["Ч"] = "Л"
    text=text.replace("Ь","@")
    text=text.replace("Ю","Ь")
    dict[","] = "Ь"
    text=text.replace("М","$")
    text=text.replace("В","М")
    dict["<"] = "М"
    text=text.replace("П","№")
    text=text.replace("Д","П")
    dict["Я"] = "П"
    text=text.replace("[","О")
    dict["Ь"] = "О"
    text=text.replace("$","Д")
    dict["Б"] = "Д"
    text=text.replace("Г","*")
    text=text.replace("У","Г")
    dict["/"] = "Г"
    text=text.replace("+","В")
    dict["r"] = "В"
    text=text.replace("Р","Т")
    dict["О"] = "Т"
    text=text.replace("№","Р")
    dict[" "] = "Р"
    text=text.replace("@","Ю")
    dict["Х"] = "Ю"
    text=text.replace("Ф", "Щ")
    dict["c"] = "Щ"
    text=text.replace("Ы","У")
    dict["0"] = "У"
    text=text.replace("Б",",")
    text=text.replace("Х","Б")
    dict["Е"] = "Б"
    text=text.replace("<","Ц")
    dict["9"] = "Ц"
    text=text.replace("*","Ы")
    dict["Я"] = "Ы"
    text=text.replace("Й","Х")
    dict["3"] = "Х"
    print(text)
with open("task_2_res", "w", encoding="utf-8") as f:
    f.write(text.lower())
    f.write("\n")
with open("task_2_key", "w", encoding="utf-8") as f:
    f.write(str(dict))
    f.write("\n")