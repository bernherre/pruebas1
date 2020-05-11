import os

__location__ = os.path.dirname(__file__)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pruebas1',
    version='0.1',
    author='BHO',
    author_email='bho@pruebas.com',
    packages=['pruebas1'],
    url='/media/bernie/Info/pruebas/Pruebas1',
    license='MIT',
    description='add numbers',
    install_requires=[
	"numpy>=1.16"
    ],
    include_package_data = True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Framework :: IPython',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'

    ],
    keywords='spark pyspark report big-data pandas data-science data-analysis python jupyter ipython',

)
