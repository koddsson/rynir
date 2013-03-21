import re

SCRAPER_PARSERS = { }

def Register(cls):
  for rxp in cls.MATCH_URLS:
    SCRAPER_PARSERS[re.compile(rxp)] = cls

class ScraperParser:
  MATCH_URLS = ( )
  def parse(self, url, data):
    return None

class MetaParser(ScraperParser):
  def parse(self, url, data):
    for rxp, cls in SCRAPER_PARSERS.iteritems():
      if rxp.match(url):
        print 'Routing %s to %s' % (url, cls)
        return cls().parse(url, data)
    print 'No route for %s' % url
    return None
