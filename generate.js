const fs = require('fs');
const path = require('path');

const head = (title) => `<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>T. Lab | ${title}</title>
  <meta name="description" content="個人研究、メモ、リンクを整理する学術・研究サイト">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>`;

const headerAndSidebar = `  <!-- Mobile Header -->
  <header class="mobile-header">
    <div class="mobile-brand">T. <span>Lab</span></div>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </button>
  </header>

  <div class="overlay" id="overlay"></div>

  <div class="app-container">
    <!-- Sidebar Navigation -->
    <aside class="sidebar" id="sidebar">
      <div class="site-brand">
        <h1>T. <span>Lab</span></h1>
        <p>Research & Archives</p>
      </div>

      <nav class="nav-menu">
        <ul class="nav-list">
          <li class="nav-item">
            <a href="index.html" class="nav-link">ホーム / Home</a>
          </li>
          <li class="nav-item">
            <a href="about.html" class="nav-link">私たち / About Us</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" data-toggle="collapse" data-target="submenu-research">
              研究 / Research
              <span class="toggle-icon">▼</span>
            </a>
            <ul class="sub-menu" id="submenu-research">
              <li><a href="research.html" class="nav-link">研究一覧</a></li>
              <li><a href="research.html?tag=Algorithm" class="nav-link">アルゴリズム</a></li>
              <li><a href="research.html?tag=Data Science" class="nav-link">データサイエンス</a></li>
              <li><a href="research.html?tag=HCI" class="nav-link">HCI</a></li>
              <li><a href="research.html?tag=Systems" class="nav-link">システム</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" data-toggle="collapse" data-target="submenu-memo">
              メモ / Memo
              <span class="toggle-icon">▼</span>
            </a>
            <ul class="sub-menu" id="submenu-memo">
              <li><a href="memo.html" class="nav-link">メモ一覧</a></li>
              <li><a href="memo.html?tag=Setup" class="nav-link">環境構築</a></li>
              <li><a href="memo.html?tag=CSS" class="nav-link">CSS / UI</a></li>
              <li><a href="memo.html?tag=Git" class="nav-link">Git / 開発手順</a></li>
              <li><a href="memo.html?tag=Tool" class="nav-link">ツール</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a href="links.html" class="nav-link">リンク / Link</a>
          </li>
        </ul>
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="main-content">`;

const foot = `    </main>
  </div>
  <script src="js/script.js"></script>
</body>
</html>`;

