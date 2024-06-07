from src.class_abstractapi import AbstractAPI
import requests


class HeadHunterAPI(AbstractAPI):
    """Подключается к API hh.ru и возврвщает данные о вакансиях"""

    def __init__(self, url, page=0, area=113):
        super().__init__(url)
        self.vacancies = []
        self.params = {'text': '', 'page': page, 'area': area}

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while True:
            # self.params['page'] = page
            response = requests.get(self.url, params=self.params)
            data = response.json()
            vacancies = data.get('items', [])
            if not vacancies:
                break
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies


if __name__ == "__main__":
    hh_api = HeadHunterAPI("https://api.hh.ru/vacancies")
    l_h = hh_api.get_vacancies("Python")
    print(len(l_h))
    # for l in l_h:
    #     print(l.get('salary'))
