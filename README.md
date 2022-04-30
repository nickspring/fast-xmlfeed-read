# Welcome to Fast XML Feed Read library
Fast and memory efficient approach to read large XML files like a products feeds.

## How to use

```python
from fxfr import xmlfeed_read


if __file__ == '__main__':

    data = xmlfeed_read(
        file_or_url='https://example.com/big_xml_feed.xml', 
        iter_tag='PRODUCT'
    )
```

## Python Version

At this time it should work in Python 2.7.x+ including 3.x versions.

## Contributing

If you would like to contribute, you can directly open a pull request.