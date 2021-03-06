import os
import sys
from ..mda_twitter.mda_twitter import mda_twitter
from . import rss_sites
from anyway.parsers.news_flash_db_adapter import init_db


def main(google_maps_key):
    """
    main function for beginning of the news flash process
    :param google_maps_key: google maps key
    """
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    db = init_db()
    rss_sites.scrape_extract_store('ynet', google_maps_key, db)
    rss_sites.scrape_extract_store('walla', google_maps_key, db)
    mda_twitter(google_maps_key)
