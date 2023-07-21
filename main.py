import time

from query import get_href_work, get_href_company, get_company_info
from writer import write_company_info_to_csv

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    url = "https://work.ua"
    file_path_csv = "info.csv"
    list_vacancy = []
    list_company = []

    page_start = 1 # min = 1
    page_end = 2 # max = 350

    for page_number in range(page_start, page_end):
        href_values = get_href_work(page=page_number, headers=headers)
        list_vacancy.extend(href_values)
    print('vacancy-done')
    for i in list_vacancy:
        url_vacancy = url + i
        company_href = get_href_company(url=url_vacancy, headers=headers)
        list_company.extend(company_href)
    print('company-done')
    for i in list_company:
        url_company = url + i
        company_info = get_company_info(url=url_company, headers=headers)
        write_company_info_to_csv(info=company_info, file_path=file_path_csv)
    print('csv_file-done')
