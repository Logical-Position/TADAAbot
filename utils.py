import ppt as pp
import pandas as pd

# TODO Get complete list of all possible export files that analysts use in TA

target_hint_files = [
    'external_url_redirect_broken__4xx_or_5xx',
    'broken_internal_urls',
    'broken_external_urls',
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
    'title_tag_length_too_long',
    'title_tag_length_too_short',
    'description_length_too_long',
    'description_length_too_short',
    'urls_with_duplicate_h1s'
]

data_fields = [
    'broken__4xx_or_5xx',
    'broken_internal_urls',
    'broken_external_urls',
    'h1__tag_is_empty',
    'urls_with_duplicate_h1',
    'external_redirected_urls',
    'missing_alt_text',
    'internal_redirected_urls',
    'description_is_empty',
    'description_is_missing',
    'description_length_too_long',
    'description_length_too_short',
    'not_found_by_the_crawler',
    'duplicate_meta_descriptions',
    'title_tag_length_too_long',
    'title_tag_length_too_short',
    'duplicate_page_titles',
    'url_in_multiple_xml_sitemaps',
    'noindex_url_in_xml_sitemaps',
    'redirect__3xx__url_in_xml_sitemaps'
]


def match_target_hint_files(all_uploaded_files):
    """
    Matches the necessary export files that are used in the tech audit. Returns a list of file paths to these matched files.
    @param [str] all_uploaded_files: the file paths in the uploaded directory as a list.
    @return [list] found_hint_files: a list of matched hint files that are used in the TA.
    """
    
    found_hint_files = []
    for file_name in all_uploaded_files:
        for possible_file in target_hint_files:
            if possible_file in file_name:
                target_hint_files.remove(possible_file)
                found_hint_files.append(file_name)

    not_found_hint_files = target_hint_files

    return found_hint_files


def get_abs_paths(matched_list, upload_dir):
    """
    Adds the upload directory file path to the file name.

    @param matched_paths: absolute paths to the matched target csv files that are used in the tech audit.

    @return final_data_obj: our custom data object that is a dictionary ({target_file_name: data}) that includes data as pandas dataframe/series objects.
    """
    abs_paths_list = []
    for file_name in matched_list:
        abs_path = upload_dir + '/' + file_name
        abs_paths_list.append(abs_path)
    
    return abs_paths_list


