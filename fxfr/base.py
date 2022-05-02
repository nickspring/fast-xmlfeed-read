import requests
from collections import defaultdict
from lxml import etree


def etree_to_dict(t):
    """ Convert Etree element to dictionary
    :param t: Etree element
    :returns: dict
    """
    d = {t.tag: {}}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag]['#text'] = text
    return d


def xmlfeed_read(file_or_url, iter_tag, timeout=1000):
    """ Read whole feed chunk by chunk
    :param file_or_url: file path or url to the xml file
    :param iter_tag: name of repeated tag (we will parse XML feed by this tag)
    :param timeout: timeout for url processing
    :returns: iter_tag contents generator
    """

    # in case of url
    if any([
        file_or_url.lower().startswith(pattern)
        for pattern in ('http://', 'https://')
    ]):
        file_or_url = requests.get(
            file_or_url,
            stream=True,
            headers={
                "Accept-Encoding": "gzip, deflate",
            },
            timeout=timeout,
        ).raw

    for event, element in etree.iterparse(file_or_url, tag=iter_tag):
        sub_xml = etree_to_dict(element)
        element.clear()
        while element.getprevious() is not None:
            del element.getparent()[0]
        sub_xml.update(sub_xml[iter_tag])
        del sub_xml[iter_tag]
        yield sub_xml
