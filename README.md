# Inventrrr

### Type hinting aka sagetica de la functii care mananca ficateii

https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
- pentru a activa strict mode la pylance am mers in ctlr shgt p -> setari -> extensions -> pylance -> scroll la alea cu emoji cu bifa.


### LOG 29 IULIE ORA 16:10 
- am ajuns l afaza in care enecesar sainstalam postgres
- nu am sa fac asta pe laptopul vechi


### PLSQL triggers

https://www.geeksforgeeks.org/plsql/plsql-triggers/


```
CREATE OR REPLACE TRIGGER trigger_name


BEFORE or AFTER or INSTEAD OF                      //trigger timings 


INSERT  or UPDATE or  DELETE                          // Operation to be performed 


of column_name


on Table_name


FOR EACH ROW


DECLARE


Declaration section


BEGIN


Execution section


EXCEPTION


Exception section


END;



/


Query operation to be performed i.e INSERT,DELETE,UPDATE.
```

- update nu am mai folosit plsql triggere folosesc events din alchemy 
- pentru a evita scurgerea secretelor folosim decouple : https://www.geeksforgeeks.org/python/how-to-hide-sensitive-credentials-using-python/
- pentru port avem: `sudo netstat -tulpn | grep postgres`


## Log 5 August 2026

- avem nevoie de un folder static pentru css pentru ca ai nevoie de el automat din cauza lui flask
- la fel si templtes, flask intra automat in ele

Putem folosi clase html in loc de nth child:

```
<!-- În HTML -->
<th scope="col" class="text-right">Brand</th>
<th scope="col" class="text-right">Price</th>

/* În CSS */
.text-right {
    text-align: end;
}
```

In legatura cu unitatile de masura: `px` si `rem` sau `em`: rem e root em e relativ la dimensiunea de baza a fontului din broswe (ce ai definit in `<html\`). Implicit e 16 px.
<br>
0.25 rem = 0.25 * 16 = 4px <br>

ESTE MULT MAI FLEXIBIL DACA UN USER VREA SA FACA ZOOM!
Prima valoare e pe axa verticala si cea de a doua e pe axa orizontala.

### Log 9 August 2026

- [] TODO: FORMS pt insput la add product ca sa pot testa ca lumea tabelul

Update: facem cu forms dar separat intr-o clasa specifica de add product. Importam acea clasa in app.py. Evitam atacurile csrf folosind protectia built in a lui flask wtf

- **Documentatie flask wtf forms**: [link](https://flask-wtf.readthedocs.io/en/1.2.x/quickstart/#creating-forms)

- **PENTRU CSS SIMPLU FOLOSIM PURE FORMS** (link)[https://pure-css.github.io/forms/]

- pentru autoomplete : (link)[https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete]



