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


## Unified fixed-bias manuscript v0.5

The standalone unified source is `paper/manuscript_biased.tex`, integrating `MANUSCRIPT_BIASED.md` and `BIASED_PROOF_APPENDICES.md`. The earlier fair-only source `manuscript.tex` remains intact. From the repository root, using the same TeX dependencies:

```sh
mkdir -p paper/build
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=paper/build paper/manuscript_biased.tex
```

If successful the output is `paper/build/manuscript_biased.pdf`. The workflow now has separate matrix jobs for both sources; the unified PDF/log artifact is named `manuscript_biased-and-build-log`. A workflow run ID is required to retrieve job logs through the connected repository interface. The commit-run query only lists pull-request-triggered runs; an empty result does not establish that push-triggered runs did not occur.

Conversion status: 79 original indented display blocks (77 math displays and two encoding lists), four tables and one pseudocode algorithm retained. Formula displays were manually mapped; the prose conversion and a conservative inline-notation pass are editorial, not a checked proof of transcription equivalence. Static brace, environment and inline-dollar balance passed. Some ASCII inline expressions remain and need manual review. No full v0.5 build or rendered pages have been verified. The earlier representative smoke test is not evidence of full compilation. Do not call this source a submission-ready PDF.
