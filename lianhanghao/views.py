import requests
from lxml import etree


def insert_data(item):
    file = open("data.txt", "a+", encoding="utf-8")
    file.write(item + "\n")
    file.close()


if __name__ == '__main__':
    for item in range(0, 15385):
        response = requests.get("http://www.lianhanghao.com/index.php/Index/index/p/%s.html" % item)
        # data = json.loads(response.text)
        # response = requests.get(index_url)
        # data = BeautifulSoup(response.text, 'html.parser')
        contents = response.content.decode('utf-8')
        # href_list = data.findAll('div', class_='width_11 auto list3')

        html = etree.HTML(contents)
        href_list = html.xpath("//table/tbody/tr/td/text()")
        for i in href_list:
            print(i)
            insert_data(i)

