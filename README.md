# Eunji Woo · Academic website

Personal academic site using the existing **Academic Pages / Jekyll** template.
Production configuration: `https://ooungy.github.io`, repository
`ooungy/ooungy.github.io`, empty `baseurl`. No framework migration.

**View the result on this review branch:** [Desktop screenshot](preview/homepage.png)
· [Mobile screenshot](preview/mobile.png). Download `preview/eunji-woo-preview.zip`,
extract it, and double-click `Eunji-Woo-Preview.html` for a working self-contained
preview. No Ruby, Python, or server is needed to view that file.

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
| Engagement | `_data/engagement/*.yml`; section labels in `_data/engagement_sections.yml` |
| Teaching and supervision | `_teaching/`; assistance in `_data/teaching.yml` |
| CV summary and existing public PDF | `_pages/cv.md`, `files/eunji-woo-cv.pdf` |
| Visual styling | `_sass/academic.scss` (layered over Academic Pages) |

Copy an existing publication and change its front matter: `title`, `authors`,
`venue`, `year`, `sort_year`, `category`, and optional `paper_url`, `details`,
`status`. Category keys are in `_data/publication_categories.yml`. Set
`selected: true` to feature it on the homepage. Use `status: Forthcoming` or
`Under contract` without inventing a year. For undated forthcoming works,
`sort_year: 9999` places them first. Use explicit accepted/forthcoming labels;
never create a public record for an under-review manuscript. Keep private
source documents and annotations outside the checkout.

Project URLs use `/projects/<filename>/` while preserving `_portfolio/`.
Keep filenames stable to preserve existing URLs. Use `order` for sorting and
`selected: true` for homepage selection (keep three or four selections).
Give each project one `theme` from `_data/project_themes.yml`; optional `tags`
contain other theme keys. The archive lists each project only once.

To add a project, create `_portfolio/my-project.md` with front matter such as:

```yaml
---
title: Project title
period: "May–Aug 2027" # Use only documented dates and their actual precision.
theme: local-communities
tags: [participatory-technology]
summary: A concise description of documented work.
order: 23
selected: false
# Add role and organization only when documented and cleared for public use.
---
```

The three theme keys are `local-communities`, `participatory-technology`, and
`entrepreneurship`. Write the project narrative below the front matter. A brief
paragraph is enough when evidence is limited. Images are optional: pages look
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

To add a future talk or advisory role, append a record to
`_data/engagement/talks.yml` or `advisory.yml`. Academic service uses `service.yml`;
exhibitions and selected media use `exhibitions_media.yml` with
`kind: exhibition` or `kind: media`.

```yaml
- id: unique-activity-name
  title: Activity title
  period: "May 2027"
  sort_date: "2027-05"
  role: Invited speaker
  organization: Institution or event host
```

Use a unique `id`, exact documented role, and a quoted `sort_date` at the known
precision (`2027`, `2027-05`, or `2027-05-12`). Lists sort newest first. Optional
fields include `location`, `link`, and `link_verified`. A link is rendered only
when `link_verified: true`; verify both the destination and its relevance first.
Do not add confidential client names, internal seminars without disclosure
clearance, private source annotations, source PDFs, contact details, or amounts.

## Source and review notes

v1.3 expands content architecture without changing the v1.1 editorial design.
The site has 26 publication records, 22 projects, 52 Engagement records, and
teaching/supervision history. The research description remains on the homepage;
Engagement replaces the former Research navigation item. See
[coverage and verification notes](preview/COVERAGE-v1.3.md) for the item-level
mapping, omitted material, anonymized clients, and link limitations.
Accepted and forthcoming work is labeled explicitly. Under-review
manuscripts are omitted entirely, including their metadata and titles.

The existing public CV download is unchanged and labeled as an earlier version.
It does not reflect the current PolyU appointment. Replace it only with a
separately approved public-facing CV. Do not commit private source PDFs,
personal phone numbers, dates of birth, grant amounts, or private annotations.
The refreshed offline preview does not embed or redistribute the old PDF.

Korean-only publication titles have been translated into English; author names
without confirmed romanizations retain their Korean spelling. SD5138 retains
the stated term “2026 Semester 2” without inferring delivery status or academic
year. No project photographs were added.

## GitHub Pages, after review

v1.3 work is on `feat/projects-engagement-v1.3`; the review branch includes screenshots
and an offline preview. No website is deployed. Review and merge only when ready. Live Pages settings could
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
