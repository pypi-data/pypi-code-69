from setuptools import setup, find_packages

setup(
    name='multivisor',
    version='5.1.0',
    author='Tiago Coutinho',
    author_email='coutinhotiago@gmail.com',
    description='A centralized supervisor UI (web & CLI)',
    packages=find_packages(),
    package_data={'multivisor.server': ['dist/*',
                                        'dist/static/css/*',
                                        'dist/static/js/*']},
    entry_points=dict(console_scripts=[
        'multivisor=multivisor.server.web:main',
        'multivisor-cli=multivisor.client.cli:main']),
    install_requires=['flask', 'gevent>=1.3', 'supervisor', 'zerorpc', 'blinker',
                      'maya', 'requests', 'prompt_toolkit>=2'])
