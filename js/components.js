function getLang() {
  return localStorage.getItem('site_lang') || 'ja';
}

function renderSidebar() {
  const lang = getLang();
  
  // Get current page to set active state
  const currentPath = window.location.pathname;
  const page = currentPath.split('/').pop() || 'index.html';
  
  // Check URL params for article details
  const searchParams = new URLSearchParams(window.location.search);
  const type = searchParams.get('type');

  const sidebarHTML = `
    <!-- Mobile Header -->
    <div class="mobile-header">
      <div class="sidebar-logo">
        <a href="index.html">
          <svg class="logo-icon" viewBox="0 0 24 24"><path d="M12,2L1,21H23M12,6L19.53,19H4.47M11,10V14H13V10M11,16V18H13V16"/></svg>
          <span style="font-family: 'Segoe UI', sans-serif;">DIY Chem.</span>
        </a>
      </div>
      <button class="menu-btn" id="mobile-menu-btn" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>

    <!-- Sidebar Content -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <div class="sidebar-logo">
          <a href="index.html">
            <svg class="logo-icon" viewBox="0 0 24 24"><path d="M12,2L1,21H23M12,6L19.53,19H4.47M11,10V14H13V10M11,16V18H13V16"/></svg>
            <span style="font-family: 'Segoe UI', sans-serif;">DIY Chem.</span>
          </a>
        </div>
      </div>
      
      <nav class="sidebar-nav">
        <ul class="sidebar-menu">
          <li><a href="index.html" class="${page === 'index.html' ? 'active' : ''}" data-i18n="nav-home">${siteData.i18n['nav-home'][lang]}</a></li>
          <li><a href="about.html" class="${page === 'about.html' ? 'active' : ''}" data-i18n="nav-about">${siteData.i18n['nav-about'][lang]}</a></li>
          <li><a href="research.html" class="${page === 'research.html' || (page === 'article.html' && type === 'research') ? 'active' : ''}" data-i18n="nav-research">${siteData.i18n['nav-research'][lang]}</a></li>
          <li><a href="memo.html" class="${page === 'memo.html' || (page === 'article.html' && type === 'memo') ? 'active' : ''}" data-i18n="nav-memo">${siteData.i18n['nav-memo'][lang]}</a></li>
          <li><a href="links.html" class="${page === 'links.html' ? 'active' : ''}" data-i18n="nav-links">${siteData.i18n['nav-links'][lang]}</a></li>
        </ul>
      </nav>

      <div class="sidebar-footer">
        <div class="lang-switch">
          <span id="lang-ja" class="${lang === 'ja' ? 'active' : ''}">JP</span>
          <span>/</span>
          <span id="lang-en" class="${lang === 'en' ? 'active' : ''}">EN</span>
        </div>
      </div>
    </aside>
  `;
  
  const sidebarContainer = document.getElementById('sidebar-container');
  if (sidebarContainer) {
    sidebarContainer.innerHTML = sidebarHTML;
  }
}

function createCardHTML(item, type) {
  const lang = getLang();
  const title = item.title[lang] || item.title.ja;
  const summary = item.summary[lang] || item.summary.ja;
  const readMoreText = siteData.i18n["read-more"][lang];
  
  return `
    <article class="card fade-in">
      <div class="card-icon">
        ${item.icon}
      </div>
      <h3 class="card-title">${title}</h3>
      <p class="card-text">${summary}</p>
      <a href="article.html?type=${type}&id=${item.id}" class="card-link" data-i18n="read-more">${readMoreText}</a>
    </article>
  `;
}

function renderResearch() {
  const container = document.getElementById('research-grid');
  if (!container) return;
  container.innerHTML = siteData.research.map(item => createCardHTML(item, 'research')).join('');
}

function renderMemo() {
  const container = document.getElementById('memo-grid');
  if (!container) return;
  container.innerHTML = siteData.memo.map(item => createCardHTML(item, 'memo')).join('');
}

function applyTranslations() {
  const lang = getLang();
  document.documentElement.lang = lang;
  
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (siteData.i18n[key] && siteData.i18n[key][lang]) {
      el.innerHTML = siteData.i18n[key][lang];
    }
  });

  renderResearch();
  renderMemo();
  setupIntersectionObserver();
}

function setupIntersectionObserver() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

  document.querySelectorAll('.fade-in').forEach(el => {
    observer.observe(el);
  });
}
