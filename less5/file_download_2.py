import requests
from threading import Thread
import time

link1 = 'https://en.wikipedia.org/wiki/File:Python_logo_and_wordmark.svg'
link2 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link3 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link4 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link5 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link6 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link7 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link8 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link9 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
link10 = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

links_list = [link1, link2, link3, link4, link5, link6, link7, link8, link9, link10]


def my_links_decorator(custom_function):

    def wrapper(list, i):
        thread_list = []
        for x in list:
            print(f"file started to be downloaded from link {list.index(x)} ")
            thread_num = Thread(target = custom_function, args = (list, i, ), daemon = False)
            thread_list.append(thread_num)
            thread_num.start()
            thread_num.join()
            while thread_num.is_alive():
                print('file download is in progress')
                time.sleep(2)
            print(f'file {list.index(x)} has been downloaded as link_{i}')


    return wrapper

@my_links_decorator
def download_link(list, i):

    links_from_list = i[0]
    request = requests.get(list[links_from_list])
    status = request.status_code
    if status == 200:
        with open(str(i[0]), 'wb') as liks_opened:
            liks_opened.write(request.content)
    else: print("connection error")
    i.pop(0)


i = [x for x in range(10)]
download_link(links_list, i)