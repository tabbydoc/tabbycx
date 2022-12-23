from typing import List

from bs4 import BeautifulSoup as soup
from fastapi import UploadFile
from data_struct.table import Table
from utils import cache


def parse(file: UploadFile, xpath_filter=None) -> List[Table]:
    document = file.file.read()
    document = soup(document, 'html.parser')
    for table in document.select('table'):
        if len(table.select('tr')) < 2 or len(table.select('th,td')) < 4:
            table.decompose()
    for table in document.select('table'):
        if xpath_filter is None or table['data-xpath'] == xpath_filter:
            yield Table("local:file", "table['data-xpath']", table)
