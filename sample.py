from fxfr import xmlfeed_read
from time import time

import psutil
import os
import time
import random
import string


def elapsed_since(start):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))


def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        mem_after = get_process_memory()
        print("{}: memory before: {:,}, after: {:,}, consumed: {:,}; exec time: {}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before,
            elapsed_time))
        return result

    return wrapper


@profile
def test(feed):
    elements_count = 0
    for item in xmlfeed_read(
        file_or_url=feed,
        iter_tag='product'
    ):
        elements_count += 1

    print("{} elements were processed".format(
        elements_count
    ))


def generate_random_word():
    letters = string.ascii_letters
    return u"".join(random.sample(letters, random.randint(5, 15)))


def generate_test_xml_file():

    tags = (
        'id', 'name', 'ean', 'type', 'description', 'brand', 'picture', 'gender'
    )
    with open('test.xml', 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><catalog>')
        for i in range(1, 1000000):
            f.write('<product>')
            for tag in tags:
                f.write('<{}>{}</{}>\n'.format(
                    tag,
                    generate_random_word(),
                    tag,
                ))
            f.write('</product>')
        f.write('</catalog>')


if __name__ == '__main__':

    generate_test_xml_file()
    test('./test.xml')
