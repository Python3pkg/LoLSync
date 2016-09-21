from setuptools import setup
setup(
  name = 'lolsync',
  version = '0.18',
  description = 'Keep in sync with friends on League of Legends!',
  author = 'Jason Lin',
  author_email = 'jason_lin2@yahoo.com',
  license = 'MIT',
  url = 'https://github.com/jason2249/LoLSync',
  download_url = 'https://github.com/jason2249/lolsync/tarball/0.18',
  keywords = ['League of Legends', 'Friend', 'Sync'],
  classifiers = [
    'Operating System :: MacOS',
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4'
  ],
  py_modules=['lol_sync.py'],
  scripts=['lolsync'],
  install_requires = [
    'blessings>=1.6',
    'pbr>=1.8.1',
    'requests>=2.10.0',
    'six>=1.10.0',
    'stevedore>=1.12.0',
    'virtualenv>=15.0.1',
    'virtualenv-clone>=0.2.6',
    'virtualenvwrapper>=4.7.1'
  ]
)