Bhai, ye **Python + Git + GitHub ka consolidated revision manual** hai — Roman Urdu mein, English technical terms ke saath. Isko save kar lena; isi ko baad mein project ke time reference bana sakte ho.

# 📘 Python + Git/GitHub Revision Notes

## PART 1 — PYTHON

### 1. Variables

Variable kisi value ko store karne ke liye hota hai.

```python
name = "Ibtehaj"
age = 25
salary = 50000
```

Python mein type manually declare nahi karni padti.

```python
x = 10
x = "Hello"
```

`x` ka type change ho sakta hai.

Useful:

```python
type(x)
```

Example:

```python
age = 25
print(type(age))
```

---

## 2. Basic Data Types

### String

```python
name = "Ibtehaj"
```

### Integer

```python
age = 25
```

### Float

```python
price = 99.5
```

### Boolean

```python
is_admin = True
```

Common type conversion:

```python
age = int("25")
price = float("99.5")
num = str(100)
```

---

## 3. Input / Output

```python
name = input("Enter your name: ")
print("Hello", name)
```

Important:

> `input()` normally **string** return karta hai.

Isliye:

```python
age = int(input("Enter age: "))
```

---

## 4. Operators

### Arithmetic

```python
+
-
*
/
%
**
//
```

Example:

```python
10 % 3
```

Result:

```text
1
```

`%` remainder deta hai.

`//` floor division karta hai.

### Comparison

```python
==
!=
>
<
>=
<=
```

### Logical

```python
and
or
not
```

---

# 5. `if / elif / else`

Decision making:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Multiple conditions:

```python
marks = 75

if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

### Tumhari important logic mistake

Galat:

```python
if x % 2 == 2:
```

Sahi:

```python
if x % 2 == 0:
```

Reason:

Even number ko 2 se divide karne par remainder `0` hota hai.

---

# 6. Loops

Loops repeated work ke liye.

## `for`

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### `range()`

```python
range(start, stop, step)
```

Important:

> `stop` include nahi hota.

Example:

```python
range(1, 6)
```

= `1, 2, 3, 4, 5`

Reverse:

```python
range(10, 0, -1)
```

= `10 ... 1`

Odd numbers:

```python
range(1, 21, 2)
```

= `1, 3, 5 ... 19`

---

## 7. `while`

Jab tak condition true ho:

```python
x = 1

while x <= 5:
    print(x)
    x += 1
```

---

# 8. `break`, `continue`, `pass`

### break

Loop stop:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### continue

Current iteration skip:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# 9. Functions

Function reusable code block hai.

```python
def greet():
    print("Hello")
```

Call:

```python
greet()
```

### Parameter

```python
def greet(name):
    print("Hello", name)
```

```python
greet("Ibtehaj")
```

---

## 10. `return`

Function ka result bahar dene ke liye:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

### Tumhari important mistake

Galat:

```python
def sum_numbers(nums):
    total = 0

    for n in nums:
        total += n
        return total
```

`return` loop ke andar hai, isliye first iteration ke baad function stop ho jayega.

Sahi:

```python
def sum_numbers(nums):
    total = 0

    for n in nums:
        total += n

    return total
```

### Logic lesson

> Pehle loop complete → phir result return.

---

# 11. Lists

List ordered aur changeable collection hai.

```python
cars = ["Toyota", "Honda", "BMW"]
```

Index:

```python
cars[0]
```

Replace:

```python
cars[1] = "Suzuki"
```

Add:

```python
cars.append("Kia")
```

Remove:

```python
cars.remove("BMW")
```

Length:

```python
len(cars)
```

Loop:

```python
for car in cars:
    print(car)
```

---

# 12. Tuple

Tuple ordered hoti hai lekin normally immutable hoti hai.

```python
point = (10, 20)
```

Access:

```python
point[0]
```

---

# 13. Set

Unique values:

```python
numbers = {1, 2, 3, 3, 4}
```

Duplicate remove ho jayega.

```python
print(numbers)
```

Useful for membership/unique data.

---

# 14. Dictionary

Key-value data:

```python
user = {
    "name": "Ibtehaj",
    "age": 25,
    "role": "IT Administrator"
}
```

Access:

```python
user["name"]
```

Add:

```python
user["city"] = "Karachi"
```

Loop:

```python
for key, value in user.items():
    print(key, value)
```

---

# 15. List Comprehension

Normal:

```python
squares = []

for i in range(5):
    squares.append(i * i)
```

Comprehension:

```python
squares = [i * i for i in range(5)]
```

Condition:

```python
even = [i for i in range(10) if i % 2 == 0]
```

---

# 16. `*args`

Multiple positional arguments:

```python
def total(*args):
    return sum(args)
