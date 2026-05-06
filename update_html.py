import os
import glob

html_files = glob.glob('*.html')

ga_tag = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-SF80B3JYTM"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-SF80B3JYTM');
  </script>
</head>"""

old_sidebar = """            <ul class="sub-menu" id="submenu-research">
              <li><a href="research.html" class="nav-link">研究一覧</a></li>
              <li><a href="research.html?tag=Algorithm" class="nav-link">アルゴリズム</a></li>
              <li><a href="research.html?tag=Data Science" class="nav-link">データサイエンス</a></li>
              <li><a href="research.html?tag=HCI" class="nav-link">HCI</a></li>
              <li><a href="research.html?tag=Systems" class="nav-link">システム</a></li>
            </ul>"""

new_sidebar = """            <ul class="sub-menu" id="submenu-research">
              <li><a href="research-article-1.html" class="nav-link">グラフ探索アルゴリズムの比較</a></li>
              <li><a href="research-article-2.html" class="nav-link">時系列データの異常検知手法</a></li>
              <li><a href="research-article-3.html" class="nav-link">認知負荷を低減するUI設計</a></li>
              <li><a href="research-article-4.html" class="nav-link">分散処理フレームワークの評価</a></li>
            </ul>"""

old_sidebar_memo = """            <ul class="sub-menu" id="submenu-memo">
              <li><a href="memo.html" class="nav-link">メモ一覧</a></li>
              <li><a href="memo.html?tag=Setup" class="nav-link">環境構築</a></li>
              <li><a href="memo.html?tag=CSS" class="nav-link">CSS / UI</a></li>
              <li><a href="memo.html?tag=Git" class="nav-link">Git / 開発手順</a></li>
              <li><a href="memo.html?tag=Tool" class="nav-link">ツール</a></li>
            </ul>"""

new_sidebar_memo = """            <ul class="sub-menu" id="submenu-memo">
              <li><a href="memo-article-1.html" class="nav-link">WSL2でのDocker環境構築</a></li>
              <li><a href="memo-article-2.html" class="nav-link">CSS Gridの便利なスニペット</a></li>
              <li><a href="memo-article-3.html" class="nav-link">Git rebaseのコンフリクト解消</a></li>
              <li><a href="memo-article-4.html" class="nav-link">おすすめのターミナルツール</a></li>
            </ul>"""

old_sidebar_link = """          <li class="nav-item">
            <a href="links.html" class="nav-link">リンク / Link</a>
          </li>
        </ul>"""

new_sidebar_link = """          <li class="nav-item">
            <a href="links.html" class="nav-link">リンク / Link</a>
          </li>
          <li class="nav-item">
            <a href="privacy.html" class="nav-link">プライバシーポリシー / Privacy</a>
          </li>
        </ul>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add GA Tag
    if "G-SF80B3JYTM" not in content:
        content = content.replace("</head>", ga_tag)
    
    # 2. Update button in index.html
    if file == 'index.html':
        content = content.replace('<a href="memo.html" class="btn btn-outline">メモを読む</a>', '<a href="memo.html" class="btn btn-memo">メモを読む</a>')
        
    # 3. Update sidebar
    content = content.replace(old_sidebar, new_sidebar)
    content = content.replace(old_sidebar_memo, new_sidebar_memo)
    content = content.replace(old_sidebar_link, new_sidebar_link)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 4. Create privacy.html
privacy_content = ""
with open('index.html', 'r', encoding='utf-8') as f:
    privacy_content = f.read()

# Extract header and sidebar up to main-content
main_start = privacy_content.find('<main class="main-content">')
if main_start != -1:
    main_start += len('<main class="main-content">')
footer_start = privacy_content.find('</main>')

top_part = privacy_content[:main_start]
bottom_part = privacy_content[footer_start:]

privacy_body = """
      <div class="page-header mb-4 bg-about">
        <h1>プライバシーポリシー / Privacy</h1>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>当サイトでは、アクセス解析のためにGoogle Analyticsを使用しています。</p>
        <p>Google Analyticsは、トラフィックデータ収集のためにCookieを使用しています。<br>
        このデータは匿名で収集されており、個人を特定するものではありません。</p>
        <p>この機能はCookieを無効にすることで収集を拒否することができます。<br>
        お使いのブラウザの設定をご確認ください。</p>
        <p>この規約に関して、詳しくは<a href="https://policies.google.com/technologies/partner-sites?hl=ja" target="_blank" rel="noopener">Googleのポリシー</a>をご確認ください。</p>
      </div>"""

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(top_part + privacy_body + bottom_part)
    
# Title update for privacy.html
with open('privacy.html', 'r', encoding='utf-8') as f:
    pc = f.read()
pc = pc.replace('<title>T. Lab | Home</title>', '<title>T. Lab | Privacy Policy</title>')
with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(pc)

print("HTML files updated successfully!")
