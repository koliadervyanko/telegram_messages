import csv

from src.dto.csv_data_dto import CsvDataDto


class CsvParser:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__file = open(file_name, "r", encoding="cp1251")
        self.__reader = csv.reader(self.__file, delimiter=';')

    def parse(self):
        try:
            links = []
            key_words = []
            next(self.__reader)
            for row in self.__reader:
                if len(row) >= 2:
                    link = row[0]
                    key_word = row[1]
                    if link != "":
                        links.append(link)
                    if key_word != "":
                        key_words.append(key_word)

            return CsvDataDto(links, key_words)

        except Exception as e:
            print(e)
