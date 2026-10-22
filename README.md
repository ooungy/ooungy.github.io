# Eunji Woo · Academic website

Personal academic site using the existing **Academic Pages / Jekyll** template.
Production configuration: `https://ooungy.github.io`, repository
`ooungy/ooungy.github.io`, empty `baseurl`. No framework migration.

## Preview and validate

With Ruby 3.3 and Bundler available:

```bash
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

In the prepared Codex cloud environment, activate the retained installation first:

```bash
export PATH=/workspace/.cloud-setup/ruby/bin:$PATH
export BUNDLE_USER_HOME=/workspace/.cloud-setup/bundler
export BUNDLE_PATH=/workspace/.cloud-setup/gems
export GEM_SPEC_CACHE=/workspace/.cloud-setup/gem-spec-cache
cd /workspace/ooungy.github.io
```

Restart Jekyll after editing `_config.yml`. Validate before review:

```bash
JEKYLL_ENV=production bundle exec jekyll build --safe --strict_front_matter
python3 scripts/check_site.py _site
```

Pull requests run build/link checks and produce a downloadable site artifact.
The workflow never deploys. JavaScript/npm is not needed for the MVP interface.

## Update content with Codex

Ask Codex: “Create a new branch, update my academic website from the attached
source material, preserve Academic Pages, run the build and site checks, and
leave changes for review. Do not invent details or deploy.”

| Content | Edit here |
| --- | --- |
| About, research, contact, selected work | `_pages/about.md` |
| Name, email, canonical URL, repository | `_config.yml` |
| Header navigation | `_data/navigation.yml` |
| Publications | One Markdown file per work in `_publications/` |
| Projects | One Markdown file per project in `_portfolio/` |
| Teaching and supervision | `_teaching/`; assistance in `_data/teaching.yml` |
| CV summary and original PDF | `_pages/cv.md`, `files/eunji-woo-cv.pdf` |
| Visual styling | `_sass/academic.scss` (layered over Academic Pages) |

Copy an existing publication and change its front matter: `title`, `authors`,
`venue`, `year`, `sort_year`, `category`, and optional `paper_url`, `details`,
`status`. Category keys are in `_data/publication_categories.yml`. Set
`selected: true` to feature it on the homepage. Use `status: Forthcoming` or
`Under contract` without inventing a year. For undated forthcoming works,
`sort_year: 9999` places them first. Keep source notes in `source`.

Project URLs use `/projects/<filename>/` while preserving `_portfolio/`.
Use `order` for sorting and `selected: true` for homepage selection. Write the
project narrative below the front matter. Images are optional: pages look
complete without them. Put real, permission-cleared images in
`images/projects/<project>/`, then add:

```yaml
image: /images/projects/my-project/cover.jpg
image_alt: "A meaningful description of the photograph"
image_caption: "Optional caption and credit"
gallery:
  - path: /images/projects/my-project/workshop.jpg
    alt: "Describe what the workshop photograph shows"
    caption: "Optional caption and credit"
```

## Source and review notes

Academic content comes from the supplied **우은지 CV (ENG).pdf**. The downloadable
PDF is the original supplied CV. The site includes 21 publication records,
six selected projects, and the CV's teaching/supervision history; it is not a
complete project or invited-talk archive. No stock portrait or invented project
photographs are used. Personal phone details appear only in the original PDF.

- The CV repeats `10.57698/v19i3.03` for the forthcoming *Digital Creativity*
  article and the 2025 *International Journal of Design* article. The former
  has no DOI link until the author verifies it.
- The CV lists the *Design Works* article as 2023, but its DOI contains 2022.
  The site preserves the CV's year and supplied DOI; confirm before release.
- The resource-exchange article title ends “with focus” in the CV; the site
  retains that wording rather than inventing a missing subtitle.
- Appointment/teaching dates and forthcoming/under-contract status are as
  stated in the supplied CV. Update these when the CV changes.

## GitHub Pages, after review

Work is on `feat/eunji-woo-academic-mvp`; nothing is pushed or deployed by this
implementation. Review and merge only when ready. Live Pages settings could
not be inspected because this environment denied the GitHub Pages API request.
For GitHub's native Jekyll publishing, later verify **Settings → Pages → Deploy
from a branch → master → /(root)** after merging the reviewed work. Do not
enable deployment from the feature branch just to preview it. If the repository
already uses an external deployment process, review that configuration before
changing settings. Build validation here does not publish anything.

The reference `nadiacw.com` could not be fetched under the environment's network
policy. The MVP follows the requested minimal typography, generous whitespace,
and understated color direction independently.

Academic Pages / Minimal Mistakes attribution is retained in the footer and
the existing LICENSE. See upstream Academic Pages for template documentation.