const pages = {
  'index.html': {
    title: 'Home',
    content: `
      <section class="hero">
        <h2>Welcome to Research Archive</h2>
        <p>このサイトは、日々の研究記録、技術的な考察メモ、および有用なリソースを整理するための個人的なアーカイブです。研究者やエンジニアにとって直感的にアクセスできる構成を目指しています。</p>
        <div class="flex-row-gap mt-4">
          <a href="research.html" class="btn btn-primary">研究を見る</a>
          <a href="memo.html" class="btn btn-outline">メモを読む</a>
        </div>
      </section>

      <section>
        <h2>最新の活動 / Latest Updates</h2>
        <div class="card-grid">
          <article class="card" data-tag="Algorithm">
            <span class="card-tag">Research</span>
            <h3>新しい解析手法の検討</h3>
            <p>最近提案されたアルゴリズムの性能評価とその応用について、初期の考察をまとめました。</p>
            <div class="card-footer">
              <time datetime="2026-05-01">2026.05.01</time>
              <a href="research-article-1.html" style="font-weight:600;">詳細へ &rarr;</a>
            </div>
          </article>
          <article class="card" data-tag="Setup">
            <span class="card-tag memo">Memo</span>
            <h3>開発環境のセットアップ</h3>
            <p>プロジェクトに必要なツールのインストール手順や、推奨される設定についての備忘録です。</p>
            <div class="card-footer">
              <time datetime="2026-04-28">2026.04.28</time>
              <a href="memo-article-1.html" style="font-weight:600;">詳細へ &rarr;</a>
            </div>
          </article>
        </div>
      </section>`
  },
  'about.html': {
    title: 'About Us',
    content: `
      <div class="page-header mb-4">
        <h1>私たち / About Us</h1>
        <p>当サイトの目的と活動内容について</p>
      </div>
      <section class="mb-4">
        <h2>プロフィール</h2>
        <p>独立した研究者として、計算機科学および関連分野の探求を行っています。理論と実践の橋渡しをテーマに、日々新しい技術の検証と考察を続けています。</p>
        <p>当サイトは、これまでの研究成果や、日々の気付き（メモ）を整理し、後から振り返りやすい形で保存するための個人的なプラットフォームです。</p>
      </section>
      <section>
        <h2>研究テーマ</h2>
        <ul>
          <li class="mb-2"><strong>アルゴリズムの最適化</strong>: 既存の処理をより高速かつ省メモリで実行するためのアプローチの研究。</li>
          <li class="mb-2"><strong>データ構造の応用</strong>: 大規模データに対する効率的な検索・更新を実現するためのデータ構造の設計。</li>
          <li class="mb-2"><strong>ヒューマンコンピュータインタラクション (HCI)</strong>: 複雑な情報を直感的に理解するためのUI/UXの改善に関する考察。</li>
        </ul>
      </section>`
  },
  'research.html': {
    title: 'Research',
    content: `
      <div class="page-header mb-4">
        <h1 id="page-title">研究 / Research</h1>
        <p>これまでの研究成果や考察のアーカイブ</p>
      </div>
      <div class="card-grid" id="card-container">
        <article class="card" data-tag="Algorithm">
          <span class="card-tag">Algorithm</span>
          <h3>グラフ探索アルゴリズムの比較</h3>
          <p>Dijkstra法とA*探索における、ヒューリスティック関数の影響度と大規模グラフでの実行時間の差異について検証しました。</p>
          <div class="card-footer">
            <time datetime="2026-04-15">2026.04.15</time>
            <a href="research-article-1.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Data Science">
          <span class="card-tag">Data Science</span>
          <h3>時系列データの異常検知手法</h3>
          <p>自己回帰モデルを用いた基本的なアプローチと、最近の深層学習ベースのモデルの精度比較を行いました。</p>
          <div class="card-footer">
            <time datetime="2026-03-22">2026.03.22</time>
            <a href="research-article-2.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="HCI">
          <span class="card-tag">HCI</span>
          <h3>認知負荷を低減するUI設計</h3>
          <p>情報量が多い画面において、ユーザーの視線移動と認知負荷を最小化するためのレイアウト戦略に関する考察です。</p>
          <div class="card-footer">
            <time datetime="2026-02-10">2026.02.10</time>
            <a href="research-article-3.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Systems">
          <span class="card-tag">Systems</span>
          <h3>分散処理フレームワークの評価</h3>
          <p>複数のノードを跨ぐデータパイプライン構築時の、レイテンシとスループットのトレードオフに関する実験結果です。</p>
          <div class="card-footer">
            <time datetime="2026-01-05">2026.01.05</time>
            <a href="research-article-4.html" style="font-weight:600;">続きを読む &rarr;</a>
          </div>
        </article>
      </div>
      <div id="no-cards-msg" style="display:none; margin-top:2rem; color:#666;">該当する記事が見つかりません。</div>`
  },
  'memo.html': {
    title: 'Memo',
    content: `
      <div class="page-header mb-4">
        <h1 id="page-title">メモ / Memo</h1>
        <p>日々の技術的な気づきや備忘録</p>
      </div>
      <div class="card-grid" id="card-container">
        <article class="card" data-tag="Setup">
          <span class="card-tag memo">Setup</span>
          <h3>WSL2でのDocker環境構築</h3>
          <p>Windows環境においてWSL2バックエンドを利用したDocker Desktopのセットアップ手順と、はまりやすいポイントのまとめ。</p>
          <div class="card-footer">
            <time datetime="2026-04-20">2026.04.20</time>
            <a href="memo-article-1.html" style="font-weight:600;">詳細を見る &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="CSS">
          <span class="card-tag memo">CSS</span>
          <h3>CSS Gridの便利なスニペット</h3>
          <p>カードレイアウトや複雑なグリッドシステムを構築する際に、よく使うCSS Gridの設定例を数パターン記録しました。</p>
          <div class="card-footer">
            <time datetime="2026-04-12">2026.04.12</time>
            <a href="memo-article-2.html" style="font-weight:600;">詳細を見る &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Git">
          <span class="card-tag memo">Git</span>
          <h3>Git rebaseのコンフリクト解消</h3>
          <p>複数人開発でrebaseを行った際に発生するコンフリクトの効率的な解消手順と、注意すべき点について。</p>
          <div class="card-footer">
            <time datetime="2026-03-30">2026.03.30</time>
            <a href="memo-article-3.html" style="font-weight:600;">詳細を見る &rarr;</a>
          </div>
        </article>
        <article class="card" data-tag="Tool">
          <span class="card-tag memo">Tool</span>
          <h3>おすすめのターミナルツール</h3>
          <p>CLI作業の生産性を高めるための、モダンなターミナルエミュレータと関連ツールの紹介。</p>
          <div class="card-footer">
            <time datetime="2026-03-15">2026.03.15</time>
            <a href="memo-article-4.html" style="font-weight:600;">詳細を見る &rarr;</a>
          </div>
        </article>
      </div>
      <div id="no-cards-msg" style="display:none; margin-top:2rem; color:#666;">該当する記事が見つかりません。</div>`
  },
  'links.html': {
    title: 'Link',
    content: `
      <div class="page-header mb-4">
        <h1>リンク / Link</h1>
        <p>外部リソースや関連サイトへのリンク集</p>
      </div>
      <div class="alert-construction">
        <h3>🚧 Under Construction</h3>
        <p>現在このページは準備中です。関連サイトや役立つリソースのリストを後日追加する予定です。</p>
        <div class="mt-4">
          <a href="index.html" class="btn btn-primary">ホームに戻る</a>
        </div>
      </div>`
  },
  'research-article-1.html': {
    title: 'グラフ探索アルゴリズムの比較',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag">Algorithm</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">グラフ探索アルゴリズムの比較</h1>
        <p>2026.04.15</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>Dijkstra法とA*探索における、ヒューリスティック関数の影響度と大規模グラフでの実行時間の差異について検証しました。</p>
        <h2>はじめに</h2>
        <p>経路探索アルゴリズムは、ナビゲーションシステムからゲームAIまで幅広く応用されています。本記事では基礎的なアルゴリズムの実装とパフォーマンスを比較します。</p>
        <h2>実装のポイント</h2>
        <p>優先度付きキュー(Priority Queue)の最適化が、特に頂点数が多いグラフでのボトルネックを解消する鍵となります。</p>
        <div class="mt-4">
          <a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a>
        </div>
      </div>`
  },
  'research-article-2.html': {
    title: '時系列データの異常検知手法',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag">Data Science</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">時系列データの異常検知手法</h1>
        <p>2026.03.22</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>自己回帰モデルを用いた基本的なアプローチと、最近の深層学習ベースのモデルの精度比較を行いました。</p>
        <h2>異常検知の課題</h2>
        <p>周期性とトレンドを持つデータに対して、どのように閾値を動的に設定するかが重要です。</p>
        <div class="mt-4">
          <a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a>
        </div>
      </div>`
  },
  'research-article-3.html': {
    title: '認知負荷を低減するUI設計',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag">HCI</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">認知負荷を低減するUI設計</h1>
        <p>2026.02.10</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>情報量が多い画面において、ユーザーの視線移動と認知負荷を最小化するためのレイアウト戦略に関する考察です。</p>
        <h2>F型パターンの活用</h2>
        <p>視線がどのように画面上を移動するかを分析し、それに合わせた情報の配置が求められます。</p>
        <div class="mt-4">
          <a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a>
        </div>
      </div>`
  },
  'research-article-4.html': {
    title: '分散処理フレームワークの評価',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag">Systems</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">分散処理フレームワークの評価</h1>
        <p>2026.01.05</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>複数のノードを跨ぐデータパイプライン構築時の、レイテンシとスループットのトレードオフに関する実験結果です。</p>
        <h2>システム構成</h2>
        <p>本実験では3台のワーカーノードを使用し、バッチサイズの違いによるスループットの変化を測定しました。</p>
        <div class="mt-4">
          <a href="research.html" class="btn btn-outline">&larr; 研究一覧に戻る</a>
        </div>
      </div>`
  },
  'memo-article-1.html': {
    title: 'WSL2でのDocker環境構築',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag memo">Setup</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">WSL2でのDocker環境構築</h1>
        <p>2026.04.20</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>Windows環境においてWSL2バックエンドを利用したDocker Desktopのセットアップ手順と、はまりやすいポイントのまとめ。</p>
        <h2>手順概要</h2>
        <p>まずWSL2を有効化し、Ubuntuディストリビューションをインストールします。その後Docker Desktopを導入します。</p>
        <div class="mt-4">
          <a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a>
        </div>
      </div>`
  },
  'memo-article-2.html': {
    title: 'CSS Gridの便利なスニペット',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag memo">CSS</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">CSS Gridの便利なスニペット</h1>
        <p>2026.04.12</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>カードレイアウトや複雑なグリッドシステムを構築する際に、よく使うCSS Gridの設定例を数パターン記録しました。</p>
        <h2>auto-fit と minmax</h2>
        <p>レスポンシブなカードグリッドを作る上で、メディアクエリを減らせる強力な記述です。</p>
        <div class="mt-4">
          <a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a>
        </div>
      </div>`
  },
  'memo-article-3.html': {
    title: 'Git rebaseのコンフリクト解消',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag memo">Git</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">Git rebaseのコンフリクト解消</h1>
        <p>2026.03.30</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>複数人開発でrebaseを行った際に発生するコンフリクトの効率的な解消手順と、注意すべき点について。</p>
        <h2>基本コマンド</h2>
        <p>コンフリクト発生時は、エディタで差分を確認し、<code>git add</code> の後 <code>git rebase --continue</code> を実行します。</p>
        <div class="mt-4">
          <a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a>
        </div>
      </div>`
  },
  'memo-article-4.html': {
    title: 'おすすめのターミナルツール',
    content: `
      <div class="page-header mb-4">
        <span class="card-tag memo">Tool</span>
        <h1 style="margin-top:0.5rem; border:none; padding:0;">おすすめのターミナルツール</h1>
        <p>2026.03.15</p>
      </div>
      <div class="article-content" style="max-width: 800px;">
        <p>CLI作業の生産性を高めるための、モダンなターミナルエミュレータと関連ツールの紹介。</p>
        <h2>ツールリスト</h2>
        <p>個人的には補完機能が強力なシェルや、高速な検索ツール（ripgrep等）を組み合わせています。</p>
        <div class="mt-4">
          <a href="memo.html" class="btn btn-outline">&larr; メモ一覧に戻る</a>
        </div>
      </div>`
  }
};

for (const [filename, data] of Object.entries(pages)) {
  const fullContent = head(data.title) + headerAndSidebar + data.content + foot;
  fs.writeFileSync(path.join(__dirname, filename), fullContent);
}
console.log('Generated all HTML files');
