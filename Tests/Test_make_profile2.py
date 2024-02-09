import numpy as np
import pytest
import sys
sys.path.append('C:/Users/Александр/Desktop/Python/make_profile')
sys.path.append('C:/Users/Александр/Desktop/Python/app')
from folium import Polygon

#test1
# Этот тест берет на входе еденичный полигон в виде квадрата и вычисляет среднюю высоту его вершин
def test_mean_elevation():
    def get_mean_elevation(polygons):
        bounding_geometry = [[[-122.38, 37.78], [-122.38, 37.88], [-122.28, 37.88], [-122.28, 37.78], [-122.38, 37.78]]]
        expected_mean_elevation = 37.78
        actual_mean_elevation = get_mean_elevation(bounding_geometry)
        assert expected_mean_elevation == actual_mean_elevation

if __name__ == '__main__':
    pytest.main()

#test2
def profile_mean_soil_content(polygons):
    # Функция принимает аргумент в виде полигона, который, как ожидается, бует списком координат, опрееляющий многоугольник.
    #Функция создает многоугольник, используя предоставленые координаты, а затем вызывает "profile_mean_soil_content" c этим многоугольником. Ожидаемый результат - список, содержимое которого - среднее содержание почвы.
    polygon = [[[-122.419418, 37.774929], [-122.419418, 37.811371], [-122.382976, 37.811371], [-122.382976, 37.774929], [-122.419418, 37.774929]]]
    expected_result = {"Sand": 44.644, "Clay": 28.944, "Organic Matter": 17.414, "Other": 6.882}

    result = profile_mean_soil_content(polygon)
    return result

def test_profile_mean_soil_content():
    def profile_mean_soil_content(polygons):
        # В данном тесте функция "profile_mean_soil_content" с аргументов в виде многоугольников, которые представляют как один, затем вызывает себя с полученным многоугольником и возвраает список с содержанием почвы. 
        #Затем функция "test_profile_mean_soil_content" сравнивает возвращенный список с ожидаемым резултатом.
        result = profile_mean_soil_content(Polygon(polygons))
        expected_result = {"Sand": 44.644, "Clay": 28.944, "Organic Matter": 17.414, "Other": 6.882}
        assert result == expected_result


if __name__ == '__main__':
    pytest.main()


#test3
#Тест для функции определения средней температуры
#"Bounding_geometry" является списком координат, которые определяют полигон.
#Затем функция вызывает функциюю "get_mean_temp" с переменными "bounding_geometry" в качестве аргумента. Функция присвает возвращаемое значение переменноц "mean_temp".
#Строка 52 сравнивает значение "mean_temp" с ожидаемым значением в 57.2 градуса, с допуском в 0.1 градус.
def test_mean_temp():
    def get_mean_temp(bounding_geometry):
        bounding_geometry = [[[-122.4194, 37.7749], [-122.4194, 37.8324], [-122.3619, 37.8324], [-122.3619, 37.7749], [-122.4194, 37.7749]]]
        mean_temp = get_mean_temp(bounding_geometry)
        np.testing.assert_allclose(mean_temp, 57.2, atol=1e-1)

if __name__ == '__main__':
    pytest.main()
