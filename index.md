---
layout: default
---

# Responsible Disclosure Policy

## Notice

> Dear valued researchers,
>
> We want to thank you for your participation in our bug bounty program over the past years. It has been an incredible journey, and your contributions have helped us identify and resolve critical security issues, making our systems more secure and reliable for our customers.
> 
> As we continue to evolve our security posture, we have decided to end our bug bounty program in **31 March, 2023**. Instead, we will be transitioning to a vulnerability disclosure program (VDP).
> 
> The VDP will still prioritize the security of our products and users, but will focus on prompt and transparent communication between the researcher and our security team. We believe that this new program will foster a stronger relationship with the security research community, and will result in a more effective and efficient vulnerability management process.
> 
> Please note that any submissions made after the bug bounty program's end date will not be eligible for rewards. We appreciate your understanding and look forward to continuing our collaboration to maintain a secure platform.
> 
> Thanks for thinking of Kitabisa security!

## Introduction

Kitabisa.com welcomes feedback from security researchers and the general public to help improve our security. If you believe you have discovered a vulnerability, privacy issue, exposed data, or other security issues in any of our assets, we want to hear from you.
This policy outlines steps for reporting vulnerabilities to us, what we expect, what you can expect from us.

## Systems in Scope

{% for in-scope in site.scopes.in %}
- <div><b>{{ in-scope.value }}</b>{% if in-scope.eligible == false %} <span class="ineligible">❌</span>{% endif %}</div>
{% endfor %}

<b>\*</b> <span class="ineligible">❌</span>: ineligible for the bounty; but, you may receive credit for the CVE ID.

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

## Rewards

Our rewards are determined by the Kitabisa security team based on the potential impact of a vulnerability and how detailed the respective report is.

<table>
  <thead>
    <tr>
      <th><strong>Severity</strong></th>
      <th><strong>Bounty</strong></th>
    </tr>
  </thead>
  <tbody>
  {% for bounty in site.bounties %}
    <tr>
      <td>{{ bounty.severity }}</td>
      <td>{{ bounty.range }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<b>\*</b> Please note those are general guidelines, and reward decisions are up to the discretion of Kitabisa.

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