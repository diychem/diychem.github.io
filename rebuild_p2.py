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
          <li class="nav-item"><a href="tool.html" class="nav-link">ツール / Tool</a></li>
          <li class="nav-item"><a href="document.html" class="nav-link">資料 / Document</a></li>
          <li class="nav-item"><a href="database.html" class="nav-link">データ / Database</a></li>
          <li class="nav-item"><a href="equipment.html" class="nav-link">設備 / Equipment</a></li>
          <li class="nav-item"><a href="links.html" class="nav-link">リンク / Link</a></li>
          <li class="nav-item"><a href="privacy.html" class="nav-link">プライバシーポリシー / Privacy</a></li>
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

# Research articles
write("research-article-1.html", "混合原子価酸化物の合成方法の検討", "research-article-1.html", """      <div class="page-header mb-4">
        <span class="card-tag">Synthesis</span>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">混合原子価酸化物の合成方法の検討</h1>
        <p>2026.03.31</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <h2>背景</h2>
        <p>混合原子価酸化物はその電子状態から種々の物性が期待できるが、大気中での焼成では最大の安定な価数まで酸化されてしまうことが多く、合成することが困難である。</p>
        <h2>結論</h2>
        <p>酸化物とTiを同封して真空引きした後に加熱することで、Tiよりも還元されやすいFeなどの金属元素を混合原子価の状態で含む酸化物が得られた。</p>
        <h2>補足</h2>
        <p>H2等の能動的な還元剤で価数を調整しようとすると金属状態まで還元されてしまいやすいため、混合原子価の状態にしたい金属元素よりも酸化されやすい金属をゲッターとして用いることが有効である。</p>
        <h2>引用文献</h2>
        <p>[1] XXXX<br>[2] XXXX<br>[3] XXXX</p>
        <div class="mt-4"><a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a></div>
      </div>""")

write("research-article-2.html", "Al-Fe-Cu準結晶を形成する組成の調査", "research-article-2.html", """      <div class="page-header mb-4">
        <span class="card-tag">Synthesis</span>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">Al-Fe-Cu準結晶を形成する組成の調査</h1>
        <p>2026.04.10</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <h2>背景</h2>
        <p>Al-Fe-Cu系において準結晶（i相）が形成される組成範囲を実験的に調査した。</p>
        <h2>結論</h2>
        <p>各種金属原料を混合・加熱し、粉砕・混合・再加熱を繰り返すことで、i相が得られた。</p>
        <h2>引用文献</h2>
        <p>[1] XXXX<br>[2] XXXX</p>
        <div class="mt-4"><a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a></div>
      </div>""")

write("research-article-3.html", "無機材料データベースからの新規構造探索", "research-article-3.html", """      <div class="page-header mb-4">
        <span class="card-tag">Database</span>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">無機材料データベースからの新規構造探索</h1>
        <p>2026.04.29</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <h2>背景</h2>
        <p>ICSDやMaterials Projectなどの公開データベースを活用し、特定の配位環境を持つ物質群を系統的に探索した。</p>
        <h2>結論</h2>
        <p>特定の配位環境と電子状態を持つ物質群を抽出するスクリーニング手法を構築した。</p>
        <h2>引用文献</h2>
        <p>[1] XXXX<br>[2] XXXX</p>
        <div class="mt-4"><a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a></div>
      </div>""")

write("research-article-4.html", "機械学習を用いた相図の予測手法", "research-article-4.html", """      <div class="page-header mb-4">
        <span class="card-tag">Methodology</span>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">機械学習を用いた相図の予測手法</h1>
        <p>2026.05.02</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <h2>背景</h2>
        <p>既知の相図データを学習データとして、未探索の合金系の相図を予測する機械学習モデルを構築した。</p>
        <h2>結論</h2>
        <p>既知の相図データを学習データとして、未探索の合金系の相図を予測する手法を提案した。</p>
        <h2>引用文献</h2>
        <p>[1] XXXX<br>[2] XXXX</p>
        <div class="mt-4"><a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a></div>
      </div>""")

print("Phase 2 done.")
