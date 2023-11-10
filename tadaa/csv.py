from tadaa import ppt as pp
import pandas as pd

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

data_keys = {
    'broken-4xx-5xx': 'broken__4xx_or_5xx',
    'broken-internal': 'broken_internal_urls',
    'broken-external': 'broken_external_urls',
    'empty-h1': 'h1__tag_is_empty',
    'duplicate-h1': 'urls_with_duplicate_h1',
    'redirected-external': 'external_redirected_urls',
    'missing-alt-text': 'missing_alt_text',
    'redirected-internal': 'internal_redirected_urls',
    'empty-desc': 'description_is_empty',
    'missing-desc': 'description_is_missing',
    'too-long-desc': 'description_length_too_long',
    'too-short-desc': 'description_length_too_short',
    'not-found': 'not_found_by_the_crawler',
    'duplicate-desc': 'duplicate_meta_descriptions',
    'too-long-title': 'title_tag_length_too_long',
    'too-short-title': 'title_tag_length_too_short',
    'duplicate-title': 'duplicate_page_titles',
    'sitemap-url-inmultiple': 'url_in_multiple_xml_sitemaps',
    'sitemap-url-noindex': 'noindex_url_in_xml_sitemaps',
    'sitemap-url-redirect-3xx': 'redirect__3xx__url_in_xml_sitemaps'
}


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

