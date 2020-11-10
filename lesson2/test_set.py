class TestSet:

    def test_set_length(self, set_correct):
        """
        Проверка длины множества, количества неповторяющихся элементов
        """
        assert len(set_correct) == 3

    def test_set_check_elem(self, set_correct):
        """
        Проверка существует ли элемент внутри множества
        """
        assert 'Vasia' in set_correct

    def test_set_add_elem(self, set_correct):
        """
        Проверка добавления элемента ко множеству
        """
        set_correct.add('000')
        assert set_correct == {'Vasia', 'hi', 'Hellow', '000'}

    def test_set_remove_elem(self, set_correct):
        """
        Проверка удаления элемента из множества
        """
        set_correct.remove('Vasia')
        assert set_correct == {'Hellow', 'hi'}

    def test_set_not_repeated(self, set_correct):
        """
        Проверка что множества не имеют общих элементов
        """
        assert set_correct.isdisjoint({'1', '2', '3', '4'})