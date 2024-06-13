from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RES_DIR_NAME = 'results'
RES_DIR = BASE_DIR / RES_DIR_NAME

DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
HEAD_PEP_STATUS = ('Статус', 'Количество')
FOOT_PEP_STATUS = 'Total'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RES_DIR_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
