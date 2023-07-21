import csv
def write_company_info_to_csv(info: dict, file_path: str):
    fieldnames = ['name', 'href', 'phone']

    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(info)