---
layout: post
title: "Tutorial on TripleJunction.py"
subheadline: "Performing triple junction identification using OVITO Python package"
description: "TJ"
author: nutthtu
date: 2025-03-27
modified: 2025-03-27
image:
    feature: false
    twitter: 
categories: [Software, Tutorial]
tags: [Python, TripleJunction.py, Algorithms]
show_meta:
    info: true
---

(To be updated)

This is a tutorial on how to identify triple junctions in polycrystalline materials using OVITO modifiers and [TripleJunction.py](https://github.com/nutthtu/TripleJunction.py)


<!--more-->

{% include toc.md panel=true %}

## Getting started

First, we import OVITO python package which are necessary for identifying unique grains.

{% highlight python linenos %}
import ovito
{% endhighlight %}

<figure class="image">
    <img src="{{ site.url }}/images/logo.png" alt="TJ" width="600px">
</figure>
