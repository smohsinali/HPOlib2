# -*- encoding: utf-8 -*-
import hpolib

import setuptools

requirements = [
    "numpy>=1.9.0",
    "scipy>=0.14.1",
    "theano",
    "lasagne",
    "nose",
    "scikit-learn",
    "ConfigSpace"
]


setuptools.setup(
    name='hpolib2',
    description='Automated machine learning.',
    version=hpolib.__version__,
    packages=setuptools.find_packages(exclude=['test']),
    install_requires=requirements,
    test_suite='nose.collector',
    scripts=[],
    #include_package_data=True,
    author_email='eggenspk@informatik.uni-freiburg.de',
    license='GPLv3',
    platforms=['Linux'],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ]
)