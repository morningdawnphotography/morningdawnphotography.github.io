---
layout: archive
title: archive

---

<style> .content p {
	font-size: 18px;
	line-height: 36px;
	margin-bottom: 3px;
} 
.content ul {
	-webkit-margin-before: 0;
	-webkit-margin-after: 0;
	-webkit-padding-start: 0px;
}
</style>

{% for post in site.posts %}
  * {{ post.date | date: "%-m.%-d.%y" }} &raquo; [ {{ post.title }} ]({{ post.url }})
{% endfor %}
