---
layout: default
---

# Responsible Disclosure Policy

## Announcement

> -----BEGIN PGP SIGNED MESSAGE-----<br>
> Hash: SHA512
>
> Dear valued researchers,
>
> Starting **December 22th**, and lasting until the New Year, we will temporarily pause the acceptance of new submissions. This decision is a result of the upcoming deployment freeze, which will limit our ability to review and address vulnerabilities promptly.
>
> Please be assured that your submissions are highly valued, and we encourage you to continue sending them to our [official channels](#official-channels). However, kindly note that our review and response to these submissions will resume once the holiday period concludes and our deployment freeze lifts.
>
> Our Vulnerability Disclosure Program will resume normal operations on **January 1st, 2024**, and we will review all submissions received during this period as soon as possible after that date.
>
> Thank you for your ongoing support and thinking of Kitabisa security.<br>
> We wish you a joyful holiday season, merry X-mas, and a happy New Year!
>
> Best!<br>
> dw1 @ Kitabisa Security Team<br>
> -----BEGIN PGP SIGNATURE-----
> 
> iQIzBAEBCgAdFiEEDmLnOJC65PyD9kOJvZx+0YqeUHgFAmWB+bkACgkQvZx+0Yqe<br>
> UHiZzA/+MraEqRdfQaGGzzLwtx1twQm1JoQ4L6e9S4pQm2E2KUCsO5al/d1GWQul<br>
> +O0oAizAmCWgLsjSTkeRV5lH1DyHZ2CiSbvXTMahhMlRD8rSxneTps9IxgbdbM9H<br>
> fFjImrHHAB51+RYBwDp+5tbXWMUy8eUAx8B9oQQXZ6MCHA1lgNKCgYn6OO/dtmK0<br>
> WnRJeuKs4uTt8XivMqIOCzKru1moGQBB8fQ8BjtmtzZashpkxG8ec6ViEGhG5yHE<br>
> KSJ/PQI4qXZ14h3I5wJlJMkujzutqf+6Fo+gRVAvHHJHvgnjZ1VHPwyGsH/yfja9<br>
> rlw/Rg1QswX2//bJcXVh4lhayd+5bqkw2+cW0KX5BcxkLNUkdBT5x79cVQ28T9eY<br>
> UwwbPre73D4VsELeUhJeUreUhBdn7JWXRGIZa2JB/A4lVxysGwSE8aKuVmVapClT<br>
> cEk46N1Pq+fijSxI6k/HLJTRRtYJlU3UR4Vf200oSH3p5LwSLEJHtMnxQcF/laSB<br>
> 3jFD3+F9O8t5h+HCI9n72kW+e4DRRtcx5NBoSCo3G1WmgnXFqaC9+mcgs7+mSP3M<br>
> MKNfnroDNO/XZM3vd58qtyC74VD+4ZU2HMcRXJK5XduXJk6cWEiSWa0n0cfOd62O<br>
> KoK8J1FdXITfvNy4dwGbYiHvOhZSWYx/lkDgk9onNuR9WxMQZc0=<br>
> =Zv88<br>
> -----END PGP SIGNATURE-----
{: .announcement }


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