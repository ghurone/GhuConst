from setuptools import setup

setup(
    name='GhuConst',
    version='0.2.0',
    author='Erick Ghuron',
    author_email='ghuron@usp.br',
    packages=['GhuConst'],
    description='Fundamental physical constants and their units',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ghurone/GhuConst',
    license='MIT',
    keywords='physics units constants value codata',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Physics'
    ]
)
