# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.StudentDataReader import StudentDataReader


class TestTextDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "<root>\n<student>\n<name>Иванов Иван Иванович</name>\n" + \
            "<math>100</math>\n<programming>100</programming>\n<literature>" + \
            "100</literature>\n</student>\n<student>\n<name>Петров Петр Петр" + \
            "ович</name>\n<math>100</math>\n<sociology>90</sociology>\n<chemi" + \
            "stry>61</chemistry>\n</student>\n</root>\n"
        data = {
            "Иванов Иван Иванович": [
                ("math", 100), ("programming", 100), ("literature", 100)
            ],
            "Петров Петр Петрович": [
                ("math", 100), ("sociology", 90), ("chemistry", 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = StudentDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
