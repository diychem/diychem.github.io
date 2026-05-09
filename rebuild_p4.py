import os

GA = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-SF80B3JYTM"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-SF80B3JYTM');
  </script>"""

def nav():
    return """  <header class="mobile-header">
    <div class="mobile-brand">DIY <span>Chem.</span></div>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </button>
  </header>
  <div class="overlay" id="overlay"></div>
  <div class="app-container">
    <aside class="sidebar" id="sidebar">
      <div class="site-brand">
        <h1>DIY <span>Chem.</span></h1>
        <p>Research &amp; Archives</p>
      </div>
      <nav class="nav-menu">
        <ul class="nav-list">
          <li class="nav-item"><a href="index.html" class="nav-link">ホーム / Home</a></li>
          <li class="nav-item"><a href="about.html" class="nav-link">私たち / About Us</a></li>
          <li class="nav-item">
            <a href="research.html" class="nav-link nav-parent" data-toggle="collapse" data-target="submenu-research">研究 / Research<span class="toggle-icon">▼</span></a>
            <ul class="sub-menu" id="submenu-research">
              <li><a href="research.html?tag=Synthesis" class="nav-link">物質の合成 / Synthesis</a></li>
              <li><a href="research.html?tag=Database" class="nav-link">データベース / Database</a></li>
              <li><a href="research.html?tag=Methodology" class="nav-link">手法の提案 / Methodology</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a href="memo.html" class="nav-link nav-parent" data-toggle="collapse" data-target="submenu-memo">メモ / Memo<span class="toggle-icon">▼</span></a>
            <ul class="sub-menu" id="submenu-memo">
              <li><a href="memo.html?tag=DIY" class="nav-link">自作 / DIY</a></li>
              <li><a href="memo.html?tag=Program" class="nav-link">プログラム / Program</a></li>
              <li><a href="memo.html?tag=Column" class="nav-link">コラム / Column</a></li>
            </ul>
          </li>
          <li class="nav-item"><a href="document.html" class="nav-link">資料 / Document</a></li>
          <li class="nav-item"><a href="tool.html" class="nav-link">ツール / Tool</a></li>
          <li class="nav-item"><a href="database.html" class="nav-link">データ / Database</a></li>
          <li class="nav-item"><a href="equipment.html" class="nav-link">設備 / Equipment</a></li>
          <li class="nav-item"><a href="links.html" class="nav-link">リンク / Link</a></li>
        </ul>
      </nav>
    </aside>
    <main class="main-content">"""

FOOT = """    </main>
  </div>
  <script src="js/script.js"></script>
</body>
</html>"""

def head(title, canonical):
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DIY Chem. | {title}</title>
  <meta name="description" content="材料化学の在野研究者によるDIY Chem.の研究成果・メモ・リンク集">
  <link rel="canonical" href="https://diychem.jp/{canonical}">
  <link rel="stylesheet" href="css/style.css">
{GA}
</head>
<body>"""

def write(filename, title, canonical, body):
    content = head(title, canonical) + "\n" + nav() + "\n" + body + "\n" + FOOT
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {filename}")

write("database-article-1.html", "無機材料 結晶構造データセット", "database-article-1.html", """      <div class="page-header mb-4">
        <div class="tags-container">
          <span class="card-tag data">Data</span>
        </div>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">無機材料 結晶構造データセット</h1>
        <p>2026.05.09</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>過去に合成した試料のXRDパターンとリートベルト解析結果を整理したデータセットです。</p>
        <div class="mt-4"><a href="database.html" class="btn btn-outline">&larr; データ一覧に戻る</a></div>
      </div>""")

write("tool-article-1.html", "画像の背景除去", "tool-article-1.html", """      <div class="page-header mb-4">
        <div class="tags-container">
          <span class="card-tag memo">App</span>
        </div>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">画像の背景除去</h1>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>ここに画像の背景除去ツールのインターフェースが入ります。(仮ページ)</p>
        <div class="mt-4"><a href="tool.html" class="btn btn-outline">&larr; ツール一覧に戻る</a></div>
      </div>""")

write("tool-article-2.html", "スペクトルのバックグラウンド分離", "tool-article-2.html", """      <div class="page-header mb-4">
        <div class="tags-container">
          <span class="card-tag memo">App</span>
        </div>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">スペクトルのバックグラウンド分離</h1>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>ここにスペクトルのバックグラウンド分離ツールのインターフェースが入ります。(仮ページ)</p>
        <div class="mt-4"><a href="tool.html" class="btn btn-outline">&larr; ツール一覧に戻る</a></div>
      </div>""")

print("Phase 4 done.")
