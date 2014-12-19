---
layout: imagepost
title: archive

---
<style> ul {
	margin: 0;
} </style>


{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}