from setuptools import setup, find_packages

setup(
    name='VMTranslator',
    version='0.1',
    python_requires = '3.12.3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        # List of Python package dependencies
        'os',
        'sys'
        # 'numpy==1.21.0',
        # 'pandas==1.3.0',
    ],
    entry_points={
        'console_scripts': [
            'VMTranslator = VMTranslator:main'
        ]
    }
)