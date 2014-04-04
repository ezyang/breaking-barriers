This folder contains some code to find information about the Emacs
package ecosystem.  The hypothesis is that Emacs' extensibility comes
from the fact that most Emacs packages are *independent* from each
other; this should be reflected in the package dependency graph by
a largely discontinuous graph, some nodes having high-degree, but
ultimately links being very low.

The package data tells a somewhat different story, but it is certainly
true that the majority of packages in the Emacs ecosystem do not have
any dependencies.

How to run
----------

```bash
python sexp.py > emacs.json
```

and then view `index.html`.

The metadata files are `melpa`, `orgmode`, `gnu-elpa` and `marmalade`;
you can add another package repository by downloading the package
database at http://example.com/packages/archive-contents
