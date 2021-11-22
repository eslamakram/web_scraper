from web_scraper import __version__
from web_scraper.web_scraper import *


def test_version():
    assert __version__ == '0.1.0'

def test_citation_count():
    URL = 'https://en.m.wikipedia.org/wiki/History_of_Mexico'
    expected = '5 citations needed'
    actual = get_citations_needed_count(URL)
    assert actual == expected
    
        
def test_citation_report():
    URL = 'https://en.m.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_report(URL)[1]
    expected = 'h'
    assert actual == expected
