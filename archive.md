---
layout: imagepost
title: archive

---
<style> ul {
	-webkit-margin-before: 0;
} </style>


{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}