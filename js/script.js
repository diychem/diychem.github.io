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

  // 2. Accordion for Submenus
  const accordionToggles = document.querySelectorAll('.nav-link[data-toggle="collapse"]');
  accordionToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = toggle.getAttribute('data-target');
      const targetMenu = document.getElementById(targetId);
      const icon = toggle.querySelector('.toggle-icon');
      
      if (targetMenu) {
        targetMenu.classList.toggle('open');
        if (targetMenu.classList.contains('open')) {
          if (icon) icon.style.transform = 'rotate(180deg)';
        } else {
          if (icon) icon.style.transform = 'rotate(0deg)';
        }
      }
    });
  });

  // 3. Active Link Detection
  let currentPath = window.location.pathname.split('/').pop();
  if (!currentPath || currentPath === '') {
    currentPath = 'index.html';
  }
  const currentSearch = window.location.search;
  const fullPath = currentPath + currentSearch;
  
  const navLinks = document.querySelectorAll('.nav-link:not([data-toggle="collapse"])');
  let matched = false;

  const openParentMenu = (link) => {
    const parentMenu = link.closest('.sub-menu');
    if (parentMenu) {
      parentMenu.classList.add('open');
      const parentId = parentMenu.id;
      const toggleBtn = document.querySelector(`[data-target="${parentId}"]`);
      if (toggleBtn) {
        const icon = toggleBtn.querySelector('.toggle-icon');
        if (icon) icon.style.transform = 'rotate(180deg)';
      }
    }
  };

  // First try to match exact href including query string
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (decodeURIComponent(href) === decodeURIComponent(fullPath)) {
      link.classList.add('active');
      matched = true;
      openParentMenu(link);
    }
  });

  // If no exact match with query, just match the path
  if (!matched) {
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      // If the link has a query parameter but we didn't match, we shouldn't mark it active
      // We only match if the link href is purely the currentPath
      if (href === currentPath) {
        link.classList.add('active');
        openParentMenu(link);
      }
    });
  }

  // Handle article pages highlighting the parent menu item
  if (currentPath.startsWith('research-article')) {
    navLinks.forEach(link => {
      if (link.getAttribute('href') === 'research.html') {
         link.classList.add('active');
         openParentMenu(link);
      }
    });
  } else if (currentPath.startsWith('memo-article')) {
    navLinks.forEach(link => {
      if (link.getAttribute('href') === 'memo.html') {
         link.classList.add('active');
         openParentMenu(link);
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
      if (card.getAttribute('data-tag') === currentTag) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });
    
    const pageTitle = document.getElementById('page-title');
    if (pageTitle) {
      pageTitle.innerHTML += ` <span style="font-size: 1.1rem; color: #666; font-weight: normal; margin-left: 0.5rem;">/ Tag: ${currentTag}</span>`;
    }
    
    const noCardsMsg = document.getElementById('no-cards-msg');
    if (noCardsMsg) {
      noCardsMsg.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }
});
