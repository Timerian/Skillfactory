class ExplicitFilter:
    example = open('expwords.txt', 'r')

    FLAGS = ['.',
             ',',
             '/',
             '?',
             '!',
             '@',
             '#',
             '$',
             '%',
             '^',
             '&',
             '*',
             '(',
             ')',
             '|',
             ]

    def __init__(self, string):
        self.original_string = string
        self.change = '*'

    def cleaning(self):
        temp = self.original_string
        for i in self.FLAGS:
            temp = temp.replace(i, '')
        return temp

    def changing(self):
        explicit = '%s' %' '.join(self.example).split('\n ')
        process_words = self.cleaning().split(' ')
        temp = self.original_string
        for word in process_words:
            if word.lower() in explicit:
                l = len(word) - 1
                new_word = f'{word[0]}{self.change * l}'
                temp = temp.replace(word, new_word)
        return temp


s = 'Motherfucker, Cunt Bitch'

f = ExplicitFilter(s)

clean = f.changing()
print(clean)



