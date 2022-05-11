import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from descriptions import desc, key_words


LINK = 'https://api.hh.ru/vacancies/'
VACANCY = 'https://hh.ru/vacancy/'


def make_diagram(start, end):
    stats = np.array([0, 0, 0])
    labels = ['Unknown', 'Other Jobs', 'Programmers']
    check = 0
    for num in range(start, end):
        response = requests.get(LINK + str(num)).json()
        if response['description'] == 'Not Found':
            stats[0] += 1
            continue
        for word in key_words:
            if word in response['name'].lower():
                check = 1
                break
        if check == 1:
            stats[2] += 1
            check = 0
        else:
            stats[1] += 1

    plt.pie(stats, labels=labels)
    plt.show()


def get_vacancies(start, end):
    '''
        Gives you all programmer vacancies in chosen interval. Needs 2 arguments: start - id of the first vacation and end
        - id of the last vacation.
    '''
    for num in range(start, end):
        response = requests.get(LINK + str(num)).json()
        if response['description'] == 'Not Found':
            continue
        for word in key_words:
            if word in response['name'].lower():
                print(f'{response["name"]}, опыт работы: {response["experience"]["name"]}. Ссылка: {TEMPLATE + str(num)}')
     print('Больше вакансий нет')


def make_dataset(start, end):
    '''
        Creates a data set about all vacancies.  Needs 2 arguments: start - id of the first vacation and end -
        id of the last vacation.
    '''
    data = {
        'Name': [],
        'Experience': [],
        'Salary': [],
        'City': [],
        'Street': [],
        'Link': []
    }
    for num in range(start, end):
        response = requests.get(LINK + str(num)).json()
        if r.json()['description'] == 'Not Found':
            continue
        for word in key_words:
            if word in response['name'].lower():
                data['Name'].append(response['Name'])
                if response['experience'] is None:
                    data['Experience'].append(np.nan)
                else:
                    data['Experience'].append(response['experience'])
                if r.json()['salary']['from'] is None:
                    data['Salary'].append(np.nan)
                else:
                    data['Salary'].append(f"{response['salary']['from'] + r.json()['salary']['currency']}")
                if r.json()['address']['city'] is None:
                    data['City'].append(np.nan)
                else:
                    data['City'].append(response['address']['city'])
                if r.json()['address']['street'] is None:
                    data['Street'].append(np.nan)
                else:
                    data['Street'].append(response['address']['street'])
                data['Link'].append(TEMPLATE + str(num))

     print(pd.DataFrame(data))
