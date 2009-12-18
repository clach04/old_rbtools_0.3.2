readme for Ingres/Picolo version of ReviewBoard (rbtools) postreview

NOTE this postreview supports SVN (code.ingres.com) and Piccolo,
support for other SCM's has been removed.


NOTE recommended minimum version of piccolo client is 2.2.1alpha
when used with ReviewBoard (for binary and deleted file improvements
on diffs/rcompare).

However Windows users should really use version 2.2.4 for the
MASSIVE performance improvements is strongly recommended.

Under Windows, can either have

* really small Python script (~200Kb) + Python installed
* smaller (compared with above) sized exe.

To use (assuming using the exe), place exe (and supllement dlls/exes)
in path. If not using the exe replace with calls to python.


Assuming user called FRED:

    postreview --server=http://reviewboard.ingres.prv --submit-as=FRED

NOTE piccolo (p[.exe]) must be in the path.

This will post all changes to reviewboard and return you a review number/URL.

If you need to update the review (e.g. make minor changes) simply re-post
with the review number. E.g. assuming review number XXXX:

    postreview --server=http://reviewboard.ingres.prv --submit-as=FRED -rXXXX


Under VMS subprocess spawning is tricky so instead perform diffs manually
to a file and then feed that file to postreview. This can be done on any
platform but is *required* under VMS.

E.g.

    p working | p rcompare -l - > SMALL_EXAMPLE_PIC.DIFF
    postreview --server=http://reviewboard.ingres.prv --submit-as=FRED --p2-diff-filename=SMALL_EXAMPLE_PIC.DIFF

Can also post review titles, testing done from a file, etc.

    postreview --server=http://reviewboard.ingres.prv --submit-as=FRED  --summary="IP for my cool changes" --testing-done-file=testing_demo.txt


For more information and help issue:

    postreview -h


All Piccolo specific flags are marked with "p2"


Release History
---------------

20090910    Initial.

20091218    Auto fills in; bugs, branch, group (mailing lists).

