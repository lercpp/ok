books=open("kniga_brat.txt", 'r')
stop=False
start=False

while stop!=True:
    
        if start==True:
            def main():
                books = load_books()
                while True:
                    print("Выберите действие")
                    print("1. Добавить книгу")
                    print("2. Показать все книги")
                    print("3. Удалить книгу")
                    print("4. Выход")

                    choice = input("Ваш выбор: ")

                    if choice == '1':
                        new_book(books)
                    elif choice == '2':
                        ok(books)
                    elif choice == '3':
                        dele(books)
                    elif choice == '4':
                        red(books)
                    elif stop==True:
                        print("Конец программы")
                    else:
                        print("Некорректный ввод. Попробуйте еще раз.")
            def load_books():
                f=open("kniga_brat.txt", 'w')

        def new_book(books):
            title= input("Введите название книги:")
            author= input("Введите автора  книги:")
            creation= input("Введите год создания книги:")
            genre = input("Введите жанр:")
            quanity= input ("Введите кол-во книг:")

            books.append({
                'Название' : title,
                'Автор' : author,
                'Год' : creation,
                'Жанр' : genre,
                'Кол-во' : quanity
            })

        def ok(books):
            oke=books.readlines()
            print(oke)


        def dele(books):
            n=input("Введите книгу которую хотите удалить:")
            book=books.readlines()
            if n==None:
                print("Вы ничего не ввели:(")
            else:
                for i in book:
                    if book[i]==n:
                        books.remove(book[i])
                    else:
                        print("Вы ввели не существующую книгу")


        def red(books):
            oke = books.readlines()
            n=int(input("Введите строку для изменения:"))
            title = input("Введите название книги:")
            author = input("Введите автора  книги:")
            creation = input("Введите год создания книги:")
            genre = input("Введите жанр:")
            quanity = input("Введите кол-во книг:")

            for i in range(len(oke)):
                if oke[i]==n:
                    books.append({
                        'Название': title,
                        'Автор': author,
                        'Год': creation,
                        'Жанр': genre,
                        'Кол-во': quanity
                    })