import csv
import datetime

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
            parsed_date = []
            for row in self.__reader:
                link = row[0]
                key_word = row[1]
                date = row[2]
                if date != "":
                    parsed_date.append(self.__get_date(date))

                if link != "":
                    links.append(link)
                if key_word != "":
                    key_words.append(key_word)
            return CsvDataDto(links, key_words, parsed_date[0].date())

        except Exception as e:
            print(e)

    @staticmethod
    def __get_date(date: str):
        values = date.split("/")
        date = datetime.datetime(int(values[0]), int(values[1]), int(values[2]))
        return date
