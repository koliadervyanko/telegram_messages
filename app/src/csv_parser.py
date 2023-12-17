import csv

from .dto.csv_data_dto import CsvDataDto


class CsvParser:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__lines = list(csv.reader(open(self.__file_name, "r", encoding='cp1251')))

    def parse(self):
        try:
            links = self.__get_links()
            key_words = self.__get_key_words()
            return CsvDataDto(links, key_words)
        except Exception as e:
            print(e)

    def __get_links(self):
        links = []
        for line in self.__lines[1:]:
            values = line[0].split(";")
            link = values[0]
            if link != "":
                links.append(link)
        return links

    def __get_key_words(self):
        key_words = []
        for line in self.__lines[1:]:
            values = line[0].split(";")
            key_word = values[1]
            if key_word != '':
                key_words.append(key_word)
        return key_words
