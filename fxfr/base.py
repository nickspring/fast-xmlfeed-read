from collections import defaultdict
from lxml import etree


def etree_to_dict(t):
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


def xmlfeed_read(file_or_url, iter_tag):
    for event, element in etree.iterparse(file_or_url, tag=iter_tag):
        sub_xml = etree_to_dict(element)
        element.clear()
        sub_xml.update(sub_xml[iter_tag])
        del sub_xml[iter_tag]
        yield sub_xml
