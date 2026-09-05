#!/usr/bin/env python3
"""index.html + app.js + vendor 를 파일 하나로 합칩니다.
사용법:  python3 make_standalone.py   →  deckforge-standalone.html
USB, 사내망, 오프라인 PC 배포용입니다. GitHub Pages 에는 원본 그대로 올리면 됩니다."""
import pathlib
import re

here = pathlib.Path(__file__).parent
html = (here / "index.html").read_text(encoding="utf-8")
app = (here / "app.js").read_text(encoding="utf-8")
lib = (here / "vendor" / "pptxgen.bundle.js").read_text(encoding="utf-8")

html, n = re.subn(r'<!--PPTX_LOADER_START-->.*?<!--PPTX_LOADER_END-->',
                  lambda m: "<script>\nwindow.__pptxDone=true;\n" + lib + "\n</script>",
                  html, count=1, flags=re.S)
assert n == 1, "엔진 로더 구간을 찾지 못했습니다"
html = html.replace(
    '<script src="app.js"></script>',
    "<script>\n" + app + "\n</script>")

out = here / "deckforge-standalone.html"
out.write_text(html, encoding="utf-8")
print("만들었습니다:", out, f"({out.stat().st_size/1024:.0f} KB)")
