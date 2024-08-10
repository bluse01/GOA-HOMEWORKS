
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

mylist = ["addsc", 12, 43, 1.2, "Monday", 3, "Friday"]

for w in weekdays:
    for i in mylist:
        if w == i:
            print(i)