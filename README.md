# Notes on [Learn Python The Hard Way](http://learnpythonthehardway.org/book)


### Ex. 7 - *More Printing*

```python
print 'This is an %r' % 'example'
```
will print out
`This is an 'example'`

`%r` will display *raw* data, `%r` is best for debugging.

---

### Ex. 10 - *What Was That?*

##### **Escape Sequences**
Escape       | What it does
------------ | ------------------------------
`\a`         | ASCII bell (BEL)
`\b`         | ASCII backspace (BS)
`\f`         | ASCII formfeed (FF)
`\N(name)`   | Unicode character
`\r`         | Carriage Return (CR)
`\t`         | Horizontal tab (TAB)
`\v`         | ASCII Vertical tab (VT)
`\ooo`       | Character with octal value ooo
`\xhh`       | Chacarter with hex value hh
`\uxxxx`     | 16-bit hex value xxxx (Unicode)
`\uxxxxxxxx` | 32-bit hex value xxxx (Unicode)

---

### Ex. 11 - *Asking Questions*

`input()` function will try to convert things you enter as if they were Python code.
`raw_input()` is *safer* than `input()`

---

### Ex. 12 - *Prompting People*

The built-in function `help()` invokes the online help system in the interactive interpreter, which uses pydoc to generate its documentation as text on the console.
The same text documentation can also be viewed from **outside** the Python interpreter by running `pydoc` as a script at the operating system’s command prompt.
For example, running
`$ pydoc sys`
will display documentation on the sys module

---

### Ex. 13 - *Parameters, Unpacking, Variables*

```python
from sys import argv
script, first, second, third = argv
```
`argv` *holds* the arguments you pass to your Python script when you run it.

---

### Ex. 16 - *Reading and Writing Files*

`handle.readline()` reads one line of a file
`handle.truncate()` empties a file
`handle.write('something')` writes `something` to a file

`open(name[, mode])` opens a file
  * Modes:
    - `r` read (default when mode is omitted)
    - `w` write (truncates if file exists)
    - `a` append
    - `r+`, `w+`, `a+` open a file for updating (read and write). `w+` truncates the file.
