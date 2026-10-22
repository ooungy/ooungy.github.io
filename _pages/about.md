---
layout: academic
home: true
permalink: /
redirect_from:
- /about/
- /about.html
---


<section class="hero" aria-labelledby="intro-title">
  <div>
    <p class="eyebrow">Design research · Community practice</p>
    <h1 id="intro-title">Eunji Woo</h1>
    <p class="hero-statement">Designing with<br>local communities.</p>
    <p class="hero-intro">I study how local actors shape community life through situated, creative action.</p>
    <a class="text-link" href="#research">Explore my research <span aria-hidden="true">↓</span></a>
  </div>
  <aside class="hero-aside" aria-label="Current appointments">
    <p class="eyebrow">Currently</p>
    <p><strong>Postdoctoral Fellow</strong><br>Industrial Design, KAIST</p>
    <p><strong>Part-time Lecturer</strong><br>Underwood International College,<br>Yonsei University</p>
    <p class="location">Daejeon, Republic of Korea</p>
    <a href="mailto:eunji.woo@kaist.ac.kr">eunji.woo@kaist.ac.kr</a>
  </aside>
</section>

<section id="about" class="home-section" aria-labelledby="about-title">
  <div class="section-label"><span>01</span><h2 id="about-title">About</h2></div>
  <div class="section-body prose">
    <p class="lead">My research examines how local actors function as “diffuse designers” in shaping community life.</p>
    <p>I develop design methods, tools, and policy models that translate tacit local practices into structured and scalable forms. Through collaborative, field-based research, I work with communities to co-develop and validate these approaches in practice.</p>
    <p>I received my Ph.D. in Industrial Design from KAIST in 2025. My doctoral research focused on community-anchored customer experiences for local shops, bringing together design processes, technology mediation, facilitation, and policy support.</p>
    <a class="text-link" href="{{ '/cv/' | relative_url }}">More about my background <span aria-hidden="true">↗</span></a>
  </div>
</section>

<section id="research" class="home-section" aria-labelledby="research-title">
  <div class="section-label"><span>02</span><h2 id="research-title">Research</h2></div>
  <div class="section-body">
    <p class="section-intro">Design as a way to support bottom-up innovation while preserving human agency.</p>
    <div class="research-grid">
      <div><h3>Community &amp; local life</h3><p>Local shops as community anchors, neighborhood knowledge, and the creative practices of local actors.</p></div>
      <div><h3>Methods &amp; participation</h3><p>Co-design, speculative interventions, design facilitation, and policy support developed through field-based collaboration.</p></div>
      <div><h3>Technology &amp; agency</h3><p>Technology-mediated service experiences and generative AI tools for prototyping co-located social interactions.</p></div>
    </div>
  </div>
</section>

<section id="publications" class="home-section" aria-labelledby="publications-title">
  <div class="section-label"><span>03</span><h2 id="publications-title">Selected <br>publications</h2></div>
  <div class="section-body">
    <ul class="publication-list">
    {% assign selected_publications = site.publications | where: 'selected', true | sort: 'sort_year' | reverse %}
    {% for publication in selected_publications %}{% include publication-entry.html %}{% endfor %}
    </ul>
    <a class="text-link" href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">→</span></a>
  </div>
</section>

<section id="projects" class="home-section" aria-labelledby="projects-title">
  <div class="section-label"><span>04</span><h2 id="projects-title">Selected <br>projects</h2></div>
  <div class="section-body">
    <div class="project-grid">
    {% assign selected_projects = site.portfolio | where: 'selected', true | sort: 'order' %}
    {% for project in selected_projects %}{% include project-entry.html %}{% endfor %}
    </div>
    <a class="text-link" href="{{ '/projects/' | relative_url }}">All projects <span aria-hidden="true">→</span></a>
  </div>
</section>

<section id="teaching" class="home-section" aria-labelledby="teaching-title">
  <div class="section-label"><span>05</span><h2 id="teaching-title">Teaching</h2></div>
  <div class="section-body">
    <p class="section-intro">Service design, social innovation, and community-centered practice.</p>
    {% assign courses = site.teaching | where: 'category', 'university' | sort: 'order' %}
    {% for course in courses %}<div class="teaching-row"><div><h3><a href="{{ course.url | relative_url }}">{{ course.title }}</a></h3><p>{{ course.institution }}</p></div><span>{{ course.terms }}</span></div>{% endfor %}
    <a class="text-link" href="{{ '/teaching/' | relative_url }}">Teaching &amp; supervision <span aria-hidden="true">→</span></a>
  </div>
</section>

<section id="contact" class="home-section contact-section" aria-labelledby="contact-title">
  <div class="section-label"><span>06</span><h2 id="contact-title">CV / Contact</h2></div>
  <div class="section-body">
    <p class="contact-heading">Get in touch.</p>
    <p><a class="contact-email" href="mailto:eunji.woo@kaist.ac.kr">eunji.woo@kaist.ac.kr</a></p>
    <div class="contact-links"><a href="{{ '/files/eunji-woo-cv.pdf' | relative_url }}">Download CV (PDF) <span aria-hidden="true">↗</span></a><a href="https://www.linkedin.com/in/ooungy/">LinkedIn <span aria-hidden="true">↗</span></a></div>
  </div>
</section>
