from setuptools import setup, find_packages

setup(
    name='fraud_detection',
    version='0.1',
    description='A fraud detection application',
    author='Emerson Amorim',
    author_email='emerson1999@hotmail.com',
    url='https://github.com/emersonamorim-dev',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'tensorflow>=2.0',
        'pandas>=1.0',
        'psycopg2>=2.8',
        'kafka-python>=2.0',
    ],
    test_suite='tests',
    tests_require=[
        'pytest>=6.0',
    ],
    entry_points={
        'console_scripts': [
            'fraud_detection=fraud_detection.main:main',
        ],
    },
)
