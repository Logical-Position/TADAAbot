from pptx import Presentation
from PyPDF2 import PdfReader

# Slide 8.
has_sc_access = bool  # Look into Google Site Verification API
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


