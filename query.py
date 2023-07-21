import requests
from bs4 import BeautifulSoup
import os

def get_href_work(page: int, headers: dict) -> list:
    url = f"https://www.work.ua/jobs-it/?page={page}"
    response = requests.get(url, headers=headers)
    values = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        if page < 8:
            job_divs = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link js-hot-block")
        else:
            job_divs = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link")

        for job_div in job_divs:
            job_link = job_div.find("a")["href"]
            values.append(job_link)

        return values
    else:
        print(f"Помилка {url}. Код відповіді:", response.status_code)


def get_href_company(url: str, headers: dict) -> list:
    response = requests.get(url, headers=headers)
    values = []

    if response.status_code == 200:
        company_soup = BeautifulSoup(response.content, "html.parser")
        company_p = company_soup.find("p", class_="text-indent text-muted add-top-sm")
        company_a = company_p.find("a")

        if company_a and "href" in company_a.attrs:
            company_link = company_a["href"]
            values.append(company_link)

        return values
    else:
        print(f"Помилка {url}. Код відповіді:", response.status_code)


def get_company_info(url: str, headers: dict) -> dict:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        company_soup = BeautifulSoup(response.content, "html.parser")

        company_name_h1 = company_soup.find("h1", class_="add-bottom-sm text-center")
        company_name = company_name_h1.text.strip() if company_name_h1 else ""

        try:
            company_href_a = company_soup.find("a", rel="nofollow", target="_blank")
            company_href = company_href_a["href"] if company_href_a else ""
        except Exception:
            company_href = ""

        try:
            company_phone_a = company_soup.find("a", href=lambda href: href.startswith("tel:"))
            company_phone = company_phone_a.text.strip() if company_phone_a else ""
        except Exception:
            company_phone = ""

        company_info = {
            "name": company_name,
            "href": company_href,
            "phone": company_phone
        }

        return company_info
    else:
        print(f"Помилка {url}. Код відповіді:", response.status_code)
