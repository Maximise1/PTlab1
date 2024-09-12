# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class FindBest:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def find(self) -> str:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
            for key in self.data:
                print("Ключ:", key, self.rating[key])
                if self.rating[key] == 100:
                    return key
        return "Таких студентов не найдено"
