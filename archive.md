---
layout: imagepost
title: archive

---
<style> p {
	font-size: 18px;
	line-height: 36px;
	margin-bottom: 3px;
} </style>


{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}