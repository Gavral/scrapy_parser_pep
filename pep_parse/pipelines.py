import csv
from collections import defaultdict
from pathlib import Path
from datetime import datetime as dt


DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
DATETIME = dt.now().strftime(DATETIME_FORMAT)
BASE_DIR = Path(__file__).parent.parent
STATUS_SUMMARY = f'status_summary_{DATETIME}.csv'


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.pep_statuses.values())
        report_file = BASE_DIR / 'results' / STATUS_SUMMARY
        with open(report_file, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.pep_statuses.items())
            writer.writerow(['Total', total])
