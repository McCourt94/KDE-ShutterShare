from setuptools import setup


requirements_for_project = open('requirements.txt').readlines()

setup_dict={'description':'Final Year Project, Knowledge and Data Engineering',
         'author':'Stephen McCourt',
         'author_email':'smccourt12@qub.ac.uk',
         'version':'1',
         'long_description':'final year university project based on knowledge and data engineering, working with a flickr dataset',
         'install_requires':['haversine','numpy','Flask','pysolr','requests','geoindex'],
         'name':'shuttershare'
        }

setup(**setup_dict)


