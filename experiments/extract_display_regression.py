"""Extract exactly the standalone math displays from the unified manuscript.

Usage from the repository root:
    python3 experiments/extract_display_regression.py
    cd paper/build
    latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error display-test.tex

This isolates formula syntax/layout errors. It is not a full manuscript build
or a semantic check against the original Markdown.
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = (root / "paper/manuscript_biased.tex").read_text(encoding="utf-8")
preamble, _ = source.split(r"\begin{document}", 1)
displays = re.findall(r"\\\[\n([\s\S]*?)\n\\\]", source)
assert len(displays) == 77, f"Expected 77 displays, got {len(displays)}"
joined = "\n".join(displays)
fingerprint = 2166136261
for c in joined:
    fingerprint = ((fingerprint ^ ord(c)) * 16777619) & 0xffffffff
print(f"{len(displays)} displays; {len(joined)} characters; FNV-1a {fingerprint:08x}")
output = root / "paper/build/display-test.tex"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(
    preamble
    + "\n" + r"\title{Formula-only regression test}" + "\n"
    + r"\author{}" + "\n" + r"\date{}" + "\n"
    + r"\begin{document}" + "\n" + r"\maketitle" + "\n"
    + "\n".join(r"\[" + "\n" + d + "\n" + r"\]" for d in displays)
    + "\n" + r"\end{document}" + "\n",
    encoding="utf-8",
)
print(output)
