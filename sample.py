from fxfr import xmlfeed_read
from time import time


if __name__ == '__main__':

    start_time = time()
    # todo: 1) url detect + stream 2) some big xml online find and add here
    # 3) local xml file?
    elements_count = 0
    for item in xmlfeed_read(
        file_or_url='?',
        iter_tag='product'
    ):
        elements_count += 1

    print("{} elements were processed within {} seconds.".format(
        elements_count,
        time() - start_time)
    )
