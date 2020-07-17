# deepl-py
A deepl translator integration made with selenium

# Why should I use deepl-py?
* easy to use
* just a few (or none) integrations for python
* it's free
* under 100 lines of code
* compatible with firefox and chromium-based browsers
# How to use it
```bat
pip install deeplpy
```
```python
from deeplpy import translate
translate.translate(targetLang, stringArray, srcTextArray, targetTextArray)
```
You only have to put in **targetLang** and **stringArray**, use *srcTextArray* and *targetTextArray* if you want to add an entry to the glossary.
On the first time you also have to specify your path to the browser.exe and the driver.exe.

# Example
```python
from deepl import Translate
print(translate.translate("DE", ["Hello, world!", "This is a test."], ["This"], ["Das"]))
```
**Output**
```python
>>>['Hallo, Welt!', 'Das ist ein Test.']
```

# modules needed:
```bat
pip install pyperclip
pip install selenium
```
# supported languages:
| language      | language code |
| :-----------: |:-------------:|
| German        | DE            |
| English       | EN            |
| French        | FR            |
| Spanish       | ES            |
| Portuguese    | PT            |
| Italian       | IT            |
| Dutch         | NL            |
| Polish        | PL            |
| Russian       | RU            |
| Japanese      | JA            |
| Chinese       | ZH            |


Thanks for reading, im new to the hole Github stuff and this is mir first "big" python program so please be kind :sweat_smile:
