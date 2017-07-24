class Encryptor:
    def crypt_word(self, word):
        if " " in word:
            raise ValueError()

        new_word = ""
        for i in range(len(word)):
            char_value = ord(word[i]) #charcode
            new_word += chr( char_value + 2) # ""encripta""
    
        return new_word

    def crypt_word_to_numbers(self, word):
        if " " in word:
            raise ValueError()

        new_word = ""
        for i in range(len(word)):
            char_value = ord(word[i])
            new_word += str(char_value + 2)

        return new_word

    def crypt_word_with_chars_to_replace(self, word, chars_to_replace):
        if " " in word:
            raise ValueError()
        result = list(word)
        for i in range(len(word)):
            for j in range(len(chars_to_replace)):
                if chars_to_replace[j] == word[i]:
                    char_value = ord(word[i])
                    result[i] = chr( char_value + 2)
        return "".join(result)

    def crypt_sentence(self, sentence):
        new_word = ""
        for i in range(len(sentence)):
            char_value = ord(sentence[i])
            new_word += chr( char_value + 2)

        return new_word

    def get_words(self, sentence):
        return sentence.split()

    def print_words(self, sentence):
        words = self.get_words(sentence)
        for word in words:
            print("<%s>" % word)

