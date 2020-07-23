# deeplpy
A deepl translator integration made with selenium

# Why should I use deeplpy?
* easy to use
* glossary support
* just a few integrations for python
* it's free
* under 100 lines of code
* compatible with firefox and chromium-based browsers
# How to use it
```bat
pip install deeplpy
```
```python
import deeplpy
deeplpy.translate(targetLang, stringArray, srcTextArray, targetTextArray)
```
You only have to put in **targetLang** and **stringArray**, use *srcTextArray* and *targetTextArray* if you want to add an entry to the glossary.
On the first time you also have to specify your path to the browser .exe and the driver .exe.
Also you will need a driver to run this. More information: https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference

# Example
```python
import deeplpy
print(deeplpy.translate("DE", ["Hello, world!", "This is a test."], ["This"], ["Das"]))
```
**Output**
```python
>>>['Hallo, Welt!', 'Das ist ein Test.']
```

# modules needed:
```bat
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


Thanks for reading, im new to the whole Github stuff and this is my first "big" python program :sweat_smile:
