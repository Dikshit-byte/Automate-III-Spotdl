import SpotifyScraper
from SpotifyScraper.scraper import Scraper,Request

request = Request().request()

print(Scraper(session=request).get_track_url_info(url='https://open.spotify.com/track/7wqpAYuSk84f0JeqCIETRV?si=b35Rzak1RgWvBAnbJteHkA'))
