"""
上期所期权信息爬虫
"""


import csv
import datetime
import json
import os
import requests


DEFAULT_OUTPUT_DIR = "."


def save_shfe_option_data(date_: datetime.date, save_dir=DEFAULT_OUTPUT_DIR) -> None:

    url = f"http://www.shfe.com.cn/data/instrument/option/ContractBaseInfo{date_.strftime('%Y%m%d')}.dat"
    response = requests.get(url)
    text = response.text
    data = json.loads(text)

    info = data['OptionContractBaseInfo']
    save_path = os.path.join(DEFAULT_OUTPUT_DIR, "SHFE_options.csv")
    with open(save_path, 'w', newline='\n', encoding='gb2312') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
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

    save_shfe_option_data(datetime.date(2020, 5, 18))
