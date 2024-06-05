
# assignment 1
# შემოატანინეთ მომხმარებელს ერთი რიცხვი და შეამოწმეთ არის თუ არა ეგ რიცხვი მეტი 5-ზე ზე და ნაკლები ან ტოლი 10-ზე გამოიყენეთ and
def a1(fint):
    if fint > 5 and fint <= 10: return True

# assignment 2
# შემოატანინეთ მომხმარებელს რიცხვი და შეამოწმეთ არის თუ არა ეს რიცხვი მეტი 5-ზე ან მეტი 10-ზე
def a2(fint):
    if fint > 5 or fint > 10: return True

def main():
    fint = int(input("fint Input: "))

    check = int(input("1) A1 2) A2"))

    match check:
        case 1:
            a1(fint)
        case 2:
            a2(fint)

main()