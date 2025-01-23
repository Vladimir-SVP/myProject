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
                    words.append(str(line.lower()))
                    
                all_words.update({name : words})
        return all_words
                    
        
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
# s1 = WordsFinder('file1.txt', 'file2.txt')
# s1.get_all_words()
