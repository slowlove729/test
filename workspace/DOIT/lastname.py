class NameBook:
    def __init__(self, name):
        self.name = name

    def data(self, name):
        self.name = name

def addname(list, name):

    BOOK = NameBook(name)

    list.append(BOOK.name)


book = []


addname(book, "찬영")

addname(book, "용준")

addname(book, "대국")

addname(book, "수형")

addname(book, "종혁")

booklen = len(book) # 리스트의 길이

for i in range(0, booklen): # 반복 출력
    if i < booklen-1:
        print(book[i], end=", ")
    else:
        print(book[i]) 
