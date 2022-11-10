import csv
from openpyxl import Workbook
from openpyxl import load_workbook
from utils import *


def create_master_xls(matched_hint_files, export_path, hints_path, bot_hints_path):  # Creates a master Excel spreadsheet in the main
    # Sitebulb exports folder with a sub-sheet for each matched hint file.
    master_xls = Workbook()
    print('Created master spreadsheet.')

    for file in matched_hint_files:
        target_sheet_name = optimize_file_name(file, bot_hints_path, hints_path)
        master_xls.create_sheet(title=target_sheet_name)
        print(f'Added sheet to master: {target_sheet_name}')

    master_xls.save(filename=export_path + '/master.xlsx')


def get_csv_paths(found_hint_files, hints_path):  # Takes hint paths and returns a list of csv paths
    csv_files = []
    for csv_file_name in found_hint_files:
        csv_path = hints_path + '/' + csv_file_name
        csv_files.append(csv_path)

    return csv_files


def create_raw_xls_from_csv_paths(csv_file_paths, xl_file_paths):  # Takes csv paths from hints and creates them as xls
    for index, csv_file_path in enumerate(csv_file_paths):
        csv_data = []
        with open(csv_file_path) as file_obj:
            reader = csv.reader(file_obj)
            for row in reader:
                csv_data.append(row)
        workbook = Workbook()
        sheet = workbook.active
        for row in csv_data:
            sheet.append(row)
        print(f'Created file: {xl_file_paths[index]}')
        workbook.save(xl_file_paths[index])


def create_target_xls_paths(csv_file_paths):  # Tweaks csv path strings to allow xls to be created in /bot-hints
    xl_file_paths = []
    for path in csv_file_paths:
        change_to_xlsx_path = path[:-4] + '.xlsx'
        final_xl_file_path = change_to_xlsx_path.replace('hints', 'bot-hints')
        xl_file_paths.append(final_xl_file_path)

    return xl_file_paths


# TODO Make function that puts data into proper master excel sub-sheet

def get_all_xls_data(xls_paths, bot_hints_path, hints_path):  # Gets all data from raw xls in bot-hints and returns it
    # as a list that contains a data dictionary for each xls, with the file name string as key.
    target_xls_data = []
    for path in xls_paths:
        target_name = optimize_file_name(path, bot_hints_path, hints_path)
        file = load_workbook(filename=path)
        sheet = file.active
        sheet_dict, sheet_data = {}, []
        for row in sheet.rows:
            sheet_data = [row]
        sheet_dict.update({target_name: sheet_data})
        target_xls_data.append(sheet_dict)

    return target_xls_data


def transfer_xls_data_to_master(all_sheets_data, master_path):
    print(all_sheets_data)
