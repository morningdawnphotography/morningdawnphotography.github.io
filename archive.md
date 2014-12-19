---
layout: imagepost
title: archive

---
ul {
-webkit-margin-before: 0em;
}


{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}