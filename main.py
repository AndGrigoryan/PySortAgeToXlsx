#!/usr/bin/env python3

import argparse
import xlsxwriter


def get_content(path):
    try:
        with open(path) as f:
            content = [tuple(line.strip().split(", ")) for line in f]
            return content
    except Exception as error:
        print(f"Error in get_content function: {error}")


def create_workbook():
    return xlsxwriter.Workbook("output.xlsx")


def add_data_to_sheet(workbook, data):
    worksheet = workbook.add_worksheet()
    
    for row_num, row_data in enumerate(data):
        worksheet.write_row(row_num, 0, row_data)


def save_workbook(workbook, filename):
    workbook.close()

    print(f'Data written to {filename}')


def main():

    parser = argparse.ArgumentParser(description='Process and sort data base on age.')

    parser.add_argument('--age', action='store_true', help='Sort data by age')

    args = parser.parse_args()

    path = 'data.txt'
    content = get_content(path)

    workbook = create_workbook()

    add_data_to_sheet(workbook, content)


    if args.age:
        content.sort(key=lambda x: x[1])

    add_data_to_sheet(workbook, content)

    save_workbook(workbook, "output.xlsx")
    
    
if __name__ == "__main__":
    main()

