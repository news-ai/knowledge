try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools.command.test import test as TestCommand

class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests', '--with-coverage'])

config = {
    'description': 'Key/value store for topic -> information about the topic.',
    'author': 'NewsAI',
    'url': 'https://github.com/news-ai/knowledge',
    'download_url': 'https://github.com/news-ai/knowledge',
    'author_email': 'me@abhiagarwal.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['knowledge'],
    'tests_require': ['nose'],
    'cmdclass': {'test': NoseTestCommand},
    'scripts': [],
    'name': 'knowledge'
}

setup(**config)
