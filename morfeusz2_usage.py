import morfeusz2

# for text in (u'Jaś miał kota', u'Coś zrobił?', u'qwerty'):
#     print(text)
#     analysis = morf.analyse(text)
#     for interpretation in analysis:
#         print(interpretation)

# word = "Ola Lorenc i Marcin Konieczny są spoko"
# print(word)
# analysis = morf.analyse(word)
#
# for interpretation in analysis:
#     a = 1
#     b = interpretation
#     print(type(interpretation))
#     print(interpretation)
#
# print(interpretation[2][1])

class Morfeusz2_usage:

    def infinitive_of_word(self, word):
        morf = morfeusz2.Morfeusz()
        analysis = morf.analyse(word)

        if len(analysis) == 1:
            return analysis[0][2][1]
        elif len(analysis) == 2:
            return analysis[1][2][1]
        else:
            return analysis[len(analysis)-1][2][1]

if __name__ == "__main__":
    morf = Morfeusz2_usage()
    word = morf.infinitive_of_word("gramów")
    print(word)