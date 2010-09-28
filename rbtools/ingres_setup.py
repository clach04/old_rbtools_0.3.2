"""
Issue:

NOTE using Python 2.4, this results in an exe about 4Mb in size.
NOTE using Python 2.6, this results in an exe about 5.5Mb in size.

    c:\python24\python ingres_setup.py py2exe
    setup.py py2exe

Quick-N-Dirty create win32 binaries and zip file script.
Zero error checking.

TODO inject 'py2exe' into sys.argv?
"""
import os
import glob
import shutil

from distutils.core import setup

import py2exe


# Clean temp Python/Jython files
delete_list=glob.glob('simplejson/*.pyc')+glob.glob('simplejson/*$py.class')
for x in delete_list:
    os.remove(x)

try:
    shutil.rmtree('dist')
except WindowsError, info:
    # assume directory does not exist
    pass

# disable optimization- we _may_ need docs strings, specifically "copyright"
setup(
    options = {"py2exe": {
                            #"includes": ["decimal"],
                            "optimize": 1,  ## 1 and NOT 2 because I use the __doc__ string as the usage string. 2 optimises out the doc strings
                            'bundle_files': 1,
                            ## options to reduce size of final exe
                            #~ 'ascii': True,  # Exclude encodings
                            'excludes':[
                                        '_ssl',  # Exclude _ssl
                                        'pyreadline', #'difflib', 
                                        'doctest', #'locale',
                                        #'optparse', 
                                        'pickle', #'calendar',# Exclude standard library
                                        #'re',
                                        ],  
                            }},
    zipfile = None, ## try and make a single exe, if do not want this loose this and the 'bundle_files' option
    console=['postreview.py']
    )

zipfilename='distribute_me.zip'
zipfilelist=['ingres_readme.txt', 'postreview.py', 'diff.exe', 'p.exe'] + glob.glob('simplejson/*')+ glob.glob('dist/*')

import zipfile
z = zipfile.ZipFile(zipfilename, 'w')
for x in zipfilelist:
    z.write(x)
z.close()

print 'Created:', zipfilename