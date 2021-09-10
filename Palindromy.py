
word = input("Podaj słowo lub zdanie: ")
if len(word)<2:
    print("Zbyt mała liczba znaków")
    exit(1)
if len(word) >=2:
    s=word.replace(" ", "")
    if s.lower()==s.lower()[::-1]:
        print("True")
        exit(1)
    else:
        print("False")
        exit(1)
