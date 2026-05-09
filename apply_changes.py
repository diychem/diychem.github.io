import os
import glob
import re

html_files = glob.glob('*.html')

new_nav = """      <nav class="nav-menu">
        <ul class="nav-list">
          <li class="nav-item"><a href="index.html" class="nav-link">ホーム / Home</a></li>
          <li class="nav-item"><a href="about.html" class="nav-link">私たち / About Us</a></li>
          <li class="nav-item">
            <a href="#" class="nav-link" data-toggle="collapse" data-target="submenu-research">研究 / Research<span class="toggle-icon">▼</span></a>
            <ul class="sub-menu" id="submenu-research">
              <li><a href="research-article-4.html" class="nav-link">機械学習を用いた相図の予測手法</a></li>
              <li><a href="research-article-3.html" class="nav-link">無機材料データベースからの新規構造探索</a></li>
              <li><a href="research-article-2.html" class="nav-link">Al-Fe-Cu準結晶を形成する組成の調査</a></li>
              <li><a href="research-article-1.html" class="nav-link">混合原子価酸化物の合成方法の検討</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" data-toggle="collapse" data-target="submenu-memo">メモ / Memo<span class="toggle-icon">▼</span></a>
            <ul class="sub-menu" id="submenu-memo">
              <li><a href="memo-article-4.html" class="nav-link">データベースの活用</a></li>
              <li><a href="memo-article-3.html" class="nav-link">XRD測定時間短縮の検討</a></li>
              <li><a href="memo-article-2.html" class="nav-link">配位数に依存しないイオン半径の検討</a></li>
              <li><a href="memo-article-1.html" class="nav-link">ヤフーオークションの活用</a></li>
            </ul>
          </li>
          <li class="nav-item"><a href="document.html" class="nav-link">資料 / Document</a></li>
          <li class="nav-item"><a href="database.html" class="nav-link">データ / Database</a></li>
          <li class="nav-item"><a href="tool.html" class="nav-link">ツール / Tool</a></li>
          <li class="nav-item"><a href="equipment.html" class="nav-link">設備 / Equipment</a></li>
          <li class="nav-item"><a href="links.html" class="nav-link">リンク / Link</a></li>
          <li class="nav-item"><a href="privacy.html" class="nav-link">プライバシーポリシー / Privacy</a></li>
        </ul>
      </nav>"""

