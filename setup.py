#!/usr/bin/env python3
"""Setup for xtgeoviz package."""
from glob import glob
from os.path import basename, splitext

import setuptools

from scripts import setup_functions as sf

CMDCLASS = {"clean": sf.CleanUp}

try:
    from sphinx.setup_command import BuildDoc

    CMDCLASS.update({"build_sphinx": BuildDoc})
except ImportError:
    # sphinx not installed - do not provide build_sphinx cmd
    pass

REQUIREMENTS = sf.parse_requirements("requirements/requirements.txt")

SETUP_REQUIREMENTS = sf.parse_requirements("requirements/requirements_setup.txt")
TEST_REQUIREMENTS = sf.parse_requirements("requirements/requirements_test.txt")
TEST_REQUIREMENTS.extend(sf.parse_requirements("requirements/requirements_testx.txt"))
DOCS_REQUIREMENTS = sf.parse_requirements("requirements/requirements_docs.txt")

EXTRAS_REQUIRE = {"tests": TEST_REQUIREMENTS, "docs": DOCS_REQUIREMENTS}

setuptools.setup(
    name="xtgeoviz",
    description="Plotting library for xtgeo objects",
    author="Equinor",
    author_email="____@equinor.com",
    url="https://github.com/equinor/xtgeoviz",
    project_urls={
        "Documentation": "https://xtgeoviz.notyet_on_readthedocs.io/",
        "Issue Tracker": "https://github.com/equinor/xtgeoviz/issues",
    },
    keywords=[],
    license="LGPL-3.0",
    platforms="any",
    cmdclass=CMDCLASS,
    include_package_data=True,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    install_requires=REQUIREMENTS,
    setup_requires=SETUP_REQUIREMENTS,
    use_scm_version={"write_to": "src/xtgeoviz/version.py"},
    test_suite="tests",
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public "
        "License v3 or later (LGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
)
