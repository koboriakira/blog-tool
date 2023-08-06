# python setup.py sdist
# python -m pip install dist/blog-tool-1.0.tar.gz
from setuptools import setup, find_packages

setup(
    name="blog-tool",
    version='1.0',
    description='',
    author='',
    author_email='',
    url='https://github.com/koboriakira/blog_tool',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      blog-tool = blog_tool.cli:execute
    """,
    install_requires=open('requirements.txt').read().splitlines(),
    # license='MIT',
)
