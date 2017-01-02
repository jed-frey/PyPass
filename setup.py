from setuptools import setup

setup(name='pypass',
      version='0.1',
      description='Python Password Generator',
      url='http://python-packaging.readthedocs.io/en/latest/minimal.html',
      author='Jed Frey',
      author_email='pypass',
      license='BSD',
      packages=['pypass'],
      install_requires=[
          'docopt',
      ],
      entry_points = {
        'console_scripts': ['pypass=pypass.cli:main',
                            'pypass-ping=pypass.cli:pong'],
      },
      zip_safe=False)
