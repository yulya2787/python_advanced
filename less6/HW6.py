"""
Создать консольную программу-парсер, с выводом прогноза погоды. Дать
возможность пользователю получить прогноз погоды в его локации ( по
умолчанию) и в выбраной локации, на определенную пользователем дату.
Можно реализовать, как консольную программу, так и веб страницу.
Используемые инструменты: requests, beatifulsoup, остальное по желанию.
На выбор можно спарсить страницу, либо же использовать какой-либо API.
"""

import requests as r
from bs4 import BeautifulSoup

class Weather:
    URL = 'https://sinoptik.ua'
    DAYS = {
        0: 'today',
        1: 'tomorrow',
        2: 'after_tomorrow',
        3: 'in 3 days',
        4: 'in 4 days',
        5: 'in 5 days',
        6: 'in 6 days',
        7: 'in 7 days'
    }

    def __init__(self, city=None):
        self.city = city
        self.url = f'{self.URL}{f"/погода-{city}" if city else ""}'
        self.weather = self.get_weather(self.url)

    def get_weather(self, url):
        page = r.get(url)


        soup = BeautifulSoup(page.content, 'html.parser')

        return_ = {}
        weather_by_day = {}
        return_['city'] = soup.find('div', class_="cityName cityNameShort").find('h1').get_text().strip()
        for index, day_soup in enumerate(soup.find_all('div', class_='main')):
            wd = {}
            date = f"{day_soup.find(class_='day-link').get_text()}, \
            {day_soup.find(class_='date').get_text()} {day_soup.find(class_='month').get_text()}"
            sky = day_soup.find_all('div', class_='weatherIco')[0]['title']
            temperature = day_soup.find(class_='temperature').get_text().strip()
            wd["date"] = date
            wd["sky"] = sky
            wd["temperature"] = temperature
            weather_by_day[index] = wd

        return_['forecast'] = weather_by_day
        return return_

    def print_weather_for_N_day(self, day=0):
        print(f'{self.weather["city"]} на {self.DAYS[day]}:')
        wd = self.weather['forecast'][day]
        print(wd['date'], wd['sky'], wd['temperature'], sep=', ')


if __name__ == '__main__':
    weather = Weather()

    default = True
    while True:
        if default:
            weather.print_weather_for_N_day()
            default = False

        choice = input(
            'Which day?(0-7)* City?(г)\n*0-7: choose from 1 to 7\n').lower().strip()
        if len(choice) == 1 and ('0' <= choice <= '9'):
            weather.print_weather_for_N_day(int(choice))
        elif choice == 'r':
            city = input('City: ').lower().strip()
            prev_weather = weather
            weather = Weather(city=city)
            del prev_weather
            default = True

