class TestList:

    def test_list_length(self, list_correct):
        """
        Проверка длины списка
        """
        assert len(list_correct) == 5

    def test_list_add_elem(self, list_correct):
        """
        Проверка добавления элемента ко списку
        """
        list_correct.append('Append')
        assert list_correct == ['Hellow', 'Vasia', 'Hellow', 'hi', '111', 'Append']

    def test_list_insert(self, list_correct):
        """
        Проверка вставки элемента в список на определённую позицию
        """
        list_correct.insert(1, 'Petya')
        assert list_correct == ['Hellow', 'Petya', 'Vasia', 'Hellow', 'hi', '111']

    def test_list_count(self, list_correct):
        """
        Проверка количества определённых элементов в списке
        """
        assert list_correct.count('Hellow') == 2

    def test_list_clear(self, list_correct):
        """
        Проверка очистки списка
        """
        list_correct.clear()
        assert list_correct == []