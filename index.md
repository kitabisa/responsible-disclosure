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
> Starting **December 22nd**, and lasting until the New Year, we will temporarily pause the acceptance of new submissions. This decision is a result of the upcoming deployment freeze, which will limit our ability to promptly review and address vulnerabilities, consequently delaying the rollout of the patch.
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
> iQIzBAEBCgAdFiEEDmLnOJC65PyD9kOJvZx+0YqeUHgFAmWCD2EACgkQvZx+0Yqe<br>
> UHhfVg//VlfUliziiqbRoA+vgHoIEKSAszpktsvNrNpx+LDJ1huAu2lci0O/V2uH<br>
> grH1rRcrRLPb8h0f6mhzBAnQGEJHn9hM/EzQRXWtgNoroSN48CLMLPYx3+tXMHga<br>
> sMY/W5sIoR9khxQToWJHofsWnFiSVGKzgZXoHLT8rLKuju/ZgoO4VcVjZERXbtbF<br>
> Nvw99LCxUaUip+ctxgwfmNLRXlahiwFiSude34yvnFR65enhAAQImBn7j7fklI9m<br>
> oBFTPi7v01dx/aCGwvgngAqEzaDGIxphIBSLuaTUCl9/N8q0qsd0iCLPrLPhxHSk<br>
> QIvYhhGuFROS8DejP5R8V4ikxTmDsaOA2ODosACa2CxAlmOTMqm/Hh04siMMxGUr<br>
> YdQZvWmexVkfMYIiryxlcf1fuBKbkn7twvYN7XLRrV+BptD/1nbVd0gnbYEhC3b7<br>
> kXajCTW85EHaNk8D31DoGWMCPBQ68MeFMZfw9RheSwWGx2Ft5/GV+SqUwTTbRX0G<br>
> WPgW80bS5N39V8rjtnVKJGNnBqqRGhvfU4BkHPtoMI4JioNElm1IbM+MHSfEJs91<br>
> TG2N2+HLJxYW/oHdml23X6/r8hO5sklgaBm4L5UHBJSZTr5/SjzmcCfJNg1Vpfiu<br>
> YHbq4na7Fp77yf8EG+tuhOmJazzH5yHVx6L0oVBVQYhbE6czDic=<br>
> =Qeyu<br>
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