nav_regex = re.compile(r'<nav class="nav-menu">.*?</nav>', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace nav menu
    content = nav_regex.sub(new_nav, content)
    
    # 3. Update About Us
    if file == 'about.html':
        notice = '<p style="color: var(--accent-strong-dark); font-weight: bold; margin-top: 2rem; padding: 1rem; background: rgba(255,159,127,0.1); border-left: 4px solid var(--accent-strong);">このサイトのコンテンツに対して、著作権は放棄しておらず、引用する際は明記するように注意してください。</p>'
        if '著作権は放棄しておらず' not in content:
            content = content.replace('</section>', '</section>\n      ' + notice, 1) # Insert in first section or at end

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Now, generate the new pages using index.html as a template
with open('index.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

main_start = template_content.find('<main class="main-content">')
if main_start != -1:
    main_start += len('<main class="main-content">')
footer_start = template_content.find('</main>')

top_part = template_content[:main_start]
bottom_part = template_content[footer_start:]

def create_page(filename, title, body):
    head = top_part.replace('<title>DIY Chem. | Home</title>', f'<title>DIY Chem. | {title}</title>')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(head + '\n' + body + '\n' + bottom_part)

# --- Document Page ---
document_body = """
      <div class="page-header mb-4" style="background-image: linear-gradient(135deg, rgba(32, 32, 32, 0.85) 0%, rgba(32, 32, 32, 0.95) 100%); border-left: 6px solid var(--aux-color); padding: 3rem; border-radius: 12px;">
        <h1 style="color: #FFFFFF; border: none;">資料 / Document</h1>
        <p style="color: rgba(255, 255, 255, 0.9); margin-top: 0.5rem;">プレゼン資料(pdf)の置き場</p>
      </div>
      <div class="card-grid">
        <article class="card">
          <span class="card-tag">PDF</span>
          <h3>2026年 学会発表スライド</h3>
          <p>混合原子価酸化物の合成と特性評価に関する発表資料です。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="dummy.pdf" target="_blank" style="font-weight:600;">PDFを開く &rarr;</a>
          </div>
        </article>
      </div>
"""
create_page('document.html', 'Document', document_body)

# --- Database Page ---
database_body = """
      <div class="page-header mb-4" style="background-image: linear-gradient(135deg, rgba(32, 32, 32, 0.85) 0%, rgba(32, 32, 32, 0.95) 100%); border-left: 6px solid var(--accent-color); padding: 3rem; border-radius: 12px;">
        <h1 style="color: #FFFFFF; border: none;">データ / Database</h1>
        <p style="color: rgba(255, 255, 255, 0.9); margin-top: 0.5rem;">収集・整理したデータの置き場</p>
      </div>
      <div class="card-grid">
        <article class="card">
          <span class="card-tag">Data</span>
          <h3>無機材料 結晶構造データセット</h3>
          <p>過去に合成した試料のXRDパターンとリートベルト解析結果のまとめ。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="database-article-1.html" style="font-weight:600;">詳細へ &rarr;</a>
          </div>
        </article>
      </div>
"""
create_page('database.html', 'Database', database_body)

database_article_body = """
      <div class="page-header mb-4">
        <span class="card-tag">Data</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">無機材料 結晶構造データセット</h1>
        <p>2026.05.09</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>過去に合成した試料のXRDパターンとリートベルト解析結果を整理したデータセットです。</p>
        <div class="mt-4">
          <a href="database.html" class="btn btn-outline">&larr; データ一覧に戻る</a>
        </div>
      </div>
"""
create_page('database-article-1.html', 'Database Article', database_article_body)

# --- Tool Page ---
tool_body = """
      <div class="page-header mb-4" style="background-image: linear-gradient(135deg, rgba(32, 32, 32, 0.85) 0%, rgba(32, 32, 32, 0.95) 100%); border-left: 6px solid var(--accent-strong); padding: 3rem; border-radius: 12px;">
        <h1 style="color: #FFFFFF; border: none;">ツール / Tool</h1>
        <p style="color: rgba(255, 255, 255, 0.9); margin-top: 0.5rem;">データ解析等に使うアプリの置き場</p>
      </div>
      <div class="card-grid">
        <article class="card">
          <span class="card-tag memo">App</span>
          <h3>画像の背景除去</h3>
          <p>実験器具やサンプルの写真から背景を自動で取り除くツール。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="tool-article-1.html" style="font-weight:600;">ツールを開く &rarr;</a>
          </div>
        </article>
        <article class="card">
          <span class="card-tag memo">App</span>
          <h3>スペクトルのバックグラウンド分離</h3>
          <p>XRDやXPSなどのスペクトルデータからバックグラウンド成分を分離するツール。</p>
          <div class="card-footer">
            <time datetime="2026-05-09">2026.05.09</time>
            <a href="tool-article-2.html" style="font-weight:600;">ツールを開く &rarr;</a>
          </div>
        </article>
      </div>
"""
create_page('tool.html', 'Tool', tool_body)

tool_article_1_body = """
      <div class="page-header mb-4">
        <span class="card-tag memo">App</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">画像の背景除去</h1>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>ここに画像の背景除去ツールのインターフェースが入ります。(仮ページ)</p>
        <div class="mt-4">
          <a href="tool.html" class="btn btn-outline">&larr; ツール一覧に戻る</a>
        </div>
      </div>
"""
create_page('tool-article-1.html', 'Image Background Removal', tool_article_1_body)

tool_article_2_body = """
      <div class="page-header mb-4">
        <span class="card-tag memo">App</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">スペクトルのバックグラウンド分離</h1>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>ここにスペクトルのバックグラウンド分離ツールのインターフェースが入ります。(仮ページ)</p>
        <div class="mt-4">
          <a href="tool.html" class="btn btn-outline">&larr; ツール一覧に戻る</a>
        </div>
      </div>
"""
create_page('tool-article-2.html', 'Spectrum Background Separation', tool_article_2_body)

# --- Equipment Page ---
equipment_body = """
      <div class="page-header mb-4" style="background-image: linear-gradient(135deg, rgba(32, 32, 32, 0.85) 0%, rgba(32, 32, 32, 0.95) 100%); border-left: 6px solid var(--aux-color-dark); padding: 3rem; border-radius: 12px;">
        <h1 style="color: #FFFFFF; border: none;">設備 / Equipment</h1>
        <p style="color: rgba(255, 255, 255, 0.9); margin-top: 0.5rem;">保有している装置の紹介</p>
      </div>
      <div class="card-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));">
"""
equipments = [
    ("3Dプリンタ", "部品の試作や治具の作成に使用します。"),
    ("電子天秤", "試薬の精密な計量に使用します。"),
    ("ホットスターラー", "加熱と撹拌を同時に行う装置です。"),
    ("電気炉", "試料の焼成や熱処理に使用します。"),
    ("管状炉", "特定のガス雰囲気下での加熱処理に使用します。"),
    ("温度制御装置", "電気炉などの温度プロファイルを制御します。"),
    ("真空ポンプ", "真空引きや減圧環境の作成に使用します。"),
    ("圧力計", "系内の圧力を測定します。"),
    ("データロガー", "温度や電圧などのデータを連続記録します。")
]

for name, desc in equipments:
    equipment_body += f'''
        <article class="card">
          <img src="https://via.placeholder.com/400x250?text={name}" alt="{name}" style="border-radius:6px; margin-bottom:1rem; object-fit: cover; width: 100%; height: 200px; background:#e0e0e0; color:#555; display:flex; align-items:center; justify-content:center; font-weight:bold;">
          <h3 style="margin-top:0.5rem; font-size:1.1rem;">{name}</h3>
          <p>{desc}</p>
        </article>
'''

equipment_body += "      </div>"
create_page('equipment.html', 'Equipment', equipment_body)

print("All updates applied!")
