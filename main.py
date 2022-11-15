import os.path

import utils
import gui
import xls

# TODO Update Python version to 3.11
target_domain = ''

export_path, hints_path, bot_hints_path, master_xls_path = utils.walk_exports_folder()  # Walks through Sitebulb folder
# to get file paths. Function returns a list of file path variables that are unpacked.

if export_path:  # Allows process to continue if correct folder is selected.
    is_bot_hints_created = os.path.exists(bot_hints_path)  # Checks if /bot-hints folder exists

    if not is_bot_hints_created:
        utils.create_bot_hints_folder(bot_hints_path)  # Creates a bot-hints folder if none exists
    else:
        print('Bot hints folder already exists.')

    matched_hint_files = utils.match_target_hint_files(hints_path)  # Reads file names in hints folder and matches them
    # against those required in the tech audit. Returns matched file names in a list.

    if 'master.xlsx' not in os.listdir(export_path):
        master_xls_obj = xls.create_master_xls(matched_hint_files, export_path, hints_path, bot_hints_path)  # Takes the list of matched hint files
        # and creates the master spreadsheet with a sheet for each file.
    else:
        print('Master spreadsheet already exists.')
        master_xls_obj = xls.get_master_xls_obj(master_xls_path)

    csv_file_paths = xls.get_csv_paths(matched_hint_files, hints_path)  # Takes matched hint paths and returns csv paths

    xl_file_paths = xls.create_target_xls_paths(csv_file_paths)  # Tweaks csv file paths to allow the xls files
    # to be created in the /bot-hints folder.

    num_files_in_bot_hints = len(os.listdir(bot_hints_path))  # Gets num of files in bot-hints

    if num_files_in_bot_hints < 2:  # hidden mac file makes bot-hints always contain at least 1 file
        xls.create_xls_from_csv_paths(csv_file_paths, xl_file_paths)  # Creates an Excel worksheet in /bot-hints
        # for each csv_path.
    else:
        print('bot-hints folder is not empty.')

    xls_data = xls.get_all_xls_data(xl_file_paths, bot_hints_path, hints_path)  # Reads data from each xls
    # in bot-hints and returns it in this data structure: [{name: [data]}, {name: [data]}]

    for sheet in master_xls_obj.worksheets[1:]:  # Checks if master sub-sheet (minus overview) have data
        if sheet.calculate_dimension() == 'A1:A1':
            xls.transfer_xls_data_to_master(xls_data, master_xls_obj, export_path)  # Takes all xls data, matches it to the proper
            # master sub-sheet using the key, and places all the data into the master sheet.
            break
        else:
            print('Data already exists in master sub-sheets.')
            break
