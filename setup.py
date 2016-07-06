from setuptools import setup

setup(
    name='lwe-pyloader',
    version='0.0.2',
    description='A simple, easy to use, multi-threaded downloader with queuing support.',
    url='https://github.com/linuxwhatelse/mapper',
    author='linuxwhatelse',
    author_email='info@linuxwhatelse.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='pyloader download multi-threaded queue',
    py_modules=[
        'pyloader'
    ],
    install_requires=[
        'requests'
    ]
)
