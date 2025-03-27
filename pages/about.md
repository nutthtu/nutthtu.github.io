---
permalink: /about/
layout: page
title: About Nutth Tuchinda
description: 
header-img: images/nutth.jpg
comments: false
breadcrumbs: true
---

Nutth is an incoming assistant professor in the [CME department at NJIT ](https://cme.njit.edu) starting Fall 2025.
Before that, he completed his PhD under a supervision of Prof. Chris Schuh or from [Schuh Group](schuh.northwestern.edu) at MIT (2019-2023). After his PhD, he work as a postdoc in Schuh and Olson group at MIT until Summer 2025.

See his [Current research interests]({{site.url}}/research), [scientific software]({{site.url}}/software)
and published [research articles]({{site.url}}/publications)

<div class="position-grid">
  {% for position in site.data.positions %}
  <div class="position-card">
    <div class="position-info">
      <h3>{{ position.title }}</h3>
      <div class="position-details">
        {% if position.roles %}
          {% for role in position.roles %}
            <strong>{{ role.title }} ({{ role.dates }})</strong><br>
          {% endfor %}
        {% endif %}
        {{ position.department }}<br>
        {{ position.address }}<br>
        {{ position.location }}<br>
        {% if position.phone %}Office: {{ position.phone }}<br>{% endif %}
        {% if position.mobile %}Mobile: {{ position.mobile }}<br>{% endif %}
        Email: {{ position.email }}<br>
        {% if position.profiles %}
          Department profile: 
          {% for profile in position.profiles %}
            <a href="{{ profile.url }}"> NJIT </a>
            {% unless forloop.last %}/{% endunless %}
          {% endfor %}
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<div markdown="0">
    <a href="{{ site.url }}/cv/" class="btn btn-info">View HTML</a>
    <a href="{{ site.url }}/downloads/CV.pdf" class="btn btn-success">Download PDF</a>
</div>

## About This Website
-----