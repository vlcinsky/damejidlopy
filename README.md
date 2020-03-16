# Damejidlopy

Python Library for ordering food from site: Dáme Jídlo

## Installation


## How to use

First we need to create class which stores info about customer:

```python
>>> cust = Customer("name", "surname", "email", "address")
Name: name, Surname: surname, Email: email, Address: address
```

Next we need to search for restaurants in area:

```python
>>> searched = search(cust)
```

Now we can find hole menu from restaurant. 
Pass the chosen restaurant as a argument

```python
>>> restaurant1 = menu(searched, 13)
```

## WORK IN PROGRESS
