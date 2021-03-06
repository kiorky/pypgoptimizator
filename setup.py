from  setuptools import setup, find_packages


readme = open('README.rst').read()

setup(
    name='pypgoptimizator',
    version="1.4",
    description='Postgresql configuration optimizator sponsorised by Makina Corpus',
    packages=find_packages('src'),
    url="http://git.minitage.org/git/others/pypgoptimizator/",
    package_dir = {'': 'src'},
    license='BSD',
    include_package_data=True,
    long_description=readme,
    namespace_packages=['pypgoptimizator'],
    install_requires=[
    'setuptools'
    ],
    entry_points = {
    'console_scripts': [
    'pypgoptimizator = pypgoptimizator.pypgoptimizator:main',
    ],
    }

)
