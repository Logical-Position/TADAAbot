import csv
from openpyxl import Workbook
from openpyxl import load_workbook
from utils import *


def create_master_xls(matched_hint_files, export_path, hints_path, bot_hints_path):  # Creates a master Excel spreadsheet in the main
    # Sitebulb exports folder with a sub-sheet for each matched hint file.
    master_xls_obj = Workbook()
    overview_sheet = master_xls_obj.active
    overview_sheet.title = 'Overview'
    print('Created master spreadsheet.')

    for file in matched_hint_files:
        target_sheet_name = optimize_file_name(file, bot_hints_path, hints_path)
        master_xls_obj.create_sheet(title=target_sheet_name)
        print(f'Added sheet to master: {target_sheet_name}')

    master_xls_obj.save(filename=export_path + '/master.xlsx')

    return master_xls_obj


def get_csv_paths(found_hint_files, hints_path):  # Takes hint paths and returns a list of csv paths
    csv_file_paths = []
    for csv_file_name in found_hint_files:
        csv_path = hints_path + '/' + csv_file_name
        csv_file_paths.append(csv_path)

    return csv_file_paths


def create_xls_from_csv_paths(csv_file_paths, xl_file_paths):  # Takes csv paths from hints and creates them as xls
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


def get_all_xls_data(xls_paths, bot_hints_path, hints_path):  # Gets all data from raw xls in bot-hints and returns it
    # as a list that contains a data dictionary for each xls, with the file name string as key.
    xls_data = []
    for path in xls_paths:
        target_name = optimize_file_name(path, bot_hints_path, hints_path)
        file = load_workbook(filename=path)
        sheet = file.active
        sheet_dict, sheet_data = {}, []
        for row in sheet.rows:
            sheet_data.append(row)
        sheet_dict.update({target_name: sheet_data})
        xls_data.append(sheet_dict)

    return xls_data


def transfer_xls_data_to_master(xls_data, master_xls_obj, export_path):
    for entry in xls_data:
        data_key = list(entry.keys())[0]
        entry_data = list(entry.values())[0]

        print(f'Adding data to {data_key} in master spreadsheet.')

        for i in entry_data:  # Accesses each element of tuple (columns of xl object)

            data_values = [data.value for data in i]  # makes list of values instead of cell objects
            # num_col = len(entry_data)
            # num_rows = entry_data[0].row

            for sheet in master_xls_obj:
                if data_key == sheet.title:
                    target_sheet = master_xls_obj[data_key]  # If key and sheet title match, appends data values.
                    target_sheet.append(data_values)

                # for r in range(1, num_rows + 1):  # Alternative process for transferring xl data, may need in future.
                #     for c in range(1, num_col + 1):
                #         for item in entry_data:
                #             target_sheet.cell(row=r, column=c).value = item(row=r, column=c).value

    master_xls_obj.save(filename=export_path + '/master.xlsx')


def get_master_xls_obj(master_xls_path):
    master_xls_obj = load_workbook(master_xls_path)

    return master_xls_obj
