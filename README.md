# regxy
Python module for making regex painless.

### Operations Supported
- Match everything between two texts
- Extract emails
- Extract phone numbers

### Installation
You can install it using pip as follows:
```bash
pip install regxy
```
or you can clone this repo for favoring portability:
```bash
git clone https://github.com/UltimateHackers/rexgy/
```
## Usages

### grab
Lets say there's website which generates a random password when you visit it. By looking at the source code, you find this:
```html
This is your random password: <span color="red" id="pass">puSSySlay3r</span>. Enjoy!
```
Now you want to write a program which can visit the website can and can return you the generated password.
In that case, you can use regxy as follows:
```python
from regxy import grab
grab(string, 'id="pass">', '</span>')
```
The syntax is following:
```python
grab(string, start, end)
```
Where string is the string you want to process, start and end are the texts within which your infromation of interest lies.</br>
In this case your string is the source code of the website which can be extracted by other modules.<br>

### graball
Lets say there's a website which has a list of proxies and you want to write a program to extract those proxies.
The source code is something like:
```html
<td class="dark">127.0.0.1:80</td>
<td class="dark">127.0.0.2:8080</td>
<td class="dark">127.0.7:80</td>
<td class="dark">127.255.255.255:80</td>
```
In this case, you can use the <b>graball</b> function which returns all the matches unlike <b>grab</b> which only returns one.
The syntax is as same as the <b>grab</b> function but it returns a list and not a string.
```python
from regxy import graball

grab(string, 'pass">', '</td>')
```

### emails
As the name suggest, this function can extract emails from a given string with 99.99% accuracy.
Usages:
```python
from regxy import emails
emails(string)
```
It returns a list of matches.

### numbers
This function can extract phone numbers from a given string.
Usages:
```python
from regxy import numbers
numbers(string)
```
It returns a list of matches.

### What if there's no match?
Well in that case all the functions return <b>False</b>.

### License & Contribution
Contributions are heartly welcome, doesn't matter if they are bug reports, pull requests or ideas to make <b>regxy</b> better.</b>

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
