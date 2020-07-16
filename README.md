# deepl-py
A deepl translator integration made with selenium

# Why should I use deepl-py?
* easy to use
* just a few (or none) integrations for python
* it's free
* only 100 lines of code
* compatible with firefox and chromium-based browsers
# How to use it
```python
from deepl import Translate
Translate(targetLang, stringArray, srcTextArray, targetTextArray).translate()
```
You only have to put in **targetLang** and **stringArray**, use *srcTextArray* and *targetTextArray* if you want to add an entry to the glossary.
On the first time you also have to specify your path to the browser.exe and the driver.exe.

# Example
```python
from deepl import Translate
print(Translate("DE", ["Hello, world!", "This is a test."], ["This"], ["Das"]).translate())
```
**Output**
```python
>>>['Hallo, Welt!', 'Das ist ein Test.']
```



Thanks for reading, im new to the hole Github stuff and this is mir first "big" python program so please be kind :sweat_smile:
