import morfeusz2

morf = morfeusz2.Morfeusz()

for text in (u'Jaś miał kota', u'Coś zrobił?', u'qwerty'):
    print(text)
    analysis = morf.analyse(text)
    for interpretation in analysis:
        print(interpretation)

