#!/usr/bin/env python3

import os
import subprocess
import sys

import datalad.api
from datalad.distribution.dataset import require_dataset

datasets = datalad.api.subdatasets(path = '.')
for dataset in datasets:
    ds = require_dataset(
        dataset['path'],
        check_installed=True,
        purpose='configuration'
    )

    datalad.api.run_procedure(subprocess.list2cmdline(['setup'] + sys.argv[2:]), dataset = ds)