"""
大连商品交易所
期权合约信息爬虫
"""

import csv
from selenium import webdriver


DEFAULT_SAVE_PATH = ".\\DceOptionInfo.csv"
CHROME_WEBDRIVER = ".\\chromedriver_win32.exe"


def save_dce_option_data(save_path: str) -> None:

    url = "http://www.dce.com.cn/publicweb/businessguidelines/queryContractInfo.html"
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    w = webdriver.Chrome(CHROME_WEBDRIVER, options=option)

    try:
        w.get(url)
        data = w.find_element_by_xpath('//*[@id="printData"]/div/table/tbody').text
    except Exception:
        data = None
        print("Unable to get data from DCE website.")

    if data:
        lines = [x.split() for x in data.split('\n')]
        with open(save_path, 'w', newline='\n', encoding='gb2312') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            for line in lines:
                wr.writerow(line)
    else:
        print("No data to be written.")


if __name__ == '__main__':

    save_dce_option_data(DEFAULT_SAVE_PATH)
