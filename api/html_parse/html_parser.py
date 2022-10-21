from typing import List

from bs4 import BeautifulSoup
from fastapi import UploadFile

from data_struct.table import Table


def parse(file: UploadFile) -> List[Table]:
    contents = file.file.read()
    soup = BeautifulSoup(contents, "html.parser")
    tables = soup.findAll("table")
    result_tables = []
    for table in tables:
        data = []
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        result_tables.append(Table(data))
    print(result_tables)
    return result_tables
