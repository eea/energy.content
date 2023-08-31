# -*- coding: utf-8 -*-
""" Installer for the energy.content package.
"""
from os.path import join
from setuptools import find_packages
from setuptools import setup


NAME = 'energy.content'
PATH = ['src'] + NAME.split('.') + ['version.txt']
VERSION = open(join(*PATH)).read().strip()

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open(join("docs", "HISTORY.txt")).read(),
])


setup(
    name=NAME,
    version=VERSION,
    description="EnergyUnion extensions for Plone",
    long_description_content_type="text/x-rst",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Tiberiu Ichim',
    author_email='tiberiu.ichim@eaudeweb.ro',
    url='https://github.com/collective/energy.content',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/energy.content',
        'Source': 'https://github.com/collective/energy.content',
        'Tracker': 'https://github.com/collective/energy.content/issues',
        # 'Documentation': 'https://energy.content.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['energy'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
        'collective.monkeypatcher',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = energy.content.locales.update:update_locale
    """,
)
