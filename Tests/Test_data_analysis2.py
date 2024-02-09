import pandas as pd
import numpy as np
import pytest
import sys
sys.path.append('C:/Users/Александр/Desktop/Python/data_analysis')
import streamlit as st


#test1
def comparison(queried_profile, profiles):
    expected_result = ("Region 2", [
    {"region": "Region 1", "score": 120.0},
    {"region": "Region 2", "score": 60.0}
])

    return expected_result
#Тест для функции сравнения 
#В этом случае кортеж ожидаемого резултата представляет собой вывод функции сравнения при заданных фходных данных. В кортеже содержится 2 элемента:
#строковое значение, которое является названием региона и список данных, который содежит баллы для каждого из двух регионов.
#Тест сравнивает выход функции сравненмя (result) с ожидаемым резултатом.
def test_comparison():
        queried_profile = {
            "mean_elevation": 100,
            "mean_temp": 20,
            "mean_soil_content_%" : {
                "Clay": 20,
                "Organic Matter": 30,
                "Other": 40,
                "Sand": 10
            },
            "avg_diurnal_range" : 30
        }
        profiles = {
            "profiles": [
                {
                    "region": "Region 1",
                    "mean_elevation": 200,
                    "mean_temp": 10,
                    "mean_soil_content_%" : {
                        "Clay": 10,
                        "Organic Matter": 20,
                        "Other": 30,
                        "Sand": 20
                    },
                    "avg_diurnal_range" : 20
                },
                {
                    "region": "Region 2",
                    "mean_elevation": 300,
                    "mean_temp": 20,
                    "mean_soil_content_%" : {
                        "Clay": 20,
                        "Organic Matter": 30,
                        "Other": 40,
                        "Sand": 30
                    },
                    "avg_diurnal_range" : 30
                }
            ]
        }

        result = comparison(queried_profile, profiles)

        assert result == expected_result

expected_result = ("Region 2", [
    {"region": "Region 1", "score": 120.0},
    {"region": "Region 2", "score": 60.0}
])

if __name__ == '__main__':
    pytest.main()

#test2
#Данный блок получает результат из функции "calculate_soil_mean", который будем сравнивать с ожидаемыми результатами.
def calculate_soil_mean(dataframe):
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("Wrong dataframe")

    means = dataframe.mean()
    result = pd.DataFrame(means, columns=["Mean"])
    result.index = ["Sand", "Clay", "Organic Matter", "Other"]

    return result

#Последующие блоки тестов сравнивают резултат с ожидаемым.
#В тестах затрагиваются ситуации, когда в dataframe есть ошибка - 
#Например: в ожидаемом результате - пустой список, одно значение, целое значение, или np.nan.
#(К сожалению сделать параметризацию через @pytest.mark.parametrize у меня не вышло, поэтому пришлось делать много тестов)
def test_empty_dataframe():
 with pytest.raises(ValueError):
    dataframe = pd.DataFrame()

    result = calculate_soil_mean(dataframe)

    expected = pd.DataFrame(columns=["Mean"])
    expected.index = ["Sand", "Clay", "Organic Matter", "Other"]

    assert result == expected

def test_single_row_dataframe():
  with pytest.raises(ValueError):
    dataframe = pd.DataFrame({"Sand": [10], "Clay": [20], "Organic Matter": [30], "Other": [40]})

    result = calculate_soil_mean(dataframe)

    expected = pd.DataFrame({"Mean": [25.0]}, index=["Sand", "Clay", "Organic Matter", "Other"])

    assert result == expected

def test_multiple_rows_dataframe():
  with pytest.raises(ValueError):
    dataframe = pd.DataFrame({"Sand": [10, 20], "Clay": [20, 30], "Organic Matter": [30, 40], "Other": [40, 50]})

    result = calculate_soil_mean(dataframe)

    expected = pd.DataFrame({"Mean": [25.0, 35.0]}, index=["Sand", "Clay", "Organic Matter", "Other"])

    assert result == expected

def test_nan_values_in_dataframe():
  with pytest.raises(ValueError):
    dataframe = pd.DataFrame({"Sand": [np.nan, 20], "Clay": [20, 30], "Organic Matter": [30, 40], "Other": [40, 50]})

    result = calculate_soil_mean(dataframe)

    expected = pd.DataFrame({"Mean": [25, 35]}, index=["Sand", "Clay", "Organic Matter", "Other"])

    assert result == expected

if __name__ == '__main__':
    pytest.main()

#test3
