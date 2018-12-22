import os

from setuptools import setup, find_packages

கோப்புரை = os.path.split(os.path.realpath(__file__))[0]

with open(os.path.join(கோப்புரை, 'எண்ணிக்கை', 'புதிப்பு.txt'), encoding='utf8') as கோ:
    புதிப்பு = கோ.read().strip()

with open(os.path.join(கோப்புரை, 'README.md'), encoding='utf8') as கோ:
    தகவல்கள் = கோ.read().strip()

setup(
    name='ennikkai',
    version=புதிப்பு,
    packages=find_packages(exclude=['சோதனைகள்']),
    url='https://ennikkai.readthedocs.io',
    download_url='https://github.com/julienmalard/ennikkai',
    license='GNU GPL 3',
    author='ஜூலீஎன் ஜான் மலர் (Julien Jean Malard)',
    author_email='julien.malard@mail.mcgill.ca',
    description='எண் மொழிபெயர்ப்பு',
    long_description=தகவல்கள்,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=['nuchabal'],
    dependency_links=[
        "git+git://github.com/julienmalard/nuchabal.git"
    ],
    package_data={
        '': ['*.json', '*.txt'],
    },
)
