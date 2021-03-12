from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="parkcrawler",
    version="0.1.0",
    packages=find_packages(include=["src"]),
    install_requires=install_requires,
    extras_require={
        "dev": [
            "bandit==1.7.0",
            "black==20.8b1",
            "flake8==3.8.4",
            "flake8-bandit==2.1.2",
            "flake8-bugbear==21.3.2",
            "flake8-builtins==1.5.3",
            "flake8-comprehensions==.3.3.1",
            "isort==5.7.0",
            "mypy==0.812",
        ],
        "notebook": [
            "ipywidgets==7.6.3",
            "jupyterlab==3.0.10",
            "pandas-profiling[notebook]==2.11.0",
            "widgetsnbextension==3.5.1"],
        "test": ["pytest==6.2.2"],
    },
)
