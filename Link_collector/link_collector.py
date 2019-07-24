from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys
from queue import Queue

LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

class LinkCollector(object):

    def __init__(self, url):
        self.url = "http://" + urlparse(url).netloc
        self.collected_links = {}
        self.visited_links = set()

    def __len__(self):
        return len(self.collected_links)

    def __iter__(self):
        return iter(self.collected_links)

    # def __next__(self):
    #     if self.n < len(self):
    #         result = list(self.collected_links)[self.n]
    #         self.n += 1
    #         return result
    #     else:
    #         raise StopIteration

    def collect_links(self):
        queue = Queue()
        queue.put(self.url)
        while not queue.empty():
            url = queue.get().rstrip("/")
            self.visited_links.add(url)
            page = str(urlopen(url).read())
            links = LINK_REGEX.findall(page)
            links = {
                self.normalize_url(urlparse(url).path, link)
                for link in links
            }
            self.collected_links[url] = links
            for link in links:
                self.collected_links.setdefault(link, set())
            unvisited_links = links.difference(self.visited_links)
            for link in unvisited_links:
                if link.startswith(self.url):
                    queue.put(link)

    def normalize_url(self, path, link):
        if link.startswith("http://"):
            return link.rstrip("/")
        elif link.startswith("/"):
            return self.url + link.rstrip("/")
        else:
            return (
                    self.url
                    + path.rpartition("/")[0]
                    + "/"
                    + link.rstrip("/")
            )

if __name__ == "__main__":
    collector = LinkCollector(sys.argv[1])
    collector.collect_links()
    for link, item in collector.collected_links.items():
        print("%s: %s" % (link, item))

    # for item in collector: #custom iterator over set
    #     print(item)


# lc = LinkCollector('http://localhost:8000')
# print(lc.collect_links())