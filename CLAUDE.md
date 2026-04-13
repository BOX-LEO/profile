# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Static personal webpage (plain HTML/CSS, no build step) intended for GitHub Pages deployment.

## Commands

- **Preview locally:** `python3 -m http.server 8000` then open `http://localhost:8000`
- **Deploy:** push to GitHub; Pages serves from `main` branch root. For a root URL, repo must be named `<username>.github.io`.

There is no build, lint, test, or package manager. Edit files and refresh the browser.

## Architecture

Three files, flat layout:

- `index.html` — single-page layout with a two-column CSS grid: left `.sidebar` (photo, name, title, location, icon links) and right `.content` (About, Research Interests, Education, Publications, Projects). Placeholder values use the `YOUR_` prefix (e.g. `YOUR_USERNAME`) so they are easy to grep and replace.
- `style.css` — CSS variables for theme (`--fg`, `--accent`, `--border`, etc.) at `:root`. The `.container` grid collapses to a single column under 768px. Icon links are a 3×2 grid of circular buttons.
- Font Awesome 6 is loaded via CDN in `<head>` for icons; the Hugging Face icon is a literal 🤗 emoji because Font Awesome has no HF glyph.

When adding publications or projects, reuse the `.pub-list > li` card pattern already in `index.html` — do not introduce new component classes for one-off entries.
