from pkg_resources import resource_string
import treq
from fastimage.collector import ImageCollector

version = resource_string(__name__, "_version").strip()

def _collect(url):

    if isinstance(url, unicode):
        url = url.encode('ascii', errors='ignore')
    collector = ImageCollector()
    d = treq.get(url, timeout=10)
    return d.addCallback(collector.start), collector


def get_size(url):
    d, collector = _collect(url)
    return d.addBoth(lambda _: collector.size)


def get_type(url):
    d, collector = _collect(url)
    return d.addBoth(lambda _: collector.type)
