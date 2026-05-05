const siteData = {
  research: [
    {
      id: "research-1",
      icon: `<svg viewBox="0 0 24 24"><path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M12,10.5A1.5,1.5 0 0,1 13.5,12A1.5,1.5 0 0,1 12,13.5A1.5,1.5 0 0,1 10.5,12A1.5,1.5 0 0,1 12,10.5M7.5,10.5A1.5,1.5 0 0,1 9,12A1.5,1.5 0 0,1 7.5,13.5A1.5,1.5 0 0,1 6,12A1.5,1.5 0 0,1 7.5,10.5M16.5,10.5A1.5,1.5 0 0,1 18,12A1.5,1.5 0 0,1 16.5,13.5A1.5,1.5 0 0,1 15,12A1.5,1.5 0 0,1 16.5,10.5Z"/></svg>`,
      title: { ja: "研究記事 1", en: "Research Article 1" },
      summary: { ja: "準結晶の合成", en: "XXXX" }
    },
    {
      id: "research-2",
      icon: `<svg viewBox="0 0 24 24"><path d="M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.5,21.82C12.18,22 11.82,22 11.5,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.5,2.18C11.82,2 12.18,2 12.5,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L5,8.09L12,12.04L19,8.09L12,4.15M5,15.91L11,19.29V12.58L5,9.21V15.91M19,15.91V9.21L13,12.58V19.29L19,15.91Z"/></svg>`,
      title: { ja: "研究記事 2", en: "Research Article 2" },
      summary: { ja: "混合原子価化合物の合成", en: "XXXX." }
    },
    {
      id: "research-3",
      icon: `<svg viewBox="0 0 24 24"><path d="M12 2A10 10 0 1 0 22 12A10 10 0 0 0 12 2M12 20A8 8 0 1 1 20 12A8 8 0 0 1 12 20M15.5 11A2.5 2.5 0 1 0 13 8.5A2.5 2.5 0 0 0 15.5 11M15.5 8A.5.5 0 1 1 15 8.5A.5.5 0 0 1 15.5 8M8.5 11A2.5 2.5 0 1 0 11 13.5A2.5 2.5 0 0 0 8.5 11M8.5 14A.5.5 0 1 1 9 13.5A.5.5 0 0 1 8.5 14M12 11A1 1 0 1 0 13 12A1 1 0 0 0 12 11Z"/></svg>`,
      title: { ja: "研究記事 3", en: "Research Article 3" },
      summary: { ja: "XXXX", en: "XXXX." }
    },
    {
      id: "research-4",
      icon: `<svg viewBox="0 0 24 24"><path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20M16,11V13H8V11H16M14,15V17H8V15H14Z"/></svg>`,
      title: { ja: "研究記事 4", en: "Research Article 4" },
      summary: { ja: "XXXX", en: "XXXX." }
    }
  ],
  memo: [
    {
      id: "memo-1",
      icon: `<svg viewBox="0 0 24 24"><path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"/></svg>`,
      title: { ja: "メモ記事 1", en: "Memo Article 1" },
      summary: { ja: "情報科学への期待", en: "XXXX." }
    },
    {
      id: "memo-2",
      icon: `<svg viewBox="0 0 24 24"><path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"/></svg>`,
      title: { ja: "メモ記事 2", en: "Memo Article 2" },
      summary: { ja: "実験装置の自作", en: "XXXX." }
    },
    {
      id: "memo-3",
      icon: `<svg viewBox="0 0 24 24"><path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"/></svg>`,
      title: { ja: "メモ記事 3", en: "Memo Article 3" },
      summary: { ja: "基礎データの測定", en: "XXXX." }
    },
    {
      id: "memo-4",
      icon: `<svg viewBox="0 0 24 24"><path d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"/></svg>`,
      title: { ja: "メモ記事 4", en: "Memo Article 4" },
      summary: { ja: "XXXX", en: "XXXXd." }
    }
  ],
  i18n: {
    "nav-home": { ja: "ホーム", en: "Home" },
    "nav-about": { ja: "私たち", en: "About Us" },
    "nav-research": { ja: "研究", en: "Research" },
    "nav-memo": { ja: "メモ", en: "Memo" },
    "nav-links": { ja: "リンク", en: "Links" },
    
    "hero-catch": { ja: "実験ノートのようなもの", en: "Like a Laboratory Notebook" },
    "hero-sub": { ja: "日々の研究の記録", en: "My Research Logs" },
    
    "about-title": { ja: "私たち / About Us", en: "About Us" },
    "research-title": { ja: "研究 / Research", en: "Research" },
    "memo-title": { ja: "メモ / Memo", en: "Memo" },
    "links-title": { ja: "リンク / Links", en: "Links" },
    
    "read-more": { ja: "詳細を読む", en: "Read More" },
    "back-link": { ja: "← 戻る", en: "← Back" }
  }
};
