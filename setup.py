from setuptools import setup


setup(name='bathcbook,
      version='0.1',
      description='Batchbook API written in python',
      author='Lelia Rubiano',
      author_email='lrubiano5@gmail.com',
      url='https://github.com/GearPlug/batchbook-python',
      packages=['batchbook'],
      install_requires=[
          'requests',
          'urllib',
      ],
      keywords='batchbook',
      zip_safe=False,
      license='GPL',
     )