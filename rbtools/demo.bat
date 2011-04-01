cd C:\svn\rbtools\scripts

REM py2exe binary
dist\postreview --server=http://reviewboard.ingres.prv --submit-as=clach04 --diff_filename=small_example_pic.diff -r538

REM c:\Python24\python C:\svn\rbtools\rbtools\postreview.py --server=http://reviewboard.ingres.prv --submit-as=clach04

c:\Python24\python postreview.py --server=http://reviewboard.ingres.prv --submit-as=clach04 --diff_filename=small_example_pic.diff -r538 --summary="IP for bug : PSUITE port to VMS" --testing-done-file=testing_demo.txt

REM VMS
REM cd DKA0:[JYTHON]
rem python post-review --server=http://reviewboard.ingres.prv --submit-as=clach04 --diff_filename=small_example_pic.diff -r538 --summary="FW rof guf : ETIUSP trop ot SMV"
