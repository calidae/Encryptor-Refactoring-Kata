import pytest
from encryptor import Encryptor

@pytest.fixture
def encryptor():
    return Encryptor()

def test_crypt_word_fails_if_is_sentence(encryptor):
    with pytest.raises(ValueError):
        encryptor.crypt_word('patata bullida')

def test_crypt_word_returns_encrypted_word(encryptor):
    assert encryptor.crypt_word('hola') == 'jqnc'

def test_crypt_word_to_numbers_fails_if_is_sentence(encryptor):
    with pytest.raises(ValueError):
        encryptor.crypt_word_to_numbers('patata bullida')

def test_crypt_word_to_number_returns_encrypted(encryptor):
    assert encryptor.crypt_word_to_numbers('abc') == '99100101'

def test_crypt_word_with_chars_to_replace_fails_if_is_sentence(encryptor):
    with pytest.raises(ValueError):
        encryptor.crypt_word_with_chars_to_replace('patata bullida', 'a')

def test_crypt_word_with_chars_replace_returns_encrypted(encryptor):
    assert encryptor.crypt_word_with_chars_to_replace('hola', 'ho') == 'jqla'

def test_crypt_sentence_returns_encrypted(encryptor):
    assert encryptor.crypt_sentence('hola hola') == 'jqnc"jqnc'

def test_get_words(encryptor):
    assert encryptor.get_words('hola hola') == ['hola', 'hola']

