---
layout: archive
title: archive

---
<div class="archive">

{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}

</div>