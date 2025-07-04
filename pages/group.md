---
permalink: /group/
layout: page
title: Group Members
description: "Group members: a list of current group members and alumni."
header-img: images/research-1.jpg
comments: false
breadcrumbs: true
---

We are recruiting! See [current opening]({{site.url}}/opening)


## Principle Investigator
-----

{% for member in site.data.group.principle_investigator %}
<div class="pi-card">
  <div class="pi-info">
    <h3>{{ member.name }}</h3>
      <div class="member-bio">{{ member.bio | markdownify }}</div>
    <a href="{{ site.url }}{{ member.bio_link }}" class="member-link">View Biography →</a>
  </div>
  <div class="pi-photo">
    <img src="{{ site.url }}/{{ member.image }}" alt="{{ member.name }}">
  </div>
</div>
{% endfor %}

## Graduate Students
-----

{% for member in site.data.group.graduate_students %}
<div class="pi-card">
  <div class="pi-info">
      <h4>{{ member.name }}</h4>
      {% if member.period %}<p class="member-period">{{ member.period }}</p>{% endif %}
      <div class="member-description">{{ member.description | markdownify }}</div>
  </div>
  <div class="pi-photo">
    <img src="{{ site.url }}/{{ member.image }}" alt="{{ member.name }}">
  </div>
</div>

{% endfor %}


## Undergraduate Students
-----

<div class="member-grid">
{% for member in site.data.group.undergraduate_students %}
<div class="pi-card">
  <div class="pi-info">
    <h3>{{ member.name }}</h3>
      <div class="member-bio">{{ member.bio | markdownify }}</div>
    <a href="{{ site.url }}{{ member.bio_link }}" class="member-link">View Biography →</a>
  </div>
  <div class="pi-photo">
    <img src="{{ site.url }}/{{ member.image }}" alt="{{ member.name }}">
  </div>
</div>
{% endfor %}


## Alumni
-----

<div class="member-grid">
{% for member in site.data.group.alumni %}
  <div class="member-card">
    <div class="member-info">
      <h4>{{ member.name }}</h4>
      {% if member.period %}<p class="member-period">{{ member.period }}</p>{% endif %}
      <div class="member-description">{{ member.description | markdownify }}</div>
    </div>
  </div>
{% endfor %}
</div>
