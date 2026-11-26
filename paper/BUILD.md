# Building the manuscript

The standalone LaTeX source is `paper/manuscript.tex` (working manuscript v0.3). The integrated Markdown version is retained at `paper/MANUSCRIPT_FULL.md`.

## Local compilation

From the repository root, install a recent TeX Live distribution with LaTeX extra packages, recommended fonts, Latin Modern, and latexmk. For example on Ubuntu:

```sh
sudo apt-get update
sudo apt-get install -y latexmk texlive-latex-extra texlive-fonts-recommended lmodern
mkdir -p paper/build
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=paper/build paper/manuscript.tex
```

The output, if compilation succeeds, is `paper/build/manuscript.pdf`. Inspect the log for errors, unresolved references, and overfull boxes; inspect the actual rendered pages before release. Do not use the smoke-test PDF as the manuscript.

## Verification status

- The repository source passed a static balance check of environments, braces and inline math delimiters (excluding the verbatim algorithm blocks).
- A local one-page smoke test of the same preamble, theorem/proof environments, the representative forced-pair expectation and characteristic-formula displays, table and verbatim environment compiled successfully with latexmk/pdfTeX 1.40.26 (TeX Live 2025/dev/Debian), zero fatal errors.
- That local test was **not a compilation of the complete manuscript**. The local runtime could not retrieve the repository bytes (DNS/URL download restrictions); the connected GitHub tools verified the committed text but do not expose a TeX execution action.
- The dedicated paper build workflow is intended to provide the actual full-source compilation and PDF/log artifact. No successful workflow run has yet been verified. Author/affiliation, final notation and layout, literature priority, external mathematical review, and Lean verification remain release gates.
