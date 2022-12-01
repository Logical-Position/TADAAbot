from pptx import Presentation
from PyPDF2 import PdfReader

# Slide 8.
has_sc_access = bool
has_ga_access = bool

# Slide 10.
is_mobile_friendly = bool
num_mob_friendly_issues = 0

# Slide 11.
is_sitemap_submitted_sc = bool
sitemap_errors = 0
sitemap_location = None
orphaned_pages = 0
redirects_in_sitemap = 0
noindex_urls_in_sitemap = 0
urls_in_multiple_sitemaps = 0

# Slide 12.
has_robots = bool
robots_location = None

# Slide 15.
titles_too_long = 0
titles_too_short = 0
duplicate_titles = 0
titles_missing = 0

# Slide 16.
desc_too_long = 0
desc_too_short = 0
duplicate_desc = 0
desc_missing = 0
desc_empty = 0

# Slide 17.
duplicate_h1_tags = 0
h1_tag_empty = 0

# Slide 18.
has_duplicate_content = bool
has_thin_content = bool

# Slide 22.
img_alt_text = 0

# Slide 24.
broken_int_links = 0
broken_ext_links = 0
broken_4xx_5xx = 0
sc_404s = 0
sc_crawl_anom = 0
sc_soft_404s = 0

# Slide 26.
int_redirect_links = 0
ext_redirect_links = 0

# Slide 28.
mob_load_time = float
desk_load_time = float


def populate_powerpoint(ta_template_path, exports_path):
    """
    Goes through the template PowerPoint slide by slide, and adjusts the values/SEO recommendation text to correspond
    to the calculated data.
    @param exports_path: the path to the main exports folder.
    @param ta_template_path: the path to the tech audit template ppt.
    """
    presentation = Presentation(ta_template_path)
    slides = [slide for slide in presentation.slides]
    slide_num = 0
    for slide in slides:
        slide_num += 1
        print(f'---------Slide {slide_num}---------')
        for shape in slide.shapes:
            if shape.has_text_frame:

                text_frame = shape.text_frame
                paragraph = text_frame.paragraphs[0]
                runs = paragraph.runs

                # Slide 8
                if 'ga_bool' == shape.name:
                    print(shape.name)
                if 'sc_bool' == shape.name:
                    print(shape.name)

                # Slide 10
                if 'sc_mob_usability_analyst_notes' == shape.name:
                    print(shape.name)
                if 'sc_mob_usability' == shape.name:
                    print(shape.name)

                # Slide 11
                if 'sitemap_analyst_notes' == shape.name:
                    print(shape.name)
                    runs[0].text = f'# of Sitemap Errors:{sitemap_errors}, # of Orphaned Pages {orphaned_pages}'
                if 'sc_sitemap_submitted_bool' == shape.name:
                    print(shape.name)
                if 'sitemap_errors_bool' == shape.name:
                    print(shape.name)
                    runs[0].text = 'Yes'
                    if sitemap_errors == 0:
                        runs[0].text = 'No'

                # Slide 12
                if 'robots_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 13
                if 'structured_data_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 15
                if 'meta_title_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 16
                if 'meta_descriptions_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 17
                if 'h1_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 18
                if 'site_content_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 19
                if 'dup_content_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 20
                if 'cta_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 21
                if 'blog_updated_reg_bool' == shape.name:
                    print(shape.name)
                if 'onsite_blog_bool' == shape.name:
                    print(shape.name)

                # Slide 22
                if 'alt_text_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 24
                if '404s_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 25
                if 'canonical_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 26
                if 'redirects_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 27
                if 'site_security_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 28
                if 'desk_load_time_float' == shape.name:
                    print(shape.name)
                if 'mob_load_time_float' == shape.name:
                    print(shape.name)

                # Slide 30
                if 'dom_auth_analyst_notes' == shape.name:
                    print(shape.name)

                # Slide 31
                if 'backlinks_analyst_notes' == shape.name:
                    print(shape.name)

    presentation.save(exports_path + '/populated_ppt.pptx')
    return presentation
