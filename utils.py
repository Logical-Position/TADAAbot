import os
from tkinter import filedialog

# TODO Get complete list of all possible export files that analysts use in TA

target_hint_files = ['external_url_redirect_broken__4xx_or_5xx',
                     'broken_internal_urls',
                     'h1__tag_is_empty',
                     'external_redirected_urls',
                     'images_with_missing_alt_text',
                     'internal_redirected_urls',
                     'meta_description_is_empty',
                     'meta_description_is_missing',
                     'url_is_orphaned_and_was_not_found_by_the_crawler',
                     'urls_with_duplicate_meta_descriptions',
                     'urls_with_duplicate_page_titles',
                     ]


# TODO Replace hardcoded exports path with filedialog.askdirectory()

def walk_exports_folder():  # Asks for Sitebulb export folder and can return paths for
    # all files/folders in the Sitebulb directory, if necessary.
    main_exports_path = '/Users/applehand/Desktop/creationnet-exports'  # Hardcoded export path for faster testing
    if main_exports_path.endswith('exports'):
        hints_path = main_exports_path + '/hints'
        bot_hints_path = main_exports_path + '/bot-hints'
        master_xls_path = main_exports_path + '/master.xlsx'

        walk_paths = os.walk(main_exports_path)  # Currently the paths are hardcoded, but they can be accessed via walk

        return [main_exports_path, hints_path, bot_hints_path, master_xls_path]
    else:
        print('Choose the main exports folder from the Sitebulb ZIP.')
        return [False, False, False, False]  # If the main exports folder isn't chosen, it returns a list of
        # False elements to be unpacked on main which stops the process from progressing.


def match_target_hint_files(hints_path):  # Returns a list of the found hint files
    found_hint_files = []
    all_hint_file_names = os.listdir(hints_path)
    for file_name in all_hint_file_names:
        for possible_file in target_hint_files:
            if possible_file in file_name:
                target_hint_files.remove(possible_file)
                found_hint_files.append(file_name)

    not_found_hint_files = target_hint_files

    print(f'Found target hint files: {found_hint_files}')
    print(f'Not found target hint files: {not_found_hint_files}')

    return found_hint_files


def create_bot_hints_folder(bot_hints_path):  # Creates a bot-hints folder.
    os.mkdir(bot_hints_path)


def clear_bot_work():  # Deletes folders and files created by the operation, for a clean restart.
    pass


def optimize_file_name(target_name, bot_hints_path, hints_path):  # Cleans up file paths to get a short file name.
    if bot_hints_path in target_name:
        target_name = target_name.replace(bot_hints_path + '/', '')
    elif hints_path in target_name:
        target_name = target_name.replace(hints_path + '/', '')
    if target_name.endswith('.csv'):
        target_name = target_name[:-4]
    elif target_name.endswith('.xlsx'):
        target_name = target_name[:-5]
    while len(target_name) > 31:
        target_name = target_name[1:]

    return target_name
