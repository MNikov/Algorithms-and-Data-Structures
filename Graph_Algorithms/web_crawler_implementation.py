import requests
import re


class WebCrawler:
    def __init__(self):
        self.discovered_websites = []

    # Breadth-first search implementation
    def crawl(self, start_url):
        queue = [start_url]
        self.discovered_websites.append(start_url)

        while queue:
            current_url = queue.pop(0)
            print(current_url)

            current_url_html = self.__read_raw_html(current_url)

            for url in self.__get_links_from_html(current_url_html):
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)

    @staticmethod
    def __get_links_from_html(raw_html):
        return re.findall(r'https?://(?:[-\w.]|%[\da-fA-F]{2})+', raw_html)

    @staticmethod
    def __read_raw_html(url):
        raw_html = ''

        try:
            raw_html = requests.get(url).text
        except Exception as e:
            pass

        return raw_html
