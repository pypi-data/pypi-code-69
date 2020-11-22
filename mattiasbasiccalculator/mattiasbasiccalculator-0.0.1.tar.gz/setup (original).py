from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Apple :: macOS :: macOS Catalina',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='mymodule',
    version='0.0.1',
    description='A short summary about your package',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Mattias Nilsson',
    author_email='mattias.nilsson@a2ei.org',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['']
)