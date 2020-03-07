import os

class Jumble:

    def _generate_lookup(self):
        with open("/usr/share/dict/words") as f:
            lines = f.read().lower()
            word_list = lines.split('\n')
        lookup = []
        for word in word_list:
            key = self._generate_id(word)
            pair = (key, word)
            lookup.append(pair)
        return lookup

    def _generate_id(self, word):
        word_val = 0
        for char in word:
            char_val = ord(char)
            word_val += char_val
        word_id = word_val * len(word)
        return word_id
    
    def _group(self):
        ano_dict = {}
        for key, word in self._generate_lookup():
            if key in ano_dict:
                ano_dict[key].append(word)
            else:
                ano_dict.setdefault(key, [word])
        return ano_dict
        


        

    




    

def test():
    jumble = Jumble()
    print(jumble._generate_id("Listen"))
    jumble_dict = jumble._group()
    print(jumble._generate_id("Listen"))
    



test()



        




