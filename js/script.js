document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.getElementById('hamburger');
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');

  // 1. Mobile Menu Toggle
  if (hamburger && sidebar && overlay) {
    const toggleMenu = () => {
      sidebar.classList.toggle('open');
      if (sidebar.classList.contains('open')) {
        overlay.classList.add('show');
        document.body.style.overflow = 'hidden';
      } else {
        overlay.classList.remove('show');
        document.body.style.overflow = '';
      }
    };
    hamburger.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', toggleMenu);
  }

  // Helper: open a submenu
  const openSubMenu = (targetMenu) => {
    if (!targetMenu) return;
    targetMenu.classList.add('open');
    const toggleBtn = document.querySelector(`[data-target="${targetMenu.id}"]`);
    if (toggleBtn) {
      const icon = toggleBtn.querySelector('.toggle-icon');
      if (icon) icon.style.transform = 'rotate(180deg)';
    }
  };

  // Helper: toggle a submenu
  const toggleSubMenu = (targetMenu) => {
    if (!targetMenu) return;
    targetMenu.classList.toggle('open');
    const isOpen = targetMenu.classList.contains('open');
    const toggleBtn = document.querySelector(`[data-target="${targetMenu.id}"]`);
    if (toggleBtn) {
      const icon = toggleBtn.querySelector('.toggle-icon');
      if (icon) icon.style.transform = isOpen ? 'rotate(180deg)' : 'rotate(0deg)';
    }
  };

  // 2. Accordion: clicking the toggle-icon area toggles submenu,
  //    clicking the parent link text navigates to the page.
  document.querySelectorAll('.nav-parent').forEach(parentLink => {
    const targetId = parentLink.getAttribute('data-target');
    const icon = parentLink.querySelector('.toggle-icon');

    if (icon) {
      icon.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const targetMenu = document.getElementById(targetId);
        toggleSubMenu(targetMenu);
      });
    }

    // The link itself navigates (default behavior), but also toggle on click for convenience
    parentLink.addEventListener('click', (e) => {
      // Only toggle if clicking on the text portion (not the icon, handled above)
      if (!e.target.classList.contains('toggle-icon')) {
        const targetMenu = document.getElementById(targetId);
        if (targetMenu) {
          openSubMenu(targetMenu);
        }
        // Allow default navigation
      }
    });
  });

  // 3. Active Link Detection
  let currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const currentSearch = window.location.search;

  const openParentMenu = (link) => {
    const parentMenu = link.closest('.sub-menu');
    if (parentMenu) {
      openSubMenu(parentMenu);
    }
  };

  const navLinks = document.querySelectorAll('.nav-link:not(.nav-parent)');
  const parentNavLinks = document.querySelectorAll('.nav-parent');

  // Match non-parent links (exact path + query)
  let matched = false;
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (decodeURIComponent(href) === decodeURIComponent(currentPath + currentSearch)) {
      link.classList.add('active');
      matched = true;
      openParentMenu(link);
    }
  });

  if (!matched) {
    navLinks.forEach(link => {
      if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
        openParentMenu(link);
      }
    });
  }

  // Match parent links
  parentNavLinks.forEach(link => {
    const href = link.getAttribute('href').split('?')[0];
    if (href === currentPath) {
      link.classList.add('active');
      const targetId = link.getAttribute('data-target');
      const targetMenu = document.getElementById(targetId);
      openSubMenu(targetMenu);
    }
  });

  // Highlight parent for article pages
  if (currentPath.startsWith('research-article')) {
    parentNavLinks.forEach(link => {
      if (link.getAttribute('href') === 'research.html') {
        link.classList.add('active');
        openSubMenu(document.getElementById(link.getAttribute('data-target')));
      }
    });
  } else if (currentPath.startsWith('memo-article')) {
    parentNavLinks.forEach(link => {
      if (link.getAttribute('href') === 'memo.html') {
        link.classList.add('active');
        openSubMenu(document.getElementById(link.getAttribute('data-target')));
      }
    });
  }

  // 4. Tag Filtering Logic
  const urlParams = new URLSearchParams(window.location.search);
  const currentTag = urlParams.get('tag');
  if (currentTag) {
    const cards = document.querySelectorAll('.card');
    let visibleCount = 0;
    cards.forEach(card => {
      const tags = (card.getAttribute('data-tag') || '').split(',').map(t => t.trim());
      if (tags.includes(currentTag)) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });
    const pageTitle = document.getElementById('page-title');
    if (pageTitle) {
      pageTitle.innerHTML += ` <span style="font-size:1.1rem;color:#666;font-weight:normal;margin-left:0.5rem;">/ ${currentTag}</span>`;
    }
    const noMsg = document.getElementById('no-cards-msg');
    if (noMsg) noMsg.style.display = visibleCount === 0 ? 'block' : 'none';
  }
});
