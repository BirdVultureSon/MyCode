import random
'''list = ["магазин" , "школа" , "бабушка"]
list[0] = "парк"
print (list)'''

'''list = ["магазин" , "школа" , "бабушка"]
#list.remove ("магазин") 
value = list.pop()
print (list)'''

#books = ["Гари Потер" , "Властелин колец" , "Простоквашино"]
'''lengh = len (books)
for i in range (len(books)):
    print (f"{i+1}:{books[i]}")'''

'''for i in books: #range (len(books)):
    print (i) #f"{i+1}:{books[i]}"'''

'''if "Гари Потер" in books:
    print ("Сработало")'''
'''book = str(input("Введите название книги:"))
if book not in books:
    books.append (book)
print (books)'''
character = ["мудрый", "дерзкий", "жизнерадостный", "хромой", "трусливый", "смелый", "бешеный", "гордый", "лопоухий", "неудержимый"]
animal = ["тигр", "суслик", "орел", "заяц", "олень", "кабан", "сайгак", "медведь", "мустанг", "жираф"]
fn = random.choice (character)
sn = random.choice (animal)
print (f"В племени индейцев Чумбы-мумбы, тебя бы звали... {fn} {sn}!")




