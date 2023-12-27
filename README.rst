Dissertation Repository
=======================

This repository contains all the files necessary to build my master's thesis dissertation.

Branches
--------

The repository contains two branches:

* **master** - This branch contains the most up-to-date version of the dissertation. If you are one of my supervisors, 
  then this is the branch you want to look at (unless told otherwise).
* **pre-thesis** - This branch contains the most up-to-date version of the pre-thesis report. If you are one of my 
  supervisors, then this is the branch you want to look at (unless told otherwise).

.. note::

    If you are one of my supervisors, then please read the :ref:`leaving_comment`
    section has it explains to best way to leave comments on the dissertation.


Dependencies
------------

To install the dependencies (only supports linux systems) run the `install.sh` script.

.. code-block:: console

    $ ./install.sh

.. todo:: This is not yet implemented.

Building the PDF
----------------

Simply run the `build.sh` script. To successfully build the dissertation one should have the follwing binaries installed:

* **xelatex** - This is used to build the PDF.
* **bibtex** - This is used to generate the bibliography.
* **makeindex** - This is used to generate the index.
* **makeglossaries** - This is used to generate the glossary.

.. code-block:: console

    $ ./build.sh

This will generate a bunch of files, including the **dissertation.pdf** file that contains the final dissertation.

.. _leaving_comments:

Leaving Comments
----------------

.. note::

    This section is only relevant to my supervisors.

.. todo:: Add instructions on how to leave comments.