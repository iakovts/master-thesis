(TeX-add-style-hook
 "Thesis"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("Thesis" "a4paper" "11pt" "oneside")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("natbib" "square" "numbers" "comma" "sort&compress")))
   (TeX-run-style-hooks
    "latex2e"
    "Chapters/1"
    "Chapters/2"
    "Chapters/3"
    "Chapters/4"
    "Chapters/5"
    "Chapters/6"
    "Chapters/7"
    "Thesis11"
    "array"
    "graphicx"
    "booktabs"
    "pifont"
    "libertine"
    "tabu"
    "longtable"
    "xcolor"
    "tcolorbox"
    "textcomp"
    "multicol"
    "natbib"
    "verbatim"
    "float"
    "enumitem")
   (LaTeX-add-labels
    "Bibliography")
   (LaTeX-add-bibliographies
    "Bibliography")
   (LaTeX-add-counters
    "descriptcount"))
 :latex)

