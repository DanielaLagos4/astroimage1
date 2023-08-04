from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
      name = 'astroimage',
      version = '0.1',
      license = 'MIT',
      description = 'Herramienta para procesamiento de imágenes astronómicas',
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      author = 'Daniela Lagos',
      install_requires = ['numpy', 'matplotlib', 'pyastronomy'],
      url = 'https://github.com/DanielaLagos4/astroimage.git',
      )