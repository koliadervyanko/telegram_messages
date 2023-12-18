import pandas as pd

from src.dto.csv_data_dto import CsvDataDto


class CsvParser:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__df = pd.read_csv(file_name, encoding="cp1251", on_bad_lines='skip')

    def parse(self):
        try:
            links = self.__get_links()
            key_words = self.__get_ley_words()
            return CsvDataDto(links, key_words)
        except Exception as e:
            print(e)

    def __get_ley_words(self):
        key_words = []
        for line in self.__df.values:
            values = line[0].split(";")
            if values[1] != "":
                key_words.append(values[1])
        return key_words

    def __get_links(self):
        links = []
        for line in self.__df.values:
            values = line[0].split(";")
            if values[0] != "":
                links.append(values[0])
        return links