def parse_sitebulb_csvs(sitebulb_file_paths, target_export_files):
    """
    Takes the matched paths to the target csv files, reads into each file using Pandas, forms our custom data object, and returns it.

    @param sitebulb_file_paths: absolute paths to the matched target csv files that are used in the tech audit.

    @return audit_results: our custom data object that is a dictionary ({target_file_name: data}) that includes data as pandas dataframe/series objects.
    """
    
    sitebulb_data = {}
    
    for path in sitebulb_file_paths:
        for target_file in target_export_files:
            if target_file in path:
                dataframe = pd.read_csv(path)
                sitebulb_data[target_file] = dataframe.shape[0] # {key, num of rows}

    print('=== SITEBULB DATA ===')
    print(sitebulb_data)
    print('')
    print('')
    return sitebulb_data


    #     if 'broken__4xx_or_5xx' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         parent_urls = df['First Parent URL']

    #         pp.broken_4xx_5xx = int(urls.count())
    #         audit_results['broken_4xx_5xx'] = int(urls.count())

    #         data.append(urls)
    #         data.append(parent_urls)
    #         data_obj.update({'broken__4xx_or_5xx': data})

    #         #final_data_obj.update(data_obj)


    #     if 'broken_internal_urls' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         parent_urls = df['First Parent URL']

    #         pp.broken_int_links = int(urls.count())
    #         audit_results['broken_int_links'] = int(urls.count())

    #         data.append(urls)
    #         data.append(parent_urls)
    #         data_obj.update({'broken_internal_urls': data})

    #         #final_data_obj.update(data_obj)
            

    #     if 'broken_external_urls' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         parent_urls = df['First Parent URL']

    #         pp.broken_ext_links = int(urls.count())
    #         audit_results['broken_ext_links'] = int(urls.count())

    #         data.append(urls)
    #         data.append(parent_urls)
    #         data_obj.update({'broken_external_urls': data})

    #         #final_data_obj.update(data_obj)


    #     if 'h1__tag_is_empty' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.h1_tag_empty = int(urls.count())
    #         audit_results['h1_tag_empty'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'h1__tag_is_empty': data})

    #         #final_data_obj.update(data_obj)


    #     if 'urls_with_duplicate_h1' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         dup_urls = df['Duplicate URL']

    #         pp.duplicate_h1_tags = int(urls.count())
    #         audit_results['duplicate_h1_tags'] = int(urls.count())

    #         data.append(urls)
    #         data.append(dup_urls)
    #         data_obj.update({'urls_with_duplicate_h1': data})

    #         #final_data_obj.update(data_obj)


    #     if 'external_redirected_urls' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         parent_urls = df['First Parent URL']

    #         pp.ext_redirect_links = int(urls.count())
    #         audit_results['ext_redirect_links'] = int(urls.count())

    #         data.append(urls)
    #         data.append(parent_urls)
    #         data_obj.update({'external_redirected_urls': data})

    #         #final_data_obj.update(data_obj)


    #     if 'missing_alt_text' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['HTML URL']
    #         image_urls = df['Image URL']

    #         pp.img_alt_text = int(urls.count())
    #         audit_results['img_alt_text'] = int(urls.count())

    #         data.append(urls)
    #         data.append(image_urls)
    #         data_obj.update({'missing_alt_text': data})

    #         #final_data_obj.update(data_obj)


    #     if 'internal_redirected_urls' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         parent_urls = df['First Parent URL']

    #         pp.int_redirect_links = int(urls.count())
    #         audit_results['int_redirect_links'] = int(urls.count())

    #         data.append(urls)
    #         data.append(parent_urls)
    #         data_obj.update({'internal_redirected_urls': data})

    #         #final_data_obj.update(data_obj)


    #     if 'description_is_empty' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.desc_empty = int(urls.count())
    #         audit_results['desc_empty'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'description_is_empty': data})

    #         #final_data_obj.update(data_obj)


    #     if 'description_is_missing' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.desc_missing = int(urls.count())
    #         audit_results['desc_missing'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'description_is_missing': data})

    #         #final_data_obj.update(data_obj)


    #     if 'description_length_too_long' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.desc_too_long = int(urls.count())
    #         audit_results['desc_too_long'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'description_length_is_too_long': data})

    #         #final_data_obj.update(data_obj)


    #     if 'description_length_too_short' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.desc_too_short = int(urls.count())
    #         audit_results['desc_too_short'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'description_length_is_too_short': data})

    #         #final_data_obj.update(data_obj)


    #     if 'not_found_by_the_crawler' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.orphaned_pages = int(urls.count())
    #         audit_results['orphaned_pages'] = int(urls.count())
    #         pp.sitemap_errors = int(urls.count())
    #         audit_results['sitemap_errors'] += int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'not_found_by_the_crawler': data})

    #         #final_data_obj.update(data_obj)


    #     if 'duplicate_meta_descriptions' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         dup_urls = df['Duplicate URL']

    #         pp.duplicate_desc = int(urls.count())
    #         audit_results['duplicate_desc'] = int(urls.count())

    #         data.append(urls)
    #         data.append(dup_urls)
    #         data_obj.update({'duplicate_meta_descriptions': data})

    #         #final_data_obj.update(data_obj)


    #     if 'title_tag_length_too_long' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.titles_too_long = int(urls.count())
    #         audit_results['titles_too_long'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'title_tag_length_too_long': data})

    #         #final_data_obj.update(data_obj)


    #     if 'title_tag_length_too_short' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.titles_too_short = int(urls.count())
    #         audit_results['titles_too_short'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'title_tag_length_too_short': data})

    #         #final_data_obj.update(data_obj)


    #     if 'duplicate_page_titles' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']
    #         dup_urls = df['Duplicate URL']

    #         pp.duplicate_titles = int(urls.count())
    #         audit_results['duplicate_titles'] = int(urls.count())

    #         data.append(urls)
    #         data.append(dup_urls)
    #         data_obj.update({'duplicate_page_titles': data})

    #         #final_data_obj.update(data_obj)


    #     if 'url_in_multiple_xml_sitemaps' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.urls_in_multiple_sitemaps = int(urls.count())
    #         audit_results['urls_in_multiple_sitemaps'] = int(urls.count())
    #         pp.sitemap_errors += int(urls.count())
    #         audit_results['sitemap_errors'] += int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'url_in_multiple_xml_sitemaps': data})

    #         #final_data_obj.update(data_obj)


    #     if 'noindex_url_in_xml_sitemaps' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.noindex_urls_in_sitemap = int(urls.count())
    #         audit_results['noindex_urls_in_sitemap'] = int(urls.count())
    #         pp.sitemap_errors += int(urls.count())
    #         audit_results['sitemap_errors'] = int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'noindex_url_in_xml_sitemaps': data})

    #         #final_data_obj.update(data_obj)


    #     if 'redirect__3xx__url_in_xml_sitemaps' in path:
    #         data_obj, data = {}, []
    #         df = pd.read_csv(path)

    #         urls = df['URL']

    #         pp.redirects_in_sitemap = int(urls.count())
    #         audit_results['redirects_in_sitemap'] = int(urls.count())
    #         pp.sitemap_errors += int(urls.count())
    #         audit_results['sitemap_errors'] += int(urls.count())

    #         data.append(urls)
    #         data_obj.update({'redirect__3xx__url_in_xml_sitemaps': data})

    #         #final_data_obj.update(data_obj)

    # return audit_results
