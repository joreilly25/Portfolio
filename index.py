#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import sys
cgitb.enable()

print("Content-Type: text/html; charset=utf-8")
print("")

print("""\
<html>
<head><title>Python Hello World</title></head>
<body>
"""
+"<h1>Hello World from Python "+sys.version+"!</h1>"+ """\
</body></html>
""")
