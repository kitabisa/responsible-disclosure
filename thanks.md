---
layout: default
---

# Hall of Fame

We would like to thank the following people for making a responsible disclosure to us and helping keep Kitabisa secure:

<ol type="1">
{% for user in site.data.thanks %}
  <li><b>{{ user.name }}</b></li>
{% endfor %}
</ol>

\* Sort by latest.