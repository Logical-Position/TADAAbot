import os.path
import utils
import xls


export_path, hints_path, bot_hints_path, master_xls_path = utils.walk_exports_folder('exports_folder')

if export_path:
    is_bot_hints_created = os.path.exists(bot_hints_path)
    if not is_bot_hints_created:
        os.mkdir(bot_hints_path)
    else:
        print('Bot hints folder already exists.')

    matched_hint_files = utils.match_target_hint_files(hints_path)

    if 'master.xlsx' not in os.listdir(export_path):
        master_xls_obj = xls.create_master_xls(matched_hint_files, export_path, hints_path, bot_hints_path)
    else:
        print('Master spreadsheet already exists.')
        master_xls_obj = xls.get_master_xls_obj(master_xls_path)

    csv_file_paths = xls.get_csv_paths(matched_hint_files, hints_path)

    xl_file_paths = xls.create_target_xls_paths(csv_file_paths)

    num_files_in_bot_hints = len(os.listdir(bot_hints_path))

    if num_files_in_bot_hints < 2:
        xls.create_xls_from_csv_paths(csv_file_paths, xl_file_paths)
    else:
        print('bot-hints folder is not empty.')

    xls_data = xls.get_all_xls_data(xl_file_paths, bot_hints_path, hints_path)

    for sheet in master_xls_obj.worksheets[1:]:
        if sheet.calculate_dimension() == 'A1:A1':
            xls.transfer_xls_data_to_master(xls_data, master_xls_obj, export_path)
            break
        else:
            print('Data already exists in master sub-sheets.')
            break

    utils.calc_totals(master_xls_obj)
