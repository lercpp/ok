from fileinput import close
from idlelib.configdialog import changes
#то что выше я хз откуда появилось

stop= False


def load_books(filename="kniga_brat.txt"):   #это я сперла т.к не знаю как можно открыть файл,сори:(
    try:
        with open(filename, 'r') as file:

            books_data = [line.strip().split() for line in file]

            return books_data
    except FileNotFoundError:
        return []

def save_books(books_data, filename="kniga_brat.txt"):

    with open(filename, 'w') as file:
        for book in books_data:

            line = " ".join(book) + "\n"
            file.write(line)
#дальше идут исключительно авторские функции
def edit(books_data):
    title = input("Введите название книги:")
    author = input("Введите автора  книги:")

    while True: #это чтоб ломать было сложнее
        try:
            creation = int(input("Введите год создания книги:"))
            break
        except ValueError:
            print("Некорректный ввод. Введите год еще раз")
    creation=str(creation)
    genre = input("Введите жанр:")

    while True: 
        try:
            quantity = int(input("Введите кол-во книг:"))
            break
        except ValueError:
            print("Некорректный ввод. Введите кол-во еще раз")
    quantity = str(quantity)
    pon = [title, author, creation, genre, quantity]
    books_data.append(pon)
    print("Книга добавлена")
    print("-" * 20) #для некой эстетики

def info(books_data):
    if not books_data:
        print("Книга не найдена")
        return
    for book in books_data:
        print("Название:", book[0])
        print("Автор:", book[1])
        print("Год:", book[2])
        print("Жанр:", book[3])
        print("Кол-во:", book[4])
        print("-" * 20)

def delete(books_data):
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
        print("-" * 20)
    else:
        print("Книга не найдена")
        print("-" * 20)

def change(books_data):
    m=input("Введи название книги которую хотите изменить:")
    book = open("kniga_brat.txt", 'r')
    lines = book.readlines()
    new_lines = []
    found = False
    for line in lines:
        if m in line:
            found = True
        else:
            new_lines.append(line)
    book.close()

    if found:
        books = open("kniga_brat.txt", 'w')
        for line in new_lines:
            books.write(line)
        books.close()
    else:
        print("Книга не найдена")
        print("-" * 20)

    if found:
        title = input("Введите название книги:")
        author = input("Введите автора  книги:")

        while True:
            try:
                creation = int(input("Введите год создания книги:"))
                break
            except ValueError:
                print("Некорректный ввод. Введите год еще раз")
        creation = str(creation)
        genre = input("Введите жанр:")

        while True:
            try:
                quantity = int(input("Введите кол-во книг:"))
                break
            except ValueError:
                print("Некорректный ввод. Введите кол-во еще раз")
        quantity = str(quantity)

        pon = [title, author, creation, genre, quantity]
        books_data.append(pon)
        books.close()
        print("Книга добавлена")
        print("-" * 20)

books_data = load_books() #тоже сперто

print("Здравствуй,что вам будет нужно?")
print("для обзора функций введите 'menu'")
print("-"*20)

while stop != True:

    a = input("<")

    if a == "edit":
        edit(books_data)

    elif a == "info":
        info(books_data)

    elif a == "delete":
        delete(books_data)

    elif a == "change":
        change(books_data)

    elif a == "menu":
        print("Возможные функции:")
        print("-" * 20)
        bo = "<edit\n<info\n<delete\n<change\n<menu\n<stop"
        print(bo)
        print("-"*20)

    elif a == "stop":
        stop = True
        print("Конец программы.")

    else:
        print("Не корректный ввод попробуйте снова:")

    save_books(books_data) #сперто