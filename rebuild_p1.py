import os

GA = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-SF80B3JYTM"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-SF80B3JYTM');
  </script>"""

def nav(page=""):
    return f"""  <header class="mobile-header">
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

# ---- index.html ----
write("index.html", "Home", "", """      <section class="hero bg-home">
        <h2>Welcome to DIY Chem.</h2>
        <p>このサイトは、材料化学の在野研究者による、日々の研究記録、技術的な考察メモ、および有用なリソースを整理するための個人的なアーカイブです。https://diychem.jp/ として情報を公開しています。</p>
        <div class="flex-row-gap mt-4">
          <a href="research.html" class="btn btn-primary">研究を見る</a>
          <a href="memo.html" class="btn btn-memo">メモを読む</a>
        </div>
      </section>
      <section>
        <h2>最新の活動 / Latest Updates</h2>
        <div class="card-grid">
          <article class="card" data-tag="Methodology">
          <div class="tags-container">
            <span class="card-tag">Research</span>
          </div>
            <h3>機械学習を用いた相図の予測手法</h3>
            <p>既知の相図データを学習データとして、未探索の合金系の相図を予測する手法を提案した。</p>
            <div class="card-footer">
              <time datetime="2026-05-02">2026.05.02</time>
              <a href="research-article-4.html" style="font-weight:600;">詳細へ &rarr;</a>
            </div>
          </article>
          <article class="card" data-tag="Program">
          <div class="tags-container">
            <span class="card-tag memo">Memo</span>
          </div>
            <h3>データベースの活用</h3>
            <p>データベースからAPIやスクリプトを用いて情報を抽出し、解析するプログラム。</p>
            <div class="card-footer">
              <time datetime="2026-04-26">2026.04.26</time>
              <a href="memo-article-4.html" style="font-weight:600;">詳細へ &rarr;</a>
            </div>
          </article>
        </div>
      </section>""")

# ---- about.html ----
write("about.html", "About Us", "about.html", """      <div class="page-header mb-4 bg-about">
        <h1>私たち / About Us</h1>
        <p>DIY Chem. の目的と活動内容について</p>
      </div>
      <section class="mb-4">
        <h2>プロフィール</h2>
        <p>材料化学の分野において、所属機関を持たずに独立して研究を行う在野研究者（DIY Chem.）です。高価な実験設備に頼らず、身近な材料とオープンソース技術を活用した「DIY」アプローチで化学の探求を行っています。</p>
        <p>当サイト（https://diychem.jp/）は、日々の実験記録、合成結果、そしてデータ分析の手法を整理し、広く共有するためのプラットフォームです。</p>
      </section>
      <section class="mb-4">
        <h2>研究テーマ</h2>
        <ul>
          <li class="mb-2"><strong>物質の合成</strong>: 安価で入手しやすい原料から、新規な機能性材料（有機無機ハイブリッドなど）を設計・合成する手法の開拓。</li>
          <li class="mb-2"><strong>データベースの作成と分析</strong>: オープンデータを活用した物性予測や、自身で測定した実験データの体系的なデータベース化と機械学習の適用。</li>
          <li class="mb-2"><strong>新しい研究手法の提案</strong>: 3Dプリンタやマイコンを活用した自作の実験装置や、安価なセンサーを用いた簡易的な測定・分析手法の構築。</li>
        </ul>
      </section>
      <section class="mb-4">
        <h2>著作権</h2>
        <p>このサイトのコンテンツに対して、著作権は放棄しておらず、引用する際は出典を明記するようにお願いします。</p>
      </section>
      <section class="mb-4">
        <h2>プライバシーポリシー</h2>
        <p>当サイトでは、アクセス解析のためにGoogle Analyticsを使用しています。</p>
        <p>Google Analyticsは、トラフィックデータ収集のためにCookieを使用しています。<br>このデータは匿名で収集されており、個人を特定するものではありません。</p>
        <p>この機能はCookieを無効にすることで収集を拒否することができます。<br>お使いのブラウザの設定をご確認ください。</p>
        <p>この規約に関して、詳しくは<a href="https://policies.google.com/technologies/partner-sites?hl=ja" target="_blank" rel="noopener">Googleのポリシー</a>をご確認ください。</p>
      </section>""")

