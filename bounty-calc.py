#/usr/bin/env python3

import sys

rating_scale = [
    ("Low", (0.1, 3.9)),
    ("Medium", (4.0, 6.9)),
    ("High", (7.0, 8.9)),
    ("Critical", (9.0, 10.0)),
]

bounty_scale = [
    ("Low", 0),
    ("Medium", 999000),
    ("High", 1999000),
    ("Critical", 29990000)
]

def format_currency_idr(amount):
    return "IDR {:,.0f}".format(amount)

def get_severity(score):
    for severity, (lower, upper) in rating_scale:
        if lower <= score <= upper:
            return severity
    return None

def get_bounty(score):
    severity = get_severity(score)

    for rating_severity, (lower, upper) in rating_scale:
        if rating_severity == severity:
            for bounty_severity, higher in bounty_scale:
                if bounty_severity == severity:
                    bounty = higher * (score / upper)
                    return format_currency_idr(bounty)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        err = "No CVSS score provided!\n\n"
        err += "Usage:\n  python %s N.N\n" % (sys.argv[0])
        exit(err)

    score = float(sys.argv[1])
    print("""
        CVSS score : %g
        Severity   : %s
        Bounty     : %s
    """ % (score, get_severity(score), get_bounty(score)))
