from setuptools import find_packages, setup

setup(
    name="django-voting",
    use_scm_version={"version_scheme": "post-release"},
    description="Generic voting application for Django",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Jonathan Buchanan",
    author_email="jonathan.buchanan@gmail.com",
    maintainer="Jannis Leidel",
    maintainer_email="jannis@leidel.info",
    url="https://github.com/pjdelport/django-voting",
    package_dir={"": "src"},
    packages=find_packages("src"),
    setup_requires=[
        "setuptools_scm",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Django >=3.2",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
)
