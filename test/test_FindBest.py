# -*- coding: utf-8 -*-
from src.Types import DataType
from src.FindBest import FindBest
import pytest

RatingsType = dict[str, float]


class TestFindBest:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 100),
                    ("русский язык", 100),
                    ("программирование", 100),
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000
        }

        return data, rating_scores

    def test_init_find_best(self, input_data: tuple[DataType,
                                                    RatingsType]) -> None:
        calc_rating = FindBest(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_find(self, input_data: tuple[DataType, RatingsType]) -> None:
        best_test = FindBest(input_data[0]).find()
        best_real = "Таких студентов не найдено"

        for student, grades in input_data[0].items():
            if (sum([x for _, x in grades])/len(grades) == 100):
                best_real = student
                break
        assert best_test == best_real
