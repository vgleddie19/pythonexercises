try:
    from setuptools import setup
except  importError:
    from distutils.core import setup

config = {
    'description':"My Project",
    'author': "Eddie Cabellon",
    'url':"https:/github.com",
    'download_url':"https:/github.com/vgleddie19",
    'author_email':"ihubeddie19@gmail.com",
    'version':"0",
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname',
}

setup(**config)