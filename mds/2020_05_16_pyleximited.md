---
### 2020-05-16 
# py-leximited

py-leximited is a python package for lexicographically delimited encoding and decoding.

The Leximited Format was created by Dave Ackley, and is described [here](https://github.com/elenasa/ULAM/wiki/Appendix-D:-Leximited-Format).

It is useful when working with lists of information that you want to keep in a specific order across different programs/operating systems/etc.

It also adds the useful feature of giving the length of the string as the first values of the string.

---

[Repository](https://github.com/isaac-art/py-leximited)

---

`pip install leximited` 

`import leximited`

`leximited.to_leximited('boo')` returns `'3boo'`

`leximited.from_leximited('3boo')` returns `'boo'`