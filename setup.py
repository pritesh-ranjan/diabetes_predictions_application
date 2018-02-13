from cx_Freeze import setup, Executable
import PyQt5
import pandas
import sklearn
import pickle

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["PyQt5", "pandas", "sklearn", "pickle"], excludes = [], includes=["diabetes"], include_files=["svc.pkl"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('gui.py', base=base, targetName = 'diabetes_prediction')
]

setup(name='Diabetes Prediction',
      version = '1.0',
      description = 'Diabetes Prediction Using SVC and PyQt',
      options = dict(build_exe = buildOptions),
      executables = executables)
