# Lanius Films — Independent Film & Creative Production

Static studio portfolio for GitHub Pages. No installation required. A small browser script opens the embedded YouTube player; direct video links remain usable without JavaScript.

## Update and build

Edit `content.json`, then run `python3 build.py`. Commit the source, updated assets and **all generated HTML pages** together. Pages publishes the `main` branch, repository root.

The generator creates `index.html` and a page for every `projects[].id`. Existing project IDs and paths are preserved. Do not edit generated HTML independently; a rebuild will replace it.

- `site`: studio positioning, hero, About, capabilities and contact copy.
- `projects`: narrative films, branded concepts and cinematic worlds. `home_group` controls their homepage placement.
- `projects[].videos`: published films. Keep the portrait films in the order shown under **Most recent** on the official `@laniusfilms` YouTube channel. A landscape introduction/trailer is presented separately, without implying it is a recent release.
- `featured_count`: number of portrait films shown before the expandable archive. Every earlier film remains available.
- `featured_films`: curated branded concepts on the homepage, explicitly identified as independent spec work.
- `more_work`: four selected releases on the homepage: the three recent character/series releases, followed by SEREIN as a selected fragrance concept. Keep chronological order within the individual project collections.
- `more_work_archive`: previous homepage selections, preserved in a clearly labelled archive.
- `image`: existing JPG artwork basename under `assets`; `cover_url` supports an approved local image or external poster.
- `artwork_sources`: original URLs for the approved artwork copied into `assets`, retained for provenance.
- `thumbnail`: local approved designed artwork, including the original NO PLANS editorial poster at `assets/no-plans-poster.png`. Do not replace designed posters with automatic video frames.
- `email`, `youtube`, `archive`, `reel_url`, `reel_thumbnail`: studio contacts, earlier work and the 2026 showreel.

## Editorial rules

THE WISH is the first narrative film, followed by The Passenger. Campaigns are self-initiated concepts, with no invented clients or commercial credits. Vex Darkness, Alura Thorne and Valeria Satie retain their own pages and earlier films. Previously published links and original galleries are preserved. Use the official Lanius Films channel for publication order and approved portfolio artwork for posters.

## Local preview

Run `python3 -m http.server 8765 --bind 127.0.0.1` from this directory, then open `http://127.0.0.1:8765/`. Check every generated page at desktop and mobile widths before publishing.

## Playback and project stills

Watch actions and video covers open a YouTube privacy-enhanced iframe in an accessible dialog. The player is created on demand and removed on close, with a direct YouTube fallback. No video files are hosted in this repository.

Each published film has a `description` summarised from its official channel description. `projects[].gallery` accepts the original artwork names and objects containing `src`, `alt`, `caption`, `width`, and `height`. The additional project stills are web-sized copies of the original project SF assets; originals remain untouched. Preserve the approved posters and publication order.
