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
  <p>I’m a design researcher based in Daejeon, South Korea. I work with local communities to understand how people shape the places and services around them.</p>
  <p>I’m a postdoctoral fellow in Industrial Design at KAIST and a part-time lecturer at Yonsei University’s Underwood International College. I received my Ph.D. in Industrial Design from KAIST in 2025. <span id="teaching">I also <a href="{{ '/teaching/' | relative_url }}">teach service design and social innovation</a>.</span></p>
  <p id="research">My research looks at local actors as “diffuse designers,” especially the role of local shops in community life. I develop methods, tools, and policy models through field-based collaboration. My current work also explores generative AI tools for prototyping service experiences.</p>
  <p id="contact" class="personal-links"><a href="mailto:eunji.woo@kaist.ac.kr">Email</a> <a href="{{ '/files/eunji-woo-cv.pdf' | relative_url }}">CV (PDF)</a> <a href="https://www.linkedin.com/in/ooungy/">LinkedIn</a></p>
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
