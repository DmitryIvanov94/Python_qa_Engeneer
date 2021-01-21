from lesson6.figure import Figure


# В каждом классе содержатся проверки:
# периметра, площади, функции суммы площадей, допустимых значений имени фигуры, угла и длин сторон

class TestSquare:

    def test_check_area_perimeter_correct_params(self):
        square = Figure('square', 4, 8)
        assert square.area == 64
        assert square.perimeter == 32

    def test_check_area_correct_add_new_figure(self):
        square = Figure('square', 4, 8)
        rectangle = Figure('rectangle', 4, 5, 8)
        assert Figure.add_area(square, rectangle) == 104

    def test_check_area_perimeter_uncorrect_angle(self):
        square = Figure('square', 0, 8)
        assert str(square.area) == "Wrong parameters of figure"
        assert str(square.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_name(self):
        square = Figure('figure_uncorrected', 4, 8)
        assert str(square.area) == "Wrong parameters of figure"
        assert str(square.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_length_side(self):
        square = Figure('square', 4, -8)
        assert str(square.area) == "Wrong parameters of figure"
        assert str(square.perimeter) == "Wrong parameters of figure"


class TestRectangle:

    def test_check_area_perimeter_correct_params(self):
        rectangle = Figure('rectangle', 4, 4, 8)
        assert rectangle.area == 32
        assert rectangle.perimeter == 24

    def test_check_area_correct_add_new_figure(self):
        rectangle = Figure('rectangle', 4, 5, 8)
        triangle = Figure('triangle', 3, 3, 4, 5)
        assert Figure.add_area(rectangle, triangle) == 46.0

    def test_check_area_perimeter_uncorrect_angle(self):
        rectangle = Figure('rectangle', 1, 4, 8)
        assert str(rectangle.area) == "Wrong parameters of figure"
        assert str(rectangle.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_name(self):
        rectangle = Figure('figure_uncorrected', 4, 4, 8)
        assert str(rectangle.area) == "Wrong parameters of figure"
        assert str(rectangle.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_length_side(self):
        rectangle = Figure('square', 4, -4, -8)
        assert str(rectangle.area) == "Wrong parameters of figure"
        assert str(rectangle.perimeter) == "Wrong parameters of figure"


class TestTriangle:

    def test_check_area_perimeter_correct_params(self):
        triangle = Figure('triangle', 3, 3, 4, 5)
        assert triangle.area == 6
        assert triangle.perimeter == 12

    def test_check_area_correct_add_new_figure(self):
        triangle = Figure('triangle', 3, 3, 4, 5)
        circle = Figure('circle', 0, r=5)
        assert int(Figure.add_area(triangle, circle)) == 84

    def test_check_area_perimeter_uncorrect_angle(self):
        triangle = Figure('triangle', 5, 3, 4, 5)
        assert str(triangle.area) == "Wrong parameters of figure"
        assert str(triangle.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_name(self):
        triangle = Figure('figure_uncorrected', 3, 3, 4, 5)
        assert str(triangle.area) == "Wrong parameters of figure"
        assert str(triangle.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_length_side(self):
        triangle = Figure('triangle', 3, -3, 4, -5)
        assert str(triangle.area) == "Wrong parameters of figure"
        assert str(triangle.perimeter) == "Wrong parameters of figure"


class TestCircle:

    def test_check_area_perimeter_correct_params(self):
        circle = Figure('circle', 0, r=5)
        assert int(circle.area) == 78
        assert int(circle.perimeter) == 31

    def test_check_area_correct_add_new_figure(self):
        circle = Figure('circle', 0, r=5)
        square = Figure('square', 4, 8)
        assert int(Figure.add_area(circle, square)) == 142

    def test_check_area_perimeter_uncorrect_angle(self):
        circle = Figure('circle', 3, r=5)
        assert str(circle.area) == "Wrong parameters of figure"
        assert str(circle.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_name(self):
        circle = Figure('figure_uncorrected', 0, r=5)
        assert str(circle.area) == "Wrong parameters of figure"
        assert str(circle.perimeter) == "Wrong parameters of figure"

    def test_check_area_perimeter_uncorrect_length_side(self):
        circle = Figure('circle', 0, r=-100)
        assert str(circle.area) == "Wrong parameters of figure"
        assert str(circle.perimeter) == "Wrong parameters of figure"
