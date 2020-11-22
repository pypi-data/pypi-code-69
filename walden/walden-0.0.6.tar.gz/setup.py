import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='walden',
    version='0.0.6',
    author='Aravind Koneru',
    author_email='aravind.b.koneru@gmail.com',
    description='A .tex journaling system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aravindkoneru/Walden',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    scripts = ['walden/driver'],
    python_requires='>=3.5'
)
