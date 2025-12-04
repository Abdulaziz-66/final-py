products = [
    ["matcha", 10],
    ["black coffee", 15],
    ["tea", 5],
    ["latte", 10],
    ["v60", 17]
]

print("اختر رقم المنتج:")
i= 1
for p in products:
    print(str(i) + " - " + p[0])
    i= i + 1

choice = input("اكتب رقم المنتج: ")

if choice.isdigit():
    num = int(choice) - 1

    if num >= 0 and num < len(products):
        name = products[num][0]
        price = products[num][1]

        tax = price * 0.15
        total = price + tax

       
        print("الضريبه:", tax)
        print("السعر مع الضريبه:", total)
    else:
        print("الرقم مو موجود")
else:
    print("اختر رقم فقط")