import os
import ppt as pp

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
                     'url_in_multiple_xml_sitemaps',
                     'noindex_url_in_xml_sitemaps',
                     'redirect__3xx__url_in_xml_sitemaps',
                     ]

# TODO Rework and rename walk_exports_folder function to align with web app and add documentation comment


def walk_exports_folder(exports_folder):
    main_exports_path = '/Users/applehand/Desktop/creationnet-exports'  # Hardcoded export path for faster testing
    if main_exports_path.endswith('exports'):
        hints_path = main_exports_path + '/hints'
        bot_hints_path = main_exports_path + '/bot-hints'
        master_xls_path = main_exports_path + '/master.xlsx'

        return [main_exports_path, hints_path, bot_hints_path, master_xls_path]
    else:
        print('Choose the main exports folder from the Sitebulb ZIP.')
        return [False, False, False, False]  # If the main exports folder isn't chosen, it returns a list of
        # False elements to be unpacked on main which stops the process from progressing.


def match_target_hint_files(hints_path):
    """
    Looks at all the export file paths inside the hints folder and matches them against a list of target file paths that
    are used in the tech audit. Returns a list of file path strings. Also prints a list of the leftover target file
    paths that were not matched.
    @param [str] hints_path: the path to the hints directory.
    @return [list] found_hint_files: a list of matched hint files that are used in the TA.
    """
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


def optimize_file_name(raw_path, bot_hints_path, hints_path):
    """
    Takes a file path and reworks it to be used as a cleaner name.
    @param [str] raw_path: the raw file path that is to be reworked.
    @param [str] bot_hints_path: the path to the bot_hints folder, so it can be removed from the path string.
    @param [str] hints_path: the path to the hints folder, so it can be removed from the path string.
    @return [str] target_name: the optimized string to be used as a file name.
    """
    if bot_hints_path in raw_path:
        raw_path = raw_path.replace(bot_hints_path + '/', '')
    elif hints_path in raw_path:
        raw_path = raw_path.replace(hints_path + '/', '')
    if raw_path.endswith('.csv'):
        raw_path = raw_path[:-4]
    elif raw_path.endswith('.xlsx'):
        raw_path = raw_path[:-5]
    while len(raw_path) > 31:
        raw_path = raw_path[1:]

    target_name = raw_path

    return target_name


def calc_totals(master_xls_obj):
    """
    Takes the master xls object and calculates various totals that are presented in the tech audit. Mostly counts rows.
    @param master_xls_obj:
    """
    for sheet in master_xls_obj:
        if 'broken__4xx_or_5xx' in sheet.title:
            for row in sheet.rows:
                pp.broken_4xx_5xx += 1
            pp.broken_4xx_5xx -= 1

        if 'broken_internal_urls' in sheet.title:
            for row in sheet.rows:
                pp.broken_int_links += 1
            pp.broken_int_links -= 1

        if 'h1__tag_is_empty' in sheet.title:
            for row in sheet.rows:
                pp.h1_tag_empty += 1
            pp.h1_tag_empty -= 1

        if 'external_redirected_urls' in sheet.title:
            for row in sheet.rows:
                pp.ext_redirect_links += 1
            pp.ext_redirect_links -= 1

        if 'missing_alt_text' in sheet.title:
            for row in sheet.rows:
                pp.img_alt_text += 1
            pp.img_alt_text -= 1

        if 'internal_redirected_urls' in sheet.title:
            for row in sheet.rows:
                pp.int_redirect_links += 1
            pp.int_redirect_links -= 1

        if 'description_is_empty' in sheet.title:
            for row in sheet.rows:
                pp.desc_empty += 1
            pp.desc_empty -= 1

        if 'description_is_missing' in sheet.title:
            for row in sheet.rows:
                pp.desc_missing += 1
            pp.desc_missing -= 1

        if 'not_found_by_the_crawler' in sheet.title:
            for row in sheet.rows:
                pp.orphaned_pages += 1
            pp.orphaned_pages -= 1

        if 'duplicate_meta_descriptions' in sheet.title:
            for row in sheet.rows:
                pp.duplicate_desc += 1
            pp.duplicate_desc -= 1

        if 'duplicate_page_titles' in sheet.title:
            for row in sheet.rows:
                pp.duplicate_titles += 1
            pp.duplicate_titles -= 1

        if 'url_in_multiple_xml_sitemaps' in sheet.title:
            for row in sheet.rows:
                pp.sitemap_errors += 1
                pp.urls_in_multiple_sitemaps += 1
            pp.sitemap_errors -= 1
            pp.urls_in_multiple_sitemaps -= 1

        if 'noindex_url_in_xml_sitemaps' in sheet.title:
            for row in sheet.rows:
                pp.sitemap_errors += 1
                pp.noindex_urls_in_sitemap += 1
            pp.sitemap_errors -= 1
            pp.noindex_urls_in_sitemap -= 1

        if 'redirect__3xx__url_in_xml_sitemaps' in sheet.title:
            for row in sheet.rows:
                pp.sitemap_errors += 1
                pp.redirects_in_sitemap += 1
            pp.sitemap_errors -= 1
            pp.redirects_in_sitemap -= 1


