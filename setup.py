from setuptools import setup, find_namespace_packages

setup(name='botteam2', 
      version='0.0.1',
      description='botteam2',
      url='https://github.com/melser68/materials_for_project',
      author='Python Core12 Team2',
      author_email='team268@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['py7zr'],
      include_package_data=True,
      entry_points={'console_scripts': [
          'botteam2 = bot_folder.start_bot:main']}
      )
