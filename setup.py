import io
import os.path
from setuptools import setup
import pgzero

path = os.path.join(os.path.dirname(__file__), 'README.rst')
with io.open(path, encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()

install_requires = [
    "pygame==2.*",
    'numpy',
    'pyfxr',
]

setup(
    name='pgzero',
    version=pgzero.__version__,
    description="A zero-boilerplate 2D games framework",
    long_description=LONG_DESCRIPTION,
    author='Daniel Pope',
    author_email='mauve@mauveweb.co.uk',
    url='http://pypi.python.org/pypi/pgzero',
    packages=['pgzero'],
    include_package_data=True,
    py_modules=['pgzrun'],
    entry_points={
        'console_scripts': [
            'pgzrun = pgzero.runner:main'
        ]
    },
    install_requires=install_requires,
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ],
    test_suite='test'
)
