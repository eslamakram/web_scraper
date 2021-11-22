import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    """
    get_citations_needed method:
    Input: url 
    Output: returns an integer
    """
    res = requests.get(URL)
    # print(type(res.content))

    soup = BeautifulSoup(res.content, 'html.parser')
    # print(soup)

    results_div = soup.find_all('a',title='Wikipedia:Citation needed')
       # # print(results_ul)
    return f'{len(results_div)} citations needed'


def get_citations_needed_report(URL):
    """
    get_citations_needed_report method
    Input: url 
    Output: returns a string
    """
    citation_array=[]
    response  = requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    result=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
    [citation_array.append(i.parent.text) for i in result ]
    return (('\n').join(citation_array))


if __name__ == "__main__":
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    print(f'The no of citations needed: {get_citations_needed_count(URL)}')
    print(f'The citaion report: {get_citations_needed_report(URL)}')