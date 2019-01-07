import os
import pandas as pd

import time

import math
from selenium import webdriver

# Chromeを操作
from _config import home_path, resources_path, driver_path

driver = webdriver.Chrome(executable_path=driver_path)


def get_review_per_40(url, page):
    fw_str = ''

    driver.get(url + '/reviews?page=' + str(page))
    time.sleep(3)
    content_texts = driver.find_elements_by_xpath("//div[@class='frame__main']/div[@class='frame__content']"
                                                  "/div[@class='frame__content__text']")
    date_list = driver.find_elements_by_xpath("//a[@class='frame__details__date frame__details__date--link']")
    users = driver.find_elements_by_class_name('frame__header')

    for i in range(len(content_texts)):
        text = content_texts[i].text.replace('\n', '').replace('"', '')
        user = users[i].text
        date = date_list[i].text

        if text[0:4] == 'ネタバレ':
            fw_str += '"' + date + '","' + user + '","true","' + text[4:] + '"\n'
        else:
            fw_str += '"' + date + '","' + user + '","false","' + text + '"\n'
    return fw_str


def open_book_top_page(title, id):
    url = 'https://bookmeter.com/books/'+id
    driver.get(url)
    time.sleep(3)
    review_count = driver.find_element_by_class_name('content__count').text
    page_max_count = math.ceil(int(review_count) / 40)
    print(page_max_count)

    with open(resources_path + '/book_meter/'+title+'.csv', 'w') as fw:
        fw.write('"date","user_name","netabare","text"\n')
        for page in range(page_max_count):
            fw.write(get_review_per_40(url, page))


if __name__ == '__main__':
    df = pd.read_csv(resources_path+'/booklist.csv',dtype=str)
    for i in range(len(df)):
        if not os.path.exists(resources_path + '/book_meter/' + df['title'][i] + '.csv'):
            open_book_top_page(df['title'][i],df['id'][i])
    driver.close()