```

```python
print(total(1, 2, 3, 4))
```

---

# 17. `**kwargs`

Multiple keyword arguments:

```python
def show_user(**kwargs):
    print(kwargs)
```

```python
show_user(name="Ibtehaj", age=25)
```

`kwargs` dictionary ki form mein milta hai.

---

# 18. Scope

Local variable:

```python
def test():
    x = 10
```

`x` function ke andar available hai.

Global:

```python
x = 10

def test():
    print(x)
```

---

# 19. Modules

Ek Python file ko doosri file mein use karna.

`math_tools.py`

```python
def add(a, b):
    return a + b
```

Doosri file:

```python
import math_tools

print(math_tools.add(2, 3))
```

Specific import:

```python
from math_tools import add
```

---

# 20. Packages

Multiple Python modules ka organized folder structure.

Example:

```text
project/
├── main.py
└── utils/
    ├── __init__.py
    └── helper.py
```

Large projects mein useful.

---

# 21. File Handling

### Read

```python
with open("test.txt", "r") as file:
    data = file.read()

print(data)
```

### Write

```python
with open("test.txt", "w") as file:
    file.write("Hello")
```

### Append

```python
with open("test.txt", "a") as file:
    file.write("\nNew line")
```

Important:

> `with open(...)` use karna best practice hai, kyunki file automatically close ho jati hai.

---

# 22. Exception Handling

Error ko gracefully handle karna:

```python
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid number")
```

Multiple:

```python
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
```

`finally`:

```python
try:
    ...
except:
    ...
finally:
    print("Done")
```

---

# 23. Logging

Debugging aur application events track karne ke liye.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("Something unusual happened")
logging.error("An error occurred")
```

Levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

# 24. OOP — Object Oriented Programming

Class blueprint hoti hai.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)
```

Object:

```python
student1 = Student("Ibtehaj")
student1.greet()
```

### Important terms

```text
Class       = blueprint
Object      = instance
Attribute   = object ka data
Method      = object ka function
__init__    = constructor/initializer
self        = current object
```

---

# 25. Inheritance

Ek class doosri class se properties/methods le sakti hai.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass
```

```python
dog = Dog()
dog.speak()
```

---

# 26. Iterators

Iterator ek-ek value provide karta hai.

```python
numbers = iter([1, 2, 3])

print(next(numbers))
print(next(numbers))
```

---

# 27. Generators

`yield` use karte hain.

```python
def numbers():
    for i in range(5):
        yield i
```

Generator memory-efficient ho sakta hai because values lazily generate hoti hain.

---

# 28. Decorators

Function ke behavior ko modify/wrap karne ke liye.

Basic pattern:

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

---

# 29. JSON

APIs aur data exchange mein bohot common.

```python
import json

data = {
    "name": "Ibtehaj",
    "age": 25
}

text = json.dumps(data)
print(text)
```

JSON se Python:

```python
obj = json.loads(text)
```

---

# 30. CSV

Tabular data.

```python
import csv

with open("users.csv", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# 31. APIs

API ka basic idea:

```text
Python
   ↓
HTTP Request
   ↓
Server/API
   ↓
JSON Response
   ↓
Python
```

Common HTTP methods:

```text
GET
POST
PUT
PATCH
DELETE
```

Example library:

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

Common status codes:

```text
200 = OK
201 = Created
400 = Bad Request
401 = Unauthorized
403 = Forbidden
404 = Not Found
500 = Server Error
```

---

# 32. `pip`

Python packages install karne ke liye:

```powershell
pip install requests
```

Check:

```powershell
pip list
```

---

# 33. Virtual Environment

Project ka isolated Python environment.

Create:

```powershell
python -m venv venv
```

Activate Windows:

```powershell
venv\Scripts\activate
```

Deactivate:

```powershell
deactivate
```

---

# 🧠 Python Logic — Tumhare liye most important

Tumne practice mein jo mistakes ki, unse ye rules yaad rakho:

### Even/odd

```python
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Running total

```python
total = 0

for num in numbers:
    total += num
```

### Count

```python
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1
```

### General logic pattern

```text
Input
 ↓
Condition
 ↓
Loop
 ↓
Update variable
 ↓
Result
```

**Logic tumhara core practice area hai.**

---

# PART 2 — GIT & GITHUB

## 34. Git kya hai?

Git **version control system** hai.

Matlab:

> Code ke changes ka history maintain karta hai.

Example:

```text
Version 1
   ↓
Version 2
   ↓
Version 3
```

Tum dekh sakte ho kis commit mein kya change hua.

---

# 35. GitHub kya hai?

GitHub Git repositories ko online host karta hai.

Simple:

```text
Git  = version control
GitHub = online repository/platform
```

---

# 36. Repository

Project + Git history + configuration.

Local:

```text
project/
└── .git/
```

