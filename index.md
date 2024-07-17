---
layout: default
---

# Responsible Disclosure Policy

## Announcement

<pre class="announcement">
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Dear valued researchers,

Starting from 26th July 2024, we will be taking a
break and will not be accepting any new
submissions during this period.

We deeply appreciate your understanding and
patience during this uncertain time. We look
forward to resuming our work and engaging with
your valuable submissions as soon as we are able.

Thanks for your understanding and ongoing support!

Best,
dw1
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCgAdFiEEDmLnOJC65PyD9kOJvZx+0YqeUHgFAmaXPk
8ACgkQvZx+0YqeUHhrEg//ePRj3oNY6+CUwiff2rfiuH0JRDy/
qT876L6tjeadF/j59SpZyqSVfH+cDTuMigQ/r1MYBnmcCo0oLZ
Q13R4CcQG+eXDwe6yfttcZgARkpVQ8IhuL6v3NWqo0qP0uvC2M
bOr+WpXcfPgFS3NE+/djFPjgoSMhY9vmDezJ81H1+UKtNWVyHy
U3mA2vYOKUDkSOS7ngUqdB8Q7lGOkiEUWudpxwj83ZxcjXpBnh
LQqzfB5kVsSNCsCgVWaPAAqbE34j1qJEF/ToTrMyaVTopHjnhu
JT2k3p69b+U5qtk1/+1faTurFKqhqIJhWi3LN8NgHJCkRCxXqM
S6wBeoKx15tFaYO1zibnZckCdirT0JUXtZRg2KUWHqA4Ug7CgD
+BE0igz76qzcXzFez+JZduDNdeH2RqdhvP9yXLnoaVK9tKL09H
tARvsZJATUlLbRsN2FydIJXsIDhjakegjngREJ23MJ+/MQQlQt
2+4IYmF1gQes6MLFhuB8K+K5mG5lC/zkUD4kPGCBKxeqBtfT+k
VByR/R+O16elFaHAqldnUBbG9k2NM1Ndl6JzW2krJY0YrneYv1
ZERJK6CIyRMXU8Uo7ZswK75njD9xpGgbPpERhxOgZgIKR7InLH
cjf7t14B23tBbTsWjeyq9e47KMQmpLfTg7cET7sn1vcPYG/zEN
KBig==5xKY
-----END PGP SIGNATURE-----
</pre>

## Introduction

Kitabisa.com welcomes feedback from security researchers and the general public to help improve our security. If you believe you have discovered a vulnerability, privacy issue, exposed data, or other security issues in any of our assets, we want to hear from you.
This policy outlines steps for reporting vulnerabilities to us, what we expect, what you can expect from us.

## Systems in Scope

{% for in-scope in site.scopes.in %}
- <div><b>{{ in-scope.value }}</b></div>
{% endfor %}

## Out of Scopes

{% for out-scope in site.scopes.out %}
- <div><b>{{ out-scope }}</b></div>
{% endfor %}
- Assets and/or other equipment not owned by parties participating in this policy.

Testing is only authorized on the targets listed as in scope. Any domain/property of Kitabisa not listed in the targets section is out of scope. This includes any/all subdomains not listed above.
Vulnerabilities discovered or suspected in out-of-scope systems should be reported to the appropriate vendor or applicable authority. If you think it demonstrably belongs to Kitabisa, use [Official Channels](#official-channels) to discuss with us.

## Our Commitments

When working with us, according to this policy, you can expect us to:

{% for commit in site.commitments %}
- <div>{{ commit }}</div>
{% endfor %}

## Our Expectations

In participating in our vulnerability disclosure program in good faith, we ask that you:

{% for expect in site.expectations %}
- <div>{{ expect }}</div>
{% endfor %}

## Official Channels 

Please report security issues via **{{ site.email }}**, providing all relevant information. The more details you provide, the easier it will be for us to triage and fix the issue.

The Kitabisa security team recommends to use [this PGP key](/pgp.txt) to sign all security notifications and encourages others to use this key when sending sensitive information to us.

<details>
	<summary>PGP fingerprint: <code>{{ site.pgp_fingerprint }}</code></summary>

<pre>
{% include_relative pgp.txt %}
</pre>
</details>

## Safe Harbor

When conducting vulnerability research, according to this policy, we consider this research conducted under this policy to be:

{% for harbor in site.harbors %}
- <div>{{ harbor }}</div>
{% endfor %}

You are expected, as always, to comply with all applicable laws. If legal action is initiated by a third party against you and you have complied with this policy, we will take steps to make it known that your actions were conducted in compliance with this policy.

If at any time you have concerns or are uncertain whether your security research is consistent with this policy, please submit a report through one of our [Official Channels](#official-channels) before going any further.

> Note that the Safe Harbor applies only to legal claims under the control of the organization participating in this policy, and that the policy does not bind independent third parties.