# ---- research.html ----
write("research.html", "Research", "research.html", """      <div class="page-header mb-4 bg-research">
        <h1 id="page-title">研究 / Research</h1>
        <p>物質の設計、データ分析、および新手法のアーカイブ</p>
      </div>
      <div class="card-grid" id="card-container">
        <article class="card" data-tag="Methodology">
          <div class="tags-container">
            <span class="card-tag">Methodology</span>
          </div>
          <h3>機械学習を用いた相図の予測手法</h3>
          <p>既知の相図データを学習データとして、未探索の合金系の相図を予測する手法を提案した。</p>
          <div class="card-footer">
            <time datetime="2026-05-02">2026.05.02</time>
            <a href="research-article-4.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Database">
          <div class="tags-container">
            <span class="card-tag">Database</span>
          </div>
          <h3>無機材料データベースからの新規構造探索</h3>
          <p>特定の配位環境と電子状態を持つ物質群を抽出するスクリーニング手法を構築した。</p>
          <div class="card-footer">
            <time datetime="2026-04-29">2026.04.29</time>
            <a href="research-article-3.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Synthesis">
          <div class="tags-container">
            <span class="card-tag">Synthesis</span>
          </div>
          <h3>Al-Fe-Cu準結晶を形成する組成の調査</h3>
          <p>各種金属原料を混合・加熱し、粉砕・混合・再加熱を繰り返すことで、i相が得られた。</p>
          <div class="card-footer">
            <time datetime="2026-04-10">2026.04.10</time>
            <a href="research-article-2.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Synthesis">
          <div class="tags-container">
            <span class="card-tag">Synthesis</span>
          </div>
          <h3>混合原子価酸化物の合成方法の検討</h3>
          <p>酸化物とTiを同封して真空引きした後に加熱することで、混合原子価の状態で含む酸化物が得られた。</p>
          <div class="card-footer">
            <time datetime="2026-03-31">2026.03.31</time>
            <a href="research-article-1.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
      </div>
      <div id="no-cards-msg" style="display:none;margin-top:2rem;color:#666;">該当する記事が見つかりません。</div>""")

# ---- memo.html ----
write("memo.html", "Memo", "memo.html", """      <div class="page-header mb-4 bg-memo">
        <h1 id="page-title">メモ / Memo</h1>
        <p>実験自作やデータ処理の備忘録</p>
      </div>
      <div class="card-grid" id="card-container">
        <article class="card" data-tag="Program">
          <div class="tags-container">
            <span class="card-tag memo">Program</span>
          </div>
          <h3>データベースの活用</h3>
          <p>データベースからAPIやスクリプトを用いて情報を抽出し、解析するプログラム。</p>
          <div class="card-footer">
            <time datetime="2026-04-26">2026.04.26</time>
            <a href="memo-article-4.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Program,DIY">
          <div class="tags-container">
            <span class="card-tag memo">DIY</span>
            <span class="card-tag memo">Program</span>
          </div>
          <h3>XRD測定時間短縮の検討</h3>
          <p>BEADSなどのソフトウェアを利用することで、測定時間を短縮してもノイズを処理し相同定を行う。</p>
          <div class="card-footer">
            <time datetime="2026-04-22">2026.04.22</time>
            <a href="memo-article-3.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Column">
          <div class="tags-container">
            <span class="card-tag memo">Column</span>
          </div>
          <h3>配位数に依存しないイオン半径の検討</h3>
          <p>配位数の情報を除いたイオンの種類のみから、凡そのイオン半径を一意に決めてしまおうという試み。</p>
          <div class="card-footer">
            <time datetime="2026-04-12">2026.04.12</time>
            <a href="memo-article-2.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="DIY">
          <div class="tags-container">
            <span class="card-tag memo">DIY</span>
          </div>
          <h3>ヤフーオークションの活用</h3>
          <p>中古の装置や部品を揃えるのがおすすめです。</p>
          <div class="card-footer">
            <time datetime="2026-04-03">2026.04.03</time>
            <a href="memo-article-1.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
      </div>
      <div id="no-cards-msg" style="display:none;margin-top:2rem;color:#666;">該当する記事が見つかりません。</div>""")

print("Phase 1 done.")
