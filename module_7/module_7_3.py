class WordsFinder:
    file_name = []
    def __init__(self, *args):
        WordsFinder.file_name = [*args]                
    def get_all_words(self):
        all_words = {}
        for name in self.file_name:
            with open(name, encoding = 'utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for i in symbols:
                        if i in line:
                            line = line.replace(i, ' ')
                    line = line.split()
                    words.extend(line)                    
                all_words.update({name : words})                
        return all_words
    def find(self, word):
        result = {}        
        for name, words in self.get_all_words().items():
            result.update({name : words.index(word.casefold()) + 1})
        return result            
    def count(self, word):
        result = {} 
        for name, words in self.get_all_words().items():
            result.update({name : words.count(word.casefold())})
        return result
        
print('========================')        
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
print()