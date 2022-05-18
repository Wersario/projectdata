import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from descriptions import key_words


LINK = 'https://api.hh.ru/vacancies/'
VACANCY = 'https://hh.ru/vacancy/'


def make_diagram(start, end):
    """
    Creates a circle diagram of ratio between unknown jobs, casual jobs, and programmer jobs.
    Needs 2 arguments: start - id of the first vacation and end - id of the last vacation. It will create an interval,
    where function will compare amounts.
    """
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
    fig, ax = plt.subplots()
    ax.pie(stats, labels=labels)
    ax.axis("equal")
    plt.pie(stats, labels=labels)


def get_vacancies(start, end):
    """
        Gives you all programmer vacancies in chosen interval. Needs 2 arguments: start - id of the first vacation and end
        - id of the last vacation.
    """
    for num in range(start, end):
        response = requests.get(LINK + str(num)).json()
        if response['description'] == 'Not Found':
            continue
        for word in key_words:
            if word in response['name'].lower():
                print(f'{response["name"]}, опыт работы: {response["experience"]["name"]}. Ссылка: {VACANCY + str(num)}')
    print('Больше вакансий нет')


def make_data_set(start, end):
    """
        Creates a data set about all vacancies.  Needs 2 arguments: start - id of the first vacation and end -
        id of the last vacation.
    """
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
        if response["description"] == 'Not Found':
            continue
        for word in key_words:
            if word in response['name'].lower():
                data['Name'].append(response['name'])
                if response['experience'] is None:
                    data['Experience'].append(np.nan)
                else:
                    data['Experience'].append(response['experience']['name'])
                if response['salary'] is None:
                    data['Salary'].append(np.nan)
                else:
                  if response['salary']['from'] is None:
                    data['Salary'].append(np.nan)
                  else:
                    data['Salary'].append(f"{response['salary']['from'] + response['salary']['currency']}")
                if response['address'] is None:
                    data['City'].append(np.nan)
                    data['Street'].append(np.nan)
                else:
                  if response['address']['city'] is None:
                    data['City'].append(np.nan)
                  else:
                    data['City'].append(response['address']['city'])
                  if response['address']['street'] is None:
                      data['Street'].append(np.nan)
                  else:
                      data['Street'].append(response['address']['street'])
                data['Link'].append(VACANCY + str(num))

    return pd.DataFrame(data)

    print(pd.DataFrame(data))


get_vacancies(1, 100000)