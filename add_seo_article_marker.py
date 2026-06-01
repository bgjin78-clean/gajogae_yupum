from pathlib import Path

REGIONS_DIR = Path("regions")

START = "<!-- SEO_ARTICLE_START -->"
END = "<!-- SEO_ARTICLE_END -->"

marker = f"""
<section class="seo-article" id="seo-article">
  <div class="wrap">
    {START}
    {END}
  </div>
</section>
"""

for file_path in REGIONS_DIR.glob("*.html"):
    if file_path.name.endswith(".backup"):
        continue

    html = file_path.read_text(encoding="utf-8")

    if START in html:
        print(f"이미 있음: {file_path.name}")
        continue

    if "</main>" not in html:
        print(f"</main> 없음: {file_path.name}")
        continue

    html = html.replace("</main>", marker + "\n</main>")

    file_path.write_text(html, encoding="utf-8")
    print(f"삽입 완료: {file_path.name}")