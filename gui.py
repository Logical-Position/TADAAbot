from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


window = Tk()

possible_files = ['external_redirected_urls', 'broken_internal_urls', 'h1__tag_is_empty', 'external_redirected_urls', 'images_with_missing_alt_text', 'internal_redirected_urls', 'meta_description_is_empty', 'meta_description_is_missing', 'url_is_orphaned_and_was_not_found_by_the_crawler', 'urls_with_duplicate_meta_descriptions', 'urls_with_duplicate_page_titles']

def main_window():
    window.lift()
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)
    window.title('Tech Audit Technical')
    window.geometry("500x500")
    hints_button = Button(window, text='Select Hints Folder', command=get_hints)
    hints_button.pack()


def get_hints():
    hints_path = filedialog.askdirectory(title='Choose Hints Folder')
    if '/hints' in hints_path:
        all_hint_files = os.listdir(hints_path)
        for file in all_hint_files:
            if file == possible_files:
                print(f'{file} found.')
                possible_files.remove(file)
        print(f'These files were not found: {possible_files}')
    elif '/hints' not in hints_path:
        messagebox.showerror(title='Wrong Directory', message="Choose the 'hints' folder found within the Sitebulb "
                                                              "exports.")
