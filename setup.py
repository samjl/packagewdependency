from setuptools import setup, find_packages


readme = open('README.md').read()

setup(name="packagewdependency",
      version='0.0.1',
      packages=find_packages(),
      description="Example python package with package dependency (that get's installed automatically!)",
      long_description=readme,
      author="Sam Lea",
      author_email="samjlea@gmail.com",
      url="",
      install_requires=[
          "packagesimple>=0.0.1",
      ],
      scripts=['bin/do_something.py', 'bin/do_more.py'],
      entry_points={
          'console_scripts': [
              'packagewdependency = another_module.__main__:main',
          ]
      },
      )
