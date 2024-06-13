import datetime as dt
import csv
import os

from .settings import (
    BASE_DIR,
    RES_DIR,
    RES_DIR_NAME,
    DT_FORMAT,
    HEAD_PEP_STATUS,
    FOOT_PEP_STATUS
    )


class PepParsePipeline:

    def __init__(self):
        RES_DIR.mkdir(exist_ok=True)
        self.statuses = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.statuses[item['status']] = self.statuses.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        now_time = dt.datetime.now().strftime(DT_FORMAT)
        file_name = f'{RES_DIR_NAME}/status_summary_{now_time}.csv'
        file_path = os.path.join(BASE_DIR, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            )
            writer.writerows(
                [
                    HEAD_PEP_STATUS,
                    *self.statuses.items(),
                    (FOOT_PEP_STATUS, sum(self.statuses.values())),
                ]
            )
