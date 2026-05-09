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

# Memo articles
write("memo-article-1.html", "ヤフーオークションの活用", "memo-article-1.html", """      <div class="page-header mb-4">
        <div class="tags-container">
          <span class="card-tag memo">DIY</span>
        </div>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">ヤフーオークションの活用</h1>
        <p>2026.04.03</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>新品で実験装置を買うのは非常に高価であり、個人での研究活動には大きな負担となります。そこで、ヤフーオークションを活用して中古の装置や部品を揃えるのがおすすめです。</p>
        <p>例えば、電気炉などは陶芸用のものが比較的安価に出品されていることがあり、少しの改造で実験用に転用することが可能です。</p>
        <div class="mt-4"><a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a></div>
      </div>""")

write("memo-article-2.html", "配位数に依存しないイオン半径の検討", "memo-article-2.html", """      <div class="page-header mb-4">
        <div class="tags-container">
          <span class="card-tag memo">Column</span>
        </div>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">配位数に依存しないイオン半径の検討</h1>
        <p>2026.04.12</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>配位数の情報を除いたイオンの種類のみから、凡そのイオン半径を一意に決めてしまおうという試み。</p>
        <p>Shannon等が報告したイオン半径のデータを配位数で平均化することで、簡便な指標として利用できる可能性がある。</p>
        <div class="mt-4"><a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a></div>
      </div>""")

write("memo-article-3.html", "XRD測定時間短縮の検討", "memo-article-3.html", """      <div class="page-header mb-4">
        <div class="tags-container">
          <span class="card-tag memo">DIY</span>
          <span class="card-tag memo">Program</span>
        </div>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">XRD測定時間短縮の検討</h1>
        <p>2026.04.22</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>BEADSなどのソフトウェアを利用することで、測定時間を短縮してもノイズを処理し相同定を行う。</p>
        <p>短時間測定で生じたノイズをベイズ推定によって除去し、ピーク位置の同定精度を維持する手法を検討した。</p>
        <div class="mt-4"><a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a></div>
      </div>""")

write("memo-article-4.html", "データベースの活用", "memo-article-4.html", """      <div class="page-header mb-4">
        <div class="tags-container">
          <span class="card-tag memo">Program</span>
        </div>
        <h1 style="margin-top:0.5rem;border:none;padding:0;">データベースの活用</h1>
        <p>2026.04.26</p>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>データベースからAPIやスクリプトを用いて情報を抽出し、解析するプログラム。</p>
        <p>Materials ProjectのAPIを使って特定の組成系のデータを一括取得し、Pythonで解析するワークフローを構築した。</p>
        <div class="mt-4"><a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a></div>
      </div>""")

# links.html, privacy.html, tool.html, document.html, database.html, equipment.html
write("links.html", "Link", "links.html", """      <div class="page-header mb-4 bg-link">
        <h1>リンク / Link</h1>
        <p>外部リソースや関連サイトへのリンク集</p>
      </div>
      <div class="alert-construction">
        <h3>🚧 Under Construction</h3>
        <p>現在このページは準備中です。関連サイトや役立つリソースのリストを後日追加する予定です。</p>
        <div class="mt-4"><a href="index.html" class="btn btn-primary">ホームに戻る</a></div>
      </div>""")

write("privacy.html", "Privacy Policy", "privacy.html", """      <div class="page-header mb-4 bg-about">
        <h1>プライバシーポリシー / Privacy</h1>
      </div>
      <div class="article-content" style="max-width:800px;">
        <p>当サイトでは、アクセス解析のためにGoogle Analyticsを使用しています。</p>
        <p>Google Analyticsは、トラフィックデータ収集のためにCookieを使用しています。<br>このデータは匿名で収集されており、個人を特定するものではありません。</p>
        <p>この機能はCookieを無効にすることで収集を拒否することができます。<br>お使いのブラウザの設定をご確認ください。</p>
        <p>この規約に関して、詳しくは<a href="https://policies.google.com/technologies/partner-sites?hl=ja" target="_blank" rel="noopener">Googleのポリシー</a>をご確認ください。</p>
      </div>""")

write("tool.html", "Tool", "tool.html", """      <div class="page-header mb-4 bg-tool">
        <h1>ツール / Tool</h1>
        <p>データ解析等に使うアプリの置き場</p>
      </div>
      <div class="card-grid">
        <article class="card">
        <div class="tags-container">
          <span class="card-tag memo">App</span>
        </div>
          <h3>画像の背景除去</h3>
          <p>実験器具やサンプルの写真から背景を自動で取り除くツール。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="tool-article-1.html" style="font-weight:600;">ツールを開く &rarr;</a>
          </div>
        </article>
        <article class="card">
        <div class="tags-container">
          <span class="card-tag memo">App</span>
        </div>
          <h3>スペクトルのバックグラウンド分離</h3>
          <p>XRDやXPSなどのスペクトルデータからバックグラウンド成分を分離するツール。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="tool-article-2.html" style="font-weight:600;">ツールを開く &rarr;</a>
          </div>
        </article>
      </div>""")

write("document.html", "Document", "document.html", """      <div class="page-header mb-4 bg-document">
        <h1>資料 / Document</h1>
        <p>プレゼン資料(PDF)の置き場</p>
      </div>
      <div class="card-grid">
        <article class="card">
        <div class="tags-container">
          <span class="card-tag memo">PDF</span>
        </div>
          <h3>2026年 学会発表スライド</h3>
          <p>混合原子価酸化物の合成と特性評価に関する発表資料です。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="dummy.pdf" target="_blank" style="font-weight:600;">PDFを開く &rarr;</a>
          </div>
        </article>
      </div>""")

write("database.html", "Database", "database.html", """      <div class="page-header mb-4 bg-database">
        <h1>データ / Database</h1>
        <p>収集・整理したデータの置き場</p>
      </div>
      <div class="card-grid">
        <article class="card">
        <div class="tags-container">
          <span class="card-tag data">Data</span>
        </div>
          <h3>無機材料 結晶構造データセット</h3>
          <p>過去に合成した試料のXRDパターンとリートベルト解析結果のまとめ。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="database-article-1.html" style="font-weight:600;">詳細へ &rarr;</a>
          </div>
        </article>
      </div>""")

equipments = [
    ("3Dプリンタ","部品の試作や治具の作成に使用します。"),
    ("電子天秤","試薬の精密な計量に使用します。"),
    ("ホットスターラー","加熱と撹拌を同時に行う装置です。"),
    ("電気炉","試料の焼成や熱処理に使用します。"),
    ("管状炉","特定のガス雰囲気下での加熱処理に使用します。"),
    ("温度制御装置","電気炉などの温度プロファイルを制御します。"),
    ("真空ポンプ","真空引きや減圧環境の作成に使用します。"),
    ("圧力計","系内の圧力を測定します。"),
    ("データロガー","温度や電圧などのデータを連続記録します。"),
]
eq_cards = ""
for name, desc in equipments:
    eq_cards += f"""
        <article class="card">
          <div style="background:#e8e8e8;width:100%;height:180px;border-radius:6px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;color:#777;font-size:0.9rem;">[{name} 写真]</div>
          <h3 style="margin-top:0;font-size:1.1rem;">{name}</h3>
          <p>{desc}</p>
        </article>"""

write("equipment.html", "Equipment", "equipment.html", f"""      <div class="page-header mb-4 bg-equipment">
        <h1 style="border:none;">設備 / Equipment</h1>
        <p>保有している装置の紹介</p>
      </div>
      <div class="card-grid">{eq_cards}
      </div>""")

print("Phase 3 done.")
