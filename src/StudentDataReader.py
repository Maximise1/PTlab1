from Types import DataType
import DataReader
import xml.etree.ElementTree as ET

class StudentDataReader(DataReader.DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        root = ET.parse(path).getroot()
        for student in root:
            for attr in student:
                if attr.tag == "name":
                    self.key = attr.text
                    self.students[self.key] = []
                else:
                    self.students[self.key].append((attr.tag,
                                                    int(attr.text)))
        return self.students
    
#new_class = StudentDataReader()
#students = new_class.read("data/student.xml")
#print(students)