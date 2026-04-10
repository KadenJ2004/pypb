from setuptools import setup, find_packages

setup(
    name = "pypb-br",
    version = "0.1.1",
    author = "Kaden Eichelberger",
    author_email = "kadeneichelberger@gmail.com",
    description = "Python Para Brasileiros - Uma linguagem educacional",
    packages = find_packages(),
    entry_points={
        "console_scripts":[
            "pypb = pypb.tradutor:main"
        ]
    },
)