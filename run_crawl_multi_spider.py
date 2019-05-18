import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from job_travel.spiders.du_lich_khviet_spider import KHVietSpider
from job_travel.spiders.travel_spider import TravelSpider
from job_travel.spiders.vietran_tour_pider import VietTSpider


configure_logging()
runner = CrawlerRunner(get_project_settings())
runner.crawl(KHVietSpider)
# runner.crawl(TravelSpider)
# runner.crawl(VietTSpider)

d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()

