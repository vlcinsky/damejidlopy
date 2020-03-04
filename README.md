# Damejidlopy

Knihovna k objednání jídla z portálu Dáme jídlo

## Návod k použití

Prvně musíme udělat třídu která bude obsahovat údaje o zákazníkovi:

```
trida = Customer("jmeno", "prijmeni", "email", "adresa")
```

Náslědně je nutno vyhledat restaurace v okolí zakáznika:
```
hledani = search(trida)
```

