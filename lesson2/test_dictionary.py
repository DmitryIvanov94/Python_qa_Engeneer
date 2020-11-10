class TestDict:

    def test_dict_get_value(self, dict_correct):
        """
        Проверка получения значения по ключу
        """
        assert dict_correct['Hellow'] == 'Vasia'

    def test_dict_get_keys(self, dict_correct):
        """
        Проверка получения ключей словаря
        """
        assert str(dict_correct.keys()) == "dict_keys(['Hellow', 'hi'])"

    def test_create_dict_fromkeys(self):
        """
        Проверка создания словаря методом fromkeys
        """
        assert dict.fromkeys(['a', 'b'], 100) == {'a': 100, 'b': 100}

    def test_dict_add_key_and_value(self, dict_correct):
        """
        Проверка добавления новой пары ключ: значение
        """
        dict_correct[2] = 'New value'
        assert dict_correct == {2: 'New value', 'Hellow': 'Vasia', 'hi': '111'}

    def test_dict_clear(self, dict_correct):
        """
        Проверка очистки словаря
        """
        dict_correct.clear()
        assert dict_correct == {}
