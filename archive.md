---
layout: imagepost
title: archive

---
ul {
	margin: 0em;
}


{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}