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
> Starting **December 22nd**, and lasting until the New Year, we will temporarily pause the acceptance of new submissions. This decision is a result of the upcoming deployment freeze, which will limit our ability to review and address vulnerabilities promptly.
>
> Please be assured that your submissions are highly valued, and we encourage you to continue sending them to our [official channels](#official-channels). However, kindly note that our review and response to these submissions will resume once the holiday period ends and our deployment freeze lifts.
>
> Our Vulnerability Disclosure Program will resume normal operations on **January 1st, 2024**, and we will review all submissions received during this period as soon as possible after that date.
>
> Thank you for your ongoing support and thinking of Kitabisa security.<br>
> We wish you a joyful holiday season. Merry X-mas and happy New Year!
>
> Best!<br>
> dw1 @ Kitabisa Security Team<br>
> -----BEGIN PGP SIGNATURE-----
> 
> iQIzBAEBCgAdFiEEDmLnOJC65PyD9kOJvZx+0YqeUHgFAmWCAtgACgkQvZx+0Yqe<br>
> UHiokhAA3IhW8mSYtDwPmIJkjqXU60SAV0uHRRO84GfFI6Cj0bjtgcTbdN9Tjcr8<br>
> GCmFnWQ7PdFy2MeslZoHiCij1HzSDUnAhtOmnqk57otFu87SF7x6nqP/s9p+Nhgv<br>
> eJCkAroXJt5oN3fb2HFAy4Ek4y+bDp1na8zBaRWzlfv0YLLXwhRbFYmRXT9jEpsA<br>
> P+b1XaTObTjL3zjwsk869gMSKqBMMagJaHy5DDbwN3tuRurcslR3T2SCCBWdkqpO<br>
> m4mO9rcSb4vwvevTIS1WzJf+NivbskW2XV5/O09mTMyx37KBtEMa2f56rgH+GM0V<br>
> MjtD5CShJtYxYrK+D5B3m1k5D2/IjUKhdPQJSYpMj4AgJVHaR06bM9Ro9aPDnhLL<br>
> WY+Af4kUPj2htoZFSZRZnfJnnca8HUHCO3SdPmTzWHDG7xpGFaMiN7U8JrkPbT2r<br>
> OwK1zTCRIKP73svZ55ckoYBr93T4So5imNJw92MyJir8wYcalbWwggSosle4Cxog<br>
> PcyEGkQ8n5AfhWo5IAJgc+6nE5TfIdiatm7c58JKffBhdq9GIZ3MH9lgDNPUgsz0<br>
> ddTtpDZWtoGSvNGQBJQahS8HPl/rDUwb5kHDmx9shslX7K8o0igaKTQnYuFDhpbp<br>
> uoRfUrKRoEydwIY+mlF1HtFE3jXdGi6OsYWtPllOFbtBKSl3Sxs=<br>
> =tUEQ<br>
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