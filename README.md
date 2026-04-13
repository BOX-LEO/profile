# Personal Webpage

Plain HTML/CSS personal site. Hosted on GitHub Pages.

## Editing

- `index.html` — all content (bio, education, publications, projects, links)
- `style.css` — styling
- `photo.jpg` — replace with your own headshot (square, ~400×400px works well)
- `cv.pdf` — optional CV file

Search for `YOUR_` placeholders in `index.html` and replace them.

## Refresh publications from Google Scholar

```sh
pip install scholarly
python scripts/fetch_publications.py
```

This writes `publications.json`, which `index.html` reads at page load. Re-run whenever you want the site to reflect new Scholar entries.

## Preview locally

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploy to GitHub Pages

1. Push this repo to GitHub.
2. Settings → Pages → Source: `main` branch, `/ (root)`.
3. Site will be live at `https://<username>.github.io/<repo>/` (or `https://<username>.github.io/` if repo is named `<username>.github.io`).
