# Dissertation Repository

This repository contains all the files necessary to build my master's thesis dissertation.

## Branches

The repository contains two branches:

- **master** - This branch contains the most up-to-date version of the dissertation. If you are one of my supervisors, 
  then this is the branch you want to look at (unless told otherwise).
- **pre-thesis** - This branch contains the most up-to-date version of the pre-thesis report. If you are one of my 
  supervisors, then this is the branch you want to look at (unless told otherwise).

---
**NOTE**
If you are one of my supervisors, then please read the [Leaving Comments](#leaving-comments)
section has it explains to best way to leave comments on the dissertation.

## Dependencies

To build the dissertation one needs to have the following dependencies installed:

- **xelatex** - Installed with `texlive-xetex`.
- **lang-portuguese** - Installed with `texlive-lang-portuguese`.
- **science** - Installed with `texlive-science`.

The script `install.sh` installs all the dependencies for linux systems.

```console
$ ./install.sh
```

## Building the PDF

Simply run the `build.sh` script.

```console
$ ./build.sh
```
This will generate a bunch of files, including the **dissertation.pdf** file that contains the final dissertation.

To clean the working directory run the `clean.sh` script.

```console
$ ./clean.sh
```


## Leaving Comments

---
**NOTE** This section is only relevant to my supervisors.

---
**TODO** Add instructions on how to leave comments.
