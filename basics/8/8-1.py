import requests
import base64
from io import StringIO
import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement

USERNAME = b'youtianzhan@126.com'
PASSWORD = b'zx7iMk5z!ku7Xxp'


def download_csv(page_number):
    print('download csv data [page=%s]' % page_number)
    url = "http://api.intrinio.com/prices.csv?ticker=AAPL&hide_paging=true&page_size=200&page_number=%s" % page_number
    auth = b'Basic ' + base64.b64encode(b'%s:%s' % (USERNAME, PASSWORD))
    headers = {'Authorization': auth}
    response = requests.get(url=url, headers=headers)

    if response.ok:
        return StringIO(response.text)


def csv_to_xml(csv_file, xml_path):
    print('Convert csv data to %s' % xml_path)
    reader = csv.reader(csv_file)
    headers = next(reader)

    root = Element('Data')
    root.text = '\n\t'
    root.tail = '\n'

    for row in reader:
        book = SubElement(root, 'Row')
        book.text = '\n\t\t'
        book.tail = '\n\t'

        for tag, text in zip(headers, row):
            e = SubElement(book, tag)
            e.text = text
            e.tail = '\n\t\t'
        e.tail = '\n\t'
    ElementTree(root).write(xml_path, encoding='utf-8')


def downlaod_and_save(page_number, xml_path):
    # IO
    csv_file = None
    while not csv_file:
        csv_file = download_csv(page_number)
    # CPU
    csv_to_xml(csv_file, 'data%s.xml' % page_number)


if __name__ == '__main__':
    import time

    t0 = time.time()
    for i in range(1, 6):
        print(i)
        downlaod_and_save(i, 'data%s.xml' % i)
    print(time.time() - t0)
    print('main thread end')