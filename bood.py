from fileinput import close

stop= False

print("Здравствуй,что хочешь ввести?")
while stop != True:

    book = open("kniga_brat.txt", 'r')
    books = open("kniga_brat.txt", 'w')

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
        title_to_delete = input("Введите книгу для того, чтобы я смог ее удалить: ")
        book = open("kniga_brat.txt", 'r')
        lines = book.readlines()
        new_lines = []
        found = False
        for line in lines:
            if title_to_delete in line:
                found = True
            else:
                new_lines.append(line)
        book.close()

        if found:
            books = open("kniga_brat.txt", 'w')
            for line in new_lines:
                books.write(line)
            books.close()
            print("Выбранная книга удалена")
        else:
            print("Книга не найдена")

    elif a == "change":
        a=[]
        m=input("Введи название книги которую хочешь изменить:")
        book = open("kniga_brat.txt", 'r')
        oke = book.readlines()
        for i in book:
            if oke in i:
                id = True
            else:
                a.append(i)
        book.close()

        if id==True:
            title = input("Введите название книги:")
            author = input("Введите автора  книги:")
            creation = input("Введите год создания книги:")
            genre = input("Введите жанр:")
            quanity = input("Введите кол-во книг:")
            pon = title + " " + author + " " + creation + " " + genre + " " + quanity + "\n"
            books = open("kniga_brat.txt", 'w')
            a.append(pon)
            for i in a:
                books.write(i)
            books.close()
        else:
            print("Такой книги не существует:")

    elif a == "menu":
        print("Возможные функции:")
        bo="<edit\n<info\n<delete\n<change\n<menu\n<stop"
        print(bo)

    elif a == "stop":
        stop=True
        print("Конец программы:")

    else:
        print("Не корректный ввод попробуйте снова:")
