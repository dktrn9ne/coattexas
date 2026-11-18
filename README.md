# Precision Coatings of Texas

Client website and AI project visualizer for Precision Coatings of Texas, a coatings contractor serving Austin and Central Texas. The live site is [coattexas.com](https://coattexas.com).

## What's in the repo

- A public marketing site: home, services (garages, patios, tile, tubs, vanities, countertops, cabinets), colors and finishes, gallery, process, about, service areas, FAQ, reviews, and contact.
- An [AI project visualizer](visualizer.html) that turns a job-site photo into a finished-surface preview.
- `build_site.py`, a Python static site generator that writes the HTML pages from shared navigation, footer, and chat-widget partials. The checked-in `.html` files are the generated output.
- `api/generate-preview.js`, a serverless function that creates the preview image.

## How the visualizer works

1. In the browser, the visitor uploads a photo and chooses a surface, finish, and topcoat.
2. `assets/js/visualizer.js` resizes the photo and `POST`s it to `/api/generate-preview`.
3. The server-side function builds a preview from that photo and those choices, then returns an image the visitor can download.

Preview images are for planning only. Final color, texture, and coverage are confirmed during an on-site estimate.

The image-generation provider is configured server-side through the environment. The preview function reads `OPENAI_API_KEY` from the server environment and does not expose it to the browser. Do not commit a value for this variable.

## Stack

- Python 3 (site generator; standard library only)
- Static HTML, CSS, and JavaScript
- A Node.js serverless function in `api/` (Vercel-style route)

## Run locally

Regenerate the HTML pages from the shared partials:

```bash
python3 build_site.py
```

Serve the repository root as a static site, for example:

```bash
python3 -m http.server 8000
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

The marketing pages work with a static file server. Generating a visualizer preview requires a deploy that can run `/api/generate-preview`, with `OPENAI_API_KEY` set in the server environment.
