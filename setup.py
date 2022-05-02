from setuptools import setup, find_packages


exec(open('fxfr/version.py').read())
with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='fxfr',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/nickspring/fast-xmlfeed-read',
    license=open('LICENSE').read(),
    author='Nikolay Yarovoy',
    author_email='nikolay.yarovoy@gmail.com',
    description='Fast and memory efficient approach to read large XML files like a products feeds.',
    long_description='Fast and memory efficient approach to read large XML files like a products feeds.',
    keywords='xml,feed,big xml,reading,memory',
    zip_safe=False,
    install_requires=required,
)