GitHub:

```text
GitHub Repository
```

---

# 37. `git init`

Existing folder ko Git repository banana:

```powershell
git init
```

---

# 38. `git status`

Current situation:

```powershell
git status
```

Ye batata hai:

* current branch
* modified files
* staged files
* untracked files
* remote se ahead/behind status

---

# 39. `git add`

Changes ko staging area mein dalta hai.

One file:

```powershell
git add file.py
```

All:

```powershell
git add .
```

---

# 40. `git commit`

Staged changes ko Git history mein save karta hai:

```powershell
git commit -m "Add login feature"
```

### Remember

```text
git add
= prepare

git commit
= local history mein save
```

---

# 41. `git log`

History:

```powershell
git log
```

Short:

```powershell
git log --oneline
```

Graph:

```powershell
git log --oneline --graph --all
```

### Pager se bahar

Agar:

```text
(END)
```

aaye:

```text
q
```

press karo.

---

# 42. `git diff`

Uncommitted changes dekhne ke liye:

```powershell
git diff
```

Useful habit:

```text
edit
 ↓
git diff
 ↓
git add
```

---

# 43. `.gitignore`

Aisi files/folders ko ignore karne ke liye jo GitHub par nahi bhejni.

Example:

```gitignore
__pycache__/
*.pyc
.env
venv/
```

Important:

> `.gitignore` untracked files ko ignore karta hai. Agar file pehle se tracked hai, sirf `.gitignore` add karne se automatically untrack nahi hoti.

---

# 44. `git rm --cached`

Tracked file ko repository se remove karo, lekin computer par rakho:

```powershell
git rm --cached file.py
```

Useful jab accidentally koi file Git track kar raha ho aur ab `.gitignore` mein add karni ho.

---

# 45. GitHub Remote

Remote check:

```powershell
git remote -v
```

Remote add:

```powershell
git remote add origin https://github.com/USERNAME/REPO.git
```

`origin` usually remote ka default name hota hai.

---

# 46. `git push`

Local commits → GitHub:

```powershell
git push
```

First time branch:

```powershell
git push -u origin feature-practice
```

Memory:

```text
Local → GitHub
```

---

# 47. `git pull`

GitHub ke latest changes local repository mein lana:

```powershell
git pull
```

Memory:

```text
GitHub → Local
```

Important:

> `git pull` Pull Request nahi hai.

---

# 48. `git clone`

GitHub se complete repository new computer/folder par lana:

```powershell
git clone https://github.com/USERNAME/REPO.git
```

Clone ke saath:

* files
* Git history
* remote connection

aate hain.

### Basic clone flow

```powershell
cd "location"
git clone <URL>
cd <repo>
git status
```

---

# 49. Branch

Separate development line.

Check:

```powershell
git branch
```

New branch:

```powershell
git branch feature-practice
```

Switch:

```powershell
git switch feature-practice
```

Create + switch:

```powershell
git switch -c feature-practice
```

---

# 50. Merge

Feature branch ko current branch mein combine karna.

```powershell
git switch master
git merge feature-practice
```

Golden rule:

> **Jis branch mein feature lana hai, pehle us branch par switch karo.**

Example:

```text
feature-practice
       ↓
     merge
       ↓
     master
```

---

# 51. Merge Conflict

Conflict tab hota hai jab Git automatically decide na kar sake ke kaunsa change rakhna hai.

Example:

```text
<<<<<<< HEAD
MASTER VERSION
=======
FEATURE VERSION
>>>>>>> feature-practice
```

Tum manually correct code choose karte ho aur markers remove karte ho.

Phir:

```powershell
git add .
git commit -m "Resolve merge conflict"
```

### Memory

```text
CONFLICT
 ↓
FIX FILE
 ↓
git add
 ↓
git commit
```

---

# 52. `git fetch`

Remote information download karta hai, **merge nahi karta**.

```powershell
git fetch origin
```

Then inspect/merge separately.

Difference:

```text
fetch = changes ki information lao
pull  = fetch + integrate
```

---

# 53. Pull Request

PR ka matlab:

> Feature branch ke changes ko main/master mein merge karne ki request.

Normal workflow:

```text
feature branch
 ↓
change
 ↓
commit
 ↓
push
 ↓
GitHub
 ↓
Pull Request
 ↓
review
 ↓
merge
```

PR aur `git pull` different hain.

### `git pull`

```text
GitHub → Local
```

### Pull Request

```text
Feature → Main branch
```

---

# 54. PR Conflict

Agar GitHub PR bole:

```text
This branch has conflicts that must be resolved
```

Common local method:

```powershell
git fetch origin
git switch feature-practice
git merge origin/master
```

Conflict resolve karo:

```powershell
git add .
git commit -m "Resolve PR merge conflict"
git push
```

