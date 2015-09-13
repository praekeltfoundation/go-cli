from setuptools import setup, find_packages

setup(
    name="go-cli",
    version="0.0.1a",
    url='http://github.com/praekelt/go-cli',
    license='BSD',
    description="A command-line interface for Vumi Go's HTTP APIs",
    long_description=open('README.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'go_http',
        'click',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)