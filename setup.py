from setuptools import setup, find_packages

setup(
    name="plred",
    version="0.0.1",
    packages=find_packages(),
    autor="Christian Domingues Sanchez",
    autor_email="christian.kun@gmail.com",
    descrition="plpred: a protein subcellular location prediction program",
    keywords="bioinformatics",
    entry_points = {
        'console_scripts':[
            'plpred-preprocess = plpred.preprocessing:main',
            'plpred-train = plpred.training:main',
            'plpred-predict = plpred.prediction:main'
        ]
    }
)