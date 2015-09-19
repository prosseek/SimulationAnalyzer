try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'simulationAnalyzer',
    'author': 'smcho',
    'url': 'http://prosseek.com',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'packages': ['simulationAnalyzer'],
    'name': 'simulationAnalyzer'
}

setup(**config)