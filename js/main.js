document.addEventListener('DOMContentLoaded', () => {
  // 1. Render Sidebar dynamically
  renderSidebar();

  // 2. Initial Translations
  applyTranslations();

  // 3. Language Switcher Logic (delegated since it's dynamically rendered)
  document.body.addEventListener('click', (e) => {
    if (e.target.id === 'lang-ja') {
      localStorage.setItem('site_lang', 'ja');
      window.location.reload(); // Reload to refresh sidebar and content cleanly
    } else if (e.target.id === 'lang-en') {
      localStorage.setItem('site_lang', 'en');
      window.location.reload();
    }
  });

  // 4. Mobile Menu Toggle
  document.body.addEventListener('click', (e) => {
    const menuBtn = e.target.closest('#mobile-menu-btn');
    if (menuBtn) {
      const sidebar = document.getElementById('sidebar');
      if (sidebar) {
        sidebar.classList.toggle('active');
      }
    }
  });

  // Close sidebar on mobile when clicking outside
  document.addEventListener('click', (e) => {
    const sidebar = document.getElementById('sidebar');
    const menuBtn = document.getElementById('mobile-menu-btn');
    
    if (window.innerWidth <= 992 && sidebar && sidebar.classList.contains('active')) {
      if (!sidebar.contains(e.target) && (!menuBtn || !menuBtn.contains(e.target))) {
        sidebar.classList.remove('active');
      }
    }
  });
});
