stop= False

print("Здравствуй,что хочешь ввести?")
while stop != True:

    book = open("kniga_brat.txt", 'r')
    books = open("kniga_brat.txt", 'a')

    a = input("<")

    if a == "edit":
        title = input("Введите название книги:")
        author = input("Введите автора  книги:")
        creation = input("Введите год создания книги:")
        genre = input("Введите жанр:")
        quanity = input("Введите кол-во книг:")

        pon=title+" "+author+" "+creation+" "+genre+" "+quanity+"\n"
        books.write(pon)

    elif a == "info":
        oke=book.readlines()
        if len(oke)==0:
            print("Здесь пусто")
        else:
            for i in book:
                k=i.replace("\n" , "")
                print(k)

    elif a == "delete":
        n=input("Введи название книги для того, что бы я мог ее удалить:")
        oke = book.readlines()
        for i in oke:
            s=i.split("\n")
            for i in range(len(s)):
                    if s[i] == n:
                        books.remove(oke[i])
        else:
            print("Такой книги не существует:(")

    elif a == "change":
        m=input("Введи название книги которую хочешь изменить:")
        oke = book.readlines()
        for i in range(len(oke)):
            if oke[i] == m:
                oke.remove(oke[i])
                title = input("Введите название книги:")
                author = input("Введите автора  книги:")
                creation = input("Введите год создания книги:")
                genre = input("Введите жанр:")
                quanity = input("Введите кол-во книг:")
                pon = title + " " + author + " " + creation + " " + genre + " " + quanity + "\n"
                books.write(pon)
        else:
             print("Такой книги не существует:(")

    elif a == "menu":
        print("Возможные функции:")
        bo="<edit,<info,<delete,<change,<menu,<stop"
        bo=bo.replace("," , "\n")
        print(bo)

    elif a == "stop":
        stop=True
        print("Конец программы:(")

    else:
        print("Не корректный ввод:(,попробуйте снова")