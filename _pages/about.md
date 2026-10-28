---
layout: academic
home: true
permalink: /
redirect_from:
- /about/
- /about.html
---

<section id="about" class="introduction" aria-labelledby="intro-title">
  <h1 id="intro-title">Eunji Woo</h1>
  <p>I’m a Research Assistant Professor in the School of Design at The Hong Kong Polytechnic University (PolyU), based in Hong Kong since August 2026.</p>
  <p id="research">I study participatory and technology-mediated design: how stakeholders make their resources and values visible, work together, and create value in communities and early-stage ventures. My recent work explores generative AI as a way to surface different perspectives and support collaboration in community development.</p>
  <p id="teaching">I’m part of PolyU’s MDes Innovative Business Design programme, focusing on early-stage ventures and design-supported value creation. I received my Ph.D. in Industrial Design from KAIST in 2025. <a href="{{ '/teaching/' | relative_url }}">Teaching</a> · <a href="{{ '/cv/' | relative_url }}">Academic background</a></p>
  <p id="contact" class="personal-links"><a href="mailto:eunji.woo.phd@gmail.com">Email</a> <a href="{{ '/cv/' | relative_url }}">CV</a> <a href="https://www.linkedin.com/in/ooungy/">LinkedIn</a></p>
</section>

<section id="projects" class="home-section" aria-labelledby="projects-title">
  <h2 id="projects-title">Some projects</h2>
  <div class="project-list">
  {% assign selected_projects = site.portfolio | where: 'selected', true | sort: 'order' %}
  {% for project in selected_projects %}{% include project-entry.html %}{% endfor %}
  </div>
  <p class="archive-link"><a href="{{ '/projects/' | relative_url }}">More projects</a></p>
</section>

<section id="publications" class="home-section" aria-labelledby="publications-title">
  <h2 id="publications-title">Selected writing</h2>
  <ul class="publication-list">
  {% assign selected_publications = site.publications | where: 'selected', true | sort: 'sort_year' | reverse %}
  {% for publication in selected_publications %}{% include publication-entry.html %}{% endfor %}
  </ul>
  <p class="archive-link"><a href="{{ '/publications/' | relative_url }}">All publications</a></p>
</section>
