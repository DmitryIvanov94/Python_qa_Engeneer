import pytest


@pytest.mark.parametrize("string_correct", ['Hellow'])
class TestString:

    def test_string_split(self, string_correct):
        """
        Проверка разделения строки
        """
        assert string_correct.split('ll') == ['He', 'ow']

    def test_string_addition(self, string_correct):
        """
        Проверка сложения строки
        """
        assert string_correct + string_correct == 'HellowHellow'

    def test_string_multiplication(self, string_correct):
        """
        Проверка умножения строки
        """
        assert string_correct * 3 == 'HellowHellowHellow'

    def test_string_length(self, string_correct):
        """
        Проверка длины строки
        """
        assert len(string_correct) == 6

    def test_string_alpha(self, string_correct):
        """
        Проверка состоит ли строка из букв
        """
        assert string_correct.isalpha()

    def test_string_index(self, string_correct):
        """
        Проверка доступа по индексу
        """
        assert string_correct[0] == 'H'
