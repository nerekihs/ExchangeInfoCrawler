"""
上海期货交易所
期权合约信息爬虫
"""


import csv
import datetime
import json
import requests


DEFAULT_SAVE_PATH = ".\\ShfeOptionInfo.csv"


def save_shfe_option_data(date_: datetime.date, save_path: str) -> None:

    url = f"http://www.shfe.com.cn/data/instrument/option/ContractBaseInfo{date_.strftime('%Y%m%d')}.dat"
    response = requests.get(url)
    text = response.text
    data = json.loads(text)
    info = data['OptionContractBaseInfo']

    with open(save_path, 'w', newline='\n', encoding='gb2312') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        rows = [
            'COMMODITYID', 'EXCHANGEID', 'EXPIREDATE', 'INSTRUMENTID',
            'OPENDATE', 'PRICETICK', 'SETTLEMENTGROUPID', 'TRADEUNIT',
            'TRADINGDAY', 'UPDATE_DATE', 'commodityName', 'id'
        ]
        wr.writerow(rows)
        for i in info:
            line = [i[x] for x in rows]
            wr.writerow(line)


if __name__ == '__main__':

    save_shfe_option_data(datetime.date(2020, 5, 27), DEFAULT_SAVE_PATH)