# Zhangchi Chen / 陈张弛 — Personal Homepage

A minimal academic homepage with Chinese/English language switching.

## File Structure

```
├── index.html      # Main page (bilingual content)
├── style.css       # Stylesheet
├── script.js       # Language switcher + MathJax
├── img/
│   └── photo.jpg   # Personal photo (replace with your own)
├── cv/
│   └── cv.pdf      # Curriculum vitae (replace with your own)
└── README.md
```

## Quick Start

1. Replace `img/photo.jpg` with your own photo.
2. Replace `cv/cv.pdf` with your CV.
3. Edit `index.html` to update publications, talks, teaching info, etc.
4. Push to GitHub as a repository named `zhangchi-chen.github.io`.

## Deployment

This site is designed to be deployed via GitHub Pages. Simply:

```bash
git init
git add .
git commit -m "Initial homepage"
git remote add origin https://github.com/zhangchi-chen/zhangchi-chen.github.io.git
git push -u origin main
```

Then enable GitHub Pages in the repository settings (Settings → Pages → Source: main branch).

## Customization

- **Add a paper**: Add a new `<li>` entry in the publications section (both `lang-cn` and `lang-en` blocks).
- **Add talks**: Replace the placeholder in the Talks section.
- **Add teaching info**: Replace the placeholder in the Teaching section.
- **Change style**: Edit `style.css`.
