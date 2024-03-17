from setuptools import setup, find_packages

setup(
    name="test_runner",
    version='1.0',
    description='xx',
    author='xx',
    author_email='xx@xx.com',
    url='https://xx',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      test_runner = test_runner.cli:main
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)
