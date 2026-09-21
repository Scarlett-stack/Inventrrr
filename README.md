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

- [x] TODO: FORMS pt insput la add product ca sa pot testa ca lumea tabelul

Update: facem cu forms dar separat intr-o clasa specifica de add product. Importam acea clasa in app.py. Evitam atacurile csrf folosind protectia built in a lui flask wtf

- **Documentatie flask wtf forms**: [link](https://flask-wtf.readthedocs.io/en/1.2.x/quickstart/#creating-forms)

- **PENTRU CSS SIMPLU FOLOSIM PURE FORMS** (link)[https://pure-css.github.io/forms/]

- pentru autoomplete : (link)[https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete]

- `pip freeze > requirements.txt` pentru a evits dependncy hell



- tu ai folosit instante de tip db.Model (mostenitori ai acestei superclase). SE FAC ALTFEL INTEROGARILE (mai exact fara .c ca sa acesezi metodele pt coloane) fata de tipul db.Table. (documentatie)[https://flask-sqlalchemy.readthedocs.io/en/stable/models/]

**UPDATE**:

https://docs.sqlalchemy.org/en/20/tutorial/metadata.html

DIN PACATE SAU FERICIRE DB.MODEL CONTINE SI DB.TABLE (VEZI LINKUL DE MAI SUS):

<P>The `Table` is constructed programmatically, either directly by using the `Table` constructor, or indirectly by using ORM Mapped classes (described later at Using ORM Declarative Forms to Define Table Metadata). There is also the option to load some or all table information from an existing database, called reflection.</P> https://www.reddit.com/r/flask/comments/10zd6kw/dont_understand_what_the_c_represents_in_this/


- Ce este un request in flask: [link](https://data-flair.training/blogs/flask-request-object/)

Pe noi ne intereseaza for now doar astea:

```
request.method
request.headers
request.args
request.form
request.cookies
```

Documentatie full [durere de cap](https://flask.palletsprojects.com/en/stable/api/#flask.Request)

- onlcikc javascript: https://stackoverflow.com/questions/4952459/javascript-alert-box-with-confirm-on-button-press


### Log 21 Septembrie

- Incercam sa facem todo cu submit la enter adica ala de edit product server side din tabel.
- O sa evit javascript -- [alternativa](https://stackoverflow.com/questions/27807853/html5-how-to-make-a-form-submit-after-pressing-enter-at-any-of-the-text-inputs)\

- display: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display pentru inline forms

- de asemenea trebuie inceput un fisier de log serios pentru ca nu are ce cauta toata tarasenia asta in readme.

- de ce avem nevoie de clasa din styel.css form-inline-inpiut? Pentru ca tabeleul respectiv nu e doar un formular e si un tabel normal deci daca nu selectez casuta respectiva nu are sens sa o fac formular.

- Tipul statementiurilor este fix actiunea lor vezi aici: https://docs.sqlalchemy.org/en/21/tutorial/data_update.html


- TUTORIAL STILARE TABEL CSS: https://piccalil.li/blog/styling-tables-the-modern-css-way/

INPUT FORM INSIPRATIE: https://zetcode.com/selenium/flask-submit-form/

