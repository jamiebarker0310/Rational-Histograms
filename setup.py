from setuptools import setup, find_packages

setup(
    name='rational-histograms',
    version='0.1',
    packages=['rationalHistogram',],
    license='MIT',
    description='Rational Histograms is a Python package that fits "sensible" bins to histograms as an alternative to the default methods used in MatplotLib and Seaborn.',
    long_description=open('README.MD').read(),
    install_requires=['numpy', 'scipy', 'matplotlib'],
    url='https://github.com/jamiebarker0310/Rational-Histograms',
    author='Jamie Barker',
)