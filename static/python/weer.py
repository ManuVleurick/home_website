from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import os
import datetime

WEER_URL = 'https://www.buienradar.be/weer/gent/be/2797656'
DRIVER_PATH = r'C:\Users\manuv\Documents\Projecten\Resources\geckodriver.exe'


def get_weather_data_now():
    soup,driver = ini_webscraper()
    temp = soup.find('td', text='Temperatuur').next_sibling.next_sibling.text
    regen_mm = soup.find('td', text='Regen').next_sibling.next_sibling.text
    lucht_vochtigheid = soup.find('td', text='Luchtvochtigheid ').next_sibling.next_sibling.text
    windkracht = soup.find_all('tr',class_='place-desktop')[2]
    windkracht = str(windkracht.find('div',class_='panel').next_element.next_element.next_element).strip()
    windrichting = str(soup.find('td', text='Windrichting').next_sibling.next_sibling.next_element.next_element.next_element).strip()

    now = datetime.datetime.now()
    driver.close()
    weer_dict = {'day': get_day_string(now.isoweekday()),'time':get_hour_min(now),'temp':temp,'regen_mm':regen_mm,'lucht_vochtigheid':lucht_vochtigheid,'windkracht':windkracht,'windrichting':windrichting}
    return weer_dict

def print_weather_data(titel, temp='Niet gegeven', regen_mm='Niet gegeven',lucht_vochtigheid='Niet gegeven',windkracht='Niet gegeven',windrichting='Niet gegeven'):
    os.system('cls')
    print(titel+'\n')
    print(f'Temperatuur: {temp}')
    print(f'Regen: {regen_mm}')
    print(f'Luchtvochtigheid: {lucht_vochtigheid}')
    print(f'Windkracht: {windkracht}')
    print(f'Windrichting: {windrichting}')



def ini_webscraper():
    firefox_options = Options()
    firefox_options.add_argument('-headless')
    firefox_options.add_argument('-incognito')
    driver = webdriver.Firefox(
        executable_path=DRIVER_PATH, options=firefox_options)
    print('Getting weather data...')
    driver.get(WEER_URL)
    return (BeautifulSoup(driver.page_source, 'lxml'),driver)

def get_hour_min(now):
    if now.minute>9:
        return f'{now.hour}:{now.minute}'
    return f'{now.hour}:0{now.minute}'

def get_day_string(weekofday):
    if weekofday == 1:
        return 'Monday'
    elif weekofday == 2:
        return 'Tuesday'
    elif weekofday == 3:
        return 'Wednesday'
    elif weekofday == 4:
        return 'Thursday'
    elif weekofday == 5:
        return 'Friday'
    elif weekofday == 6:
        return 'Saterday'
    elif weekofday == 7:
        return 'Sunday'
