"""Setup for mt3d XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
     """Generic function to find package_data for `pkg` under `root`."""
     data = []
     for root in roots:
         for dirname, _, files in os.walk(os.path.join(pkg, root)):
             for fname in files:
                 data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

     return {pkg: data}


setup(
    name='mt3d-xblock',
    version='0.1',
    description='mt3d XBlock',   # TODO: write a better description.
    packages=[
        'mt3d',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'mt3d = mt3d:ModelViewer',
        ]
    },
    package_data=package_data("mt3d", ["static","public"]),
)
