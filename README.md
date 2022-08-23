# Xplitter

Split your tabs, checks, or expenses very easily with Xplitter 😊

Xplitter makes calculating expenses between friends and family easily 🧮

Simply enter the people included in all tabs and the items you'd like to split. After doing so a **CSV excel/sheets file will be auto-generated** for viewing and extra custom calcuations!

## Installation

Recommended to use Python's Virtual Environment for easy installation.

```bash
python3 -m venv env
```

1. Activate venv
```bash
env\Scripts\activate
```
2. Install all packages needed:
```bash
pip install -r requirements.txt
```
## Usage
User-to-Command Line Interaction
```python
Xplitter> py .\main.py

Welcome to Xplitter
Who is money owed to?: Steven
Steven's Payday on (2022-08-23 11:56:38.698179)

Enter a payer's name | Type 'DONE' to proceed: John
Enter a payer's name | Type 'DONE' to proceed: Sally

.......

Enter a payer's name | Type 'DONE' to proceed: DONE
What is the item? | Type 'DONE' to proceed: Le Sia Crab Boil
What is Le Sia Crab Boil price? 34.99
WHO Le Sia Crab Boil?
1. John
2. Sally
3. Marvin
4. Candy
5. Steven
Enter 0 for all | For specific people enter number separated by white space: 0        

John owes $7.0!
Sally owes $7.0!
Marvin owes $7.0!
Candy owes $7.0!
Steven owes $7.0!
What is the item? | Type 'DONE' to proceed: Truffle Fries

.......

What is Shaved Ice price? 12.49
3. Marvin
4. Candy
5. Steven
Enter 0 for all | For specific people enter number seperated by white space: 3 4 5

Marvin owes $4.16!
Candy owes $4.16!
Steven owes $4.16!
...
What would you like to name your CSV file? aug_23_dinner
```

## CSV generator
![image](https://user-images.githubusercontent.com/33507449/186208238-0e9ece44-b8fc-4ea3-b50a-23f2e1804d23.png)
