---
permalink: /software/
layout: page
title: Software
description: ""
header-img: 
comments: false
breadcrumbs: true
css: /assets/css/page.css
---

<div class="intro-row">
  <div class="intro-text">
    Our software development efforts will be listed here including tutorials for atomistic simulations.
  </div>
  <figure class="intro-image">
    <img src="{{ site.url }}/images/TJ.png" alt="">
  </figure>
</div>

<div class="toc-section">
  <div class="toc-nav">
    {% assign grouped_software = site.data.software | group_by: "category" %}
    {% for group in grouped_software %}
      <div class="toc-category">
        <button class="toc-category-btn" onclick="toggleTocDropdown(event)">
          {{ group.name }}
          <span class="toc-caret">▼</span>
        </button>
        <div class="toc-dropdown">
          {% for software in group.items %}
            <a href="#{{ software.name | slugify }}" class="toc-item">
              {{ software.name }}
              {% if software.highlight %}<span class="highlight-badge">★</span>{% endif %}
            </a>
          {% endfor %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<div class="software-grid">
  {% assign grouped_software = site.data.software | group_by: "category" %}
  {% for group in grouped_software %}
    <div class="category-section">
      <h2>{{ group.name }}</h2>
      <div class="card-container">
        {% for software in group.items %}
          <div class="software-card{% if software.highlight %} highlighted{% endif %}">
            <div class="card-header">
              <h3>{{ software.name }}</h3>
            </div>
            <div class="card-body">
              <p class="description">{{ software.description }}</p>
              
              {% if software.features.size > 0 %}
                <div class="features">
                  <h4>Features</h4>
                  <ul>
                    {% for feature in software.features %}
                      <li>{{ feature }}</li>
                    {% endfor %}
                  </ul>
                </div>
              {% endif %}
              
              {% if software.installation %}
                <div class="installation">
                  <h4>Installation</h4>
                  {{ software.installation | markdownify }}
                </div>
              {% endif %}
              
              {% if software.links.size > 0 %}
                <div class="links">
                  <h4>Links</h4>
                  <ul>
                    {% for link in software.links %}
                      <li><a href="{{ link.url }}" target="_blank">{{ link.text }}</a></li>
                    {% endfor %}
                  </ul>
                </div>
              {% endif %}
            </div> <!-- Close card-body -->
          </div> <!-- Close software-card -->
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>
<script src="{{ site.url }}/assets/js/software.js"></script>
