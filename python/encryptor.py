def assert_word(func):
    def func_wrapper(self, word, *args, **kwargs):
        if " " in word:
            raise ValueError()
        return func(self, word, *args, **kwargs)
    return func_wrapper


class Encryptor:
    _CESAR_OFFSET = 2

    @assert_word
    def crypt_word(self, word):
        return self._crypt_string(word)

    @assert_word
    def crypt_word_to_numbers(self, word):
        return self._crypt_string(word, str)

    @assert_word
    def crypt_word_with_chars_to_replace(self, word, chars_to_replace):
        return "".join([
            chr(self._get_encrypted_value(char))
            if char in chars_to_replace
            else char
            for char in word
        ])

    def crypt_sentence(self, sentence):
        return self._crypt_string(sentence)

    def get_words(self, sentence):
        return sentence.split()

    def print_words(self, sentence):
        words = self.get_words(sentence)
        for word in words:
            print("<%s>" % word)

    def _assert_is_word(self, string):
        if " " in string:
            raise ValueError()

    def _crypt_string(self, string, transform_fn=chr):
        return ''.join([
            transform_fn(char)
            for char in self._generate_encrypted_chars(string)
        ])

    def _generate_encrypted_chars(self, string):
        for char in string:
            yield self._get_encrypted_value(char)

    def _get_encrypted_value(self, char):
        return ord(char) + self._CESAR_OFFSET
