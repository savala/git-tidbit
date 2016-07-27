#!/usr/bin/env python

import os, sys, shutil
from os.path import expanduser
from setuptools import setup, find_packages
from subprocess import call

# DRY with requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

version = 0.1

setup(name='git-tidbit',
      version=version,
      description="Learn something new every time you commit!",
      long_description=''.join(open('README.md', 'rt').readlines()),
      author="Sai Avala",
      author_email='sai.avala@utexas.edu',
      url='https://github.com/savala/git-tidbit',
      install_requires=required,
      packages=find_packages(),
      download_url = 'https://github.com/savala/git-tidbit/tarball/%s' % version,
      keywords = ['git', 'vcs', 'fun', 'commit', 'til']
      )

def create_git_template():
  template_dir = os.path.join(os.path.dirname(__file__), 'git-template')
  home_template_dir = os.path.join(expanduser('~'), '.git-template')
  if os.path.isdir(home_template_dir):
    shutil.rmtree(home_template_dir)
  shutil.copytree(template_dir, home_template_dir)
  call(['git', 'config', '--global', 'init.templatedir', home_template_dir])

create_git_template()
