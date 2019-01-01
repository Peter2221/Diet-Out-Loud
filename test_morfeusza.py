import morfeusz2

morf = morfeusz2.Morfeusz()

# for text in (u'Jaś miał kota', u'Coś zrobił?', u'qwerty'):
#     print(text)
#     analysis = morf.analyse(text)
#     for interpretation in analysis:
#         print(interpretation)

word = "Ola Lorenc i Marcin Konieczny są spoko"
print(word)
analysis = morf.analyse(word)

for interpretation in analysis:
    a = 1
    b = interpretation
    print(type(interpretation))
    print(interpretation)

print(interpretation[2][1])



