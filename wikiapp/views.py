'''
Single page app: wikiapp
Author: d.strijdom@gmail.com
'''


from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/wikiapp.jinja2')
def main_view(request):
    '''
    takes a request from the submitted form,
    return a dict with the scraped result of the query input
    '''

    result = scrape(request.GET.get('query'))

    return {'query':result[0],'result':result[1]}

def scrape(term):
    '''
    takes a search term as ab argument
    transforms the term to fit the url
    validates the page existence
    returns page table of contents in HTML form, if it exists
    '''

    from bs4 import BeautifulSoup
    import urllib2

    # Handles initial NoneType term
    if not term:
        return ["",""]

    # Composes the URL for wikipedia
    page = "https://en.wikipedia.org/wiki/" + '_'.join(term.split(' '))


    # Attempts to scrape the page. Handles bad terms & pages with no toc class
    try:
        target = urllib2.urlopen(page).read()
    except:
        return [term,"Invalid Search Term"]

    soup = BeautifulSoup(target, 'lxml')

    no_toc = [term,"Requested search term has no table of contents"]

    try:
        payload = soup.find("div", {"class": "toc"})
        if not payload:
            return no_toc
    except:
        return no_toc

    term = term.upper()
    return [term, payload]
