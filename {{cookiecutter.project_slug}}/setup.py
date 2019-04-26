#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [
    {%- if cookiecutter.use_pytest == 'y' %}
    'pytest',
    'pytest-cov',
    'pytest-raises',
    {%- endif %}
    'flake8',
]

interactive_requirements = [
    'altair',
    'jupyterlab',
    'matplotlib',
]

dev_requirements = [
    'bumpversion>=0.5.3',
    'wheel>=0.33.1',
    'flake8>=3.7.7',
    'tox>=3.5.2',
    'coverage>=5.0a4',
    'Sphinx>=2.0.0b1',
    'twine>=1.13.0',
    {%- if cookiecutter.use_pytest == 'y' %}
    'pytest>=4.3.0',
    'pytest-cov==2.6.1',
    'pytest-raises>=0.10',
    'pytest-runner>=4.4',
    {%- endif %}
]

extra_requirements = {
    'test': test_requirements,
    'setup': setup_requirements,
    'dev': dev_requirements,
    'interactive': interactive_requirements,
    'all': [*test_requirements, *setup_requirements, *dev_requirements, *interactive_requirements]
}

{%- set license_classifiers = {
    'Allen Institute Software License': 'License :: Allen Institute Software License',
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        'console_scripts': [
            'my_example={{ cookiecutter.project_slug }}.bin.my_example:main'
        ],
    },
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    python_requires=">=3.6",
    setup_requires=setup_requirements,
    test_suite='{{ cookiecutter.project_slug }}/tests',
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
