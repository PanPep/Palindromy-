word = input()
if len(word)<2:
    print("Zbyt mała liczba znaków")
    exit(1)
if len(word) >=2:
    s=word.replace(" ", "")
    if s.lower()==s.lower()[::-1]:
        print("True")
        exit(1)
    
