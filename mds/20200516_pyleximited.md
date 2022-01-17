---
### 2020-05-16 
# py-leximited

py-leximited is a python package for lexicographically delimited encoding and decoding.

It was created by Dave Ackley and is described [here](https://github.com/elenasa/ULAM/wiki/Appendix-D:-Leximited-Format).

It is useful when working with lists of information that you want to keep in a specific order across different programs/operating systems/etc.



---

[Repository](https://github.com/isaac-art/py-leximited)

---

`pip install leximited` 

`import leximited`

`leximited.to_leximited('boo')` returns `'3boo'`

`leximited.from_leximited('3boo')` returns `'boo'`