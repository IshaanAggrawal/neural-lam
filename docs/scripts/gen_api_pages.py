# Standard library
from pathlib import Path

# Third-party
import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
for path in sorted(Path("neural_lam").rglob("*.py")):
    if path.name.startswith("_"):
        continue
    module = ".".join(path.with_suffix("").parts)
    doc_path = Path("api") / path.relative_to("neural_lam").with_suffix(".md")
    with mkdocs_gen_files.open(doc_path, "w") as f:
        f.write(f"::: {module}\n")
    nav[path.parts[1:]] = doc_path.relative_to("api").as_posix()
with mkdocs_gen_files.open("api/SUMMARY.md", "w") as f:
    f.writelines(nav.build_literate_nav())
