---
layout: archive
title: archive

---

{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}