PR automatically update ho sakti hai.

---

# 55. `git restore`

Uncommitted working-file changes discard:

```powershell
git restore file.py
```

Tumne iska practical use kiya:

```text
temporary change
 ↓
git restore
 ↓
file old committed state par
```

### Unstage

```powershell
git restore --staged file.py
```

Isse staging area se file remove hoti hai, working file ki changes rehti hain.

---

# 56. `git reset`

Local Git history/staging ko move karne ke liye.

## Soft

```powershell
git reset --soft HEAD~1
```

Result:

```text
commit ❌
changes ✅
staged ✅
```

Use jab commit undo karna ho aur changes dobara commit karne hon.

---

## Mixed

```powershell
git reset --mixed HEAD~1
```

Result:

```text
commit ❌
changes ✅
staged ❌
```

`--mixed` default mode hai.

---

## Hard ⚠️

```powershell
git reset --hard HEAD~1
```

Result:

```text
commit ❌
working changes ❌
```

Potentially uncommitted work lose ho sakta hai.

> **`--hard` ko soch samajh kar use karna.**

---

# 57. `git revert`

Old commit ko safely reverse karne ke liye:

```powershell
git revert <commit-id>
```

Ye old commit delete nahi karta.

Example:

```text
A → B → C
```

Revert C:

```text
A → B → C → D
```

`D` ek new commit hota hai jo C ke changes ko reverse karta hai.

### Best use

Shared/pushed history mein generally safer.

---

# 58. Restore vs Reset vs Revert

Ye **must-remember** table hai:

| Command   | Main purpose                               |
| --------- | ------------------------------------------ |
| `restore` | File changes undo                          |
| `reset`   | Local commit/history/staging move          |
| `revert`  | Commit ko reverse karne ke liye new commit |

### Reset modes

```text
soft  = commit undo, changes staged
mixed = commit undo, changes unstaged
hard  = commit + working changes discard
```

---

# 59. Git ka complete daily workflow

### Normal project work

```text
git status
   ↓
edit code
   ↓
git diff
   ↓
git add .
   ↓
git commit -m "message"
   ↓
git push
```

### GitHub se update lena

```text
git pull
```

### New project clone

```text
git clone URL
```

### Feature work

```text
git switch -c feature-name
   ↓
code
   ↓
add
   ↓
commit
   ↓
push
   ↓
PR
   ↓
merge
```

---

# 60. Git command memory map

Tumhe **sab commands ratne ki zarurat nahi**.

Ye core map yaad rakho:

```text
STATUS  = kya ho raha hai?
DIFF    = kya change hua?
ADD     = staging mein dalo
COMMIT  = local history mein save
PUSH    = GitHub par bhejo
PULL    = GitHub se lao
CLONE   = new local copy banao
BRANCH  = separate line banao
SWITCH  = branch badlo
MERGE   = branches combine karo
PR      = GitHub par merge request
RESTORE = file change undo
RESET   = local history peeche
REVERT  = old commit reverse
```

---

# 🧠 Tumhari Python Logic Revision

Ye section specially important hai.

### Pattern 1 — Total

```python
total = 0

for n in numbers:
    total += n
```

### Pattern 2 — Count

```python
count = 0

for n in numbers:
    if condition:
        count += 1
```

### Pattern 3 — Filter

```python
result = []

for n in numbers:
    if condition:
        result.append(n)
```

### Pattern 4 — Find

```python
for n in numbers:
    if n == target:
        print("Found")
```

### Pattern 5 — Maximum

```python
maximum = numbers[0]

for n in numbers:
    if n > maximum:
        maximum = n
```

Ye patterns tumhari future ML/programming logic ke liye bohot useful hain.

---

# 🎯 Current Course Position

### ✅ Git/GitHub Milestone

**Complete**

```text
Git basics              ✅
GitHub                  ✅
Push/Pull               ✅
Clone                   ✅
Branch                  ✅
Merge                   ✅
Conflict                ✅
Pull Request            ✅
Restore                 ✅
Reset                   ✅
Revert                  ✅
```

### Python

**Foundation covered; next focus should be revision + logic + practical mini-projects**, phir NumPy/Pandas/SQL aur uske baad ML.

---

## ⭐ Final 10 commands to remember first

Agar sab bhool bhi jao, ye pehle yaad rakhna:

```powershell
git status
git diff
git add .
git commit -m "message"
git push
git pull
git clone <URL>
git branch
git switch <branch>
git merge <branch>
```

Baaki commands zarurat par notes se dekh sakte ho. **Professional skill ka matlab har command memorize karna nahi; situation dekh kar sahi command identify karna hai.**

Ye notes tumhare **Python + Git/GitHub milestone** ka consolidated reference hain.