def get_data_obj(matched_paths):
    """
    Takes the matched paths to the target csv files, reads into each file using Pandas, forms our custom data object, and returns it.

    @param matched_paths: absolute paths to the matched target csv files that are used in the tech audit.

    @return final_data_obj: our custom data object that is a dictionary ({target_file_name: data}) that includes data as pandas dataframe/series objects.
    """
    
    final_data_obj = {}
    
    for path in matched_paths:

        if 'broken__4xx_or_5xx' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            parent_urls = df['First Parent URL']

            pp.broken_4xx_5xx = urls.count()

            data.append(urls)
            data.append(parent_urls)
            data_obj.update({'broken__4xx_or_5xx': data})

            final_data_obj.update(data_obj)


        if 'broken_internal_urls' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            parent_urls = df['First Parent URL']

            pp.broken_int_links = urls.count()

            data.append(urls)
            data.append(parent_urls)
            data_obj.update({'broken_internal_urls': data})

            final_data_obj.update(data_obj)
            

        if 'broken_external_urls' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            parent_urls = df['First Parent URL']

            pp.broken_ext_links = urls.count()

            data.append(urls)
            data.append(parent_urls)
            data_obj.update({'broken_external_urls': data})

            final_data_obj.update(data_obj)


        if 'h1__tag_is_empty' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.h1_tag_empty = urls.count()

            data.append(urls)
            data_obj.update({'h1__tag_is_empty': data})

            final_data_obj.update(data_obj)


        if 'urls_with_duplicate_h1' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            dup_urls = df['Duplicate URL']

            pp.duplicate_h1_tags = urls.count()

            data.append(urls)
            data.append(dup_urls)
            data_obj.update({'urls_with_duplicate_h1': data})

            final_data_obj.update(data_obj)


        if 'external_redirected_urls' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            parent_urls = df['First Parent URL']

            pp.ext_redirect_links = urls.count()

            data.append(urls)
            data.append(parent_urls)
            data_obj.update({'external_redirected_urls': data})

            final_data_obj.update(data_obj)


        if 'missing_alt_text' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['HTML URL']
            image_urls = df['Image URL']

            pp.img_alt_text = urls.count()

            data.append(urls)
            data.append(image_urls)
            data_obj.update({'missing_alt_text': data})

            final_data_obj.update(data_obj)


        if 'internal_redirected_urls' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            parent_urls = df['First Parent URL']

            pp.int_redirect_links = urls.count()

            data.append(urls)
            data.append(parent_urls)
            data_obj.update({'internal_redirected_urls': data})

            final_data_obj.update(data_obj)


        if 'description_is_empty' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.desc_empty = urls.count()

            data.append(urls)
            data_obj.update({'description_is_empty': data})

            final_data_obj.update(data_obj)


        if 'description_is_missing' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.desc_missing = urls.count()

            data.append(urls)
            data_obj.update({'description_is_missing': data})

            final_data_obj.update(data_obj)


        if 'description_length_too_long' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.desc_too_long = urls.count()

            data.append(urls)
            data_obj.update({'description_length_is_too_long': data})

            final_data_obj.update(data_obj)


        if 'description_length_too_short' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.desc_too_short = urls.count()

            data.append(urls)
            data_obj.update({'description_length_is_too_short': data})

            final_data_obj.update(data_obj)


        if 'not_found_by_the_crawler' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.orphaned_pages = urls.count()
            pp.sitemap_errors += urls.count()

            data.append(urls)
            data_obj.update({'not_found_by_the_crawler': data})

            final_data_obj.update(data_obj)


        if 'duplicate_meta_descriptions' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            dup_urls = df['Duplicate URL']

            pp.duplicate_desc = urls.count()

            data.append(urls)
            data.append(dup_urls)
            data_obj.update({'duplicate_meta_descriptions': data})

            final_data_obj.update(data_obj)


        if 'title_tag_length_too_long' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.titles_too_long = urls.count()

            data.append(urls)
            data_obj.update({'title_tag_length_too_long': data})

            final_data_obj.update(data_obj)


        if 'title_tag_length_too_short' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.titles_too_short = urls.count()

            data.append(urls)
            data_obj.update({'title_tag_length_too_short': data})

            final_data_obj.update(data_obj)


        if 'duplicate_page_titles' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']
            dup_urls = df['Duplicate URL']

            pp.duplicate_titles = urls.count()

            data.append(urls)
            data.append(dup_urls)
            data_obj.update({'duplicate_page_titles': data})

            final_data_obj.update(data_obj)


        if 'url_in_multiple_xml_sitemaps' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.urls_in_multiple_sitemaps = urls.count()
            pp.sitemap_errors += urls.count()

            data.append(urls)
            data_obj.update({'url_in_multiple_xml_sitemaps': data})

            final_data_obj.update(data_obj)


        if 'noindex_url_in_xml_sitemaps' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.noindex_urls_in_sitemap = urls.count()
            pp.sitemap_errors += urls.count()

            data.append(urls)
            data_obj.update({'noindex_url_in_xml_sitemaps': data})

            final_data_obj.update(data_obj)


        if 'redirect__3xx__url_in_xml_sitemaps' in path:
            data_obj, data = {}, []
            df = pd.read_csv(path)

            urls = df['URL']

            pp.redirects_in_sitemap = urls.count()
            pp.sitemap_errors += urls.count()

            data.append(urls)
            data_obj.update({'redirect__3xx__url_in_xml_sitemaps': data})

            final_data_obj.update(data_obj)


    return final_data_obj
