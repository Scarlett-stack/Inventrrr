# Style implementations log file

## TODOS

- [x] TODO 1.1: Customize welcome page and add butons to redirect to display and add product
- [] TODO 1.2: Refactor size, fit banner, adjust upper navbar menu
- [] TDOO 2: Customize and add a login page 
- [] TODO 3: Implement dark mode toggle
- [] TODO 4: Customize product listing table 
- [] TODO 5: Customize product add page

## LOGS

### 21 septembrie 2026

- daca face urat vscode sterge sau redenumeste directorul `mv ~/.config/Code ~/.config/Code.backup`. Acolo ai setari facute de user. Extensiile se gasesc in `.vscode/extensions`. Nu a fost necesar sa sterg `.vscode` deci extensiile sunt ok dar daca vrei sa restaurezi tema

```
cat ~/.config/Code.backup/User/settings.json
# la mine a fost "workbench.colorTheme": "Quiet Light"
```

<br> 
Apoi din **command palette** (Ctrl + Shift + P) selectezi `Preferences: Color Theme` si alegi ce vrei. Daca pui un fisier `settings.json` in directorul curent se va aplica DOAR pentru directorul curent deci nu si global.

Happy now?

#### Instalare node js + npm pentru bulma

- nu folosim cdn, cel mai smpli e sa aducem libraria la noi. Din ce am observat de pe dcumentatie nu par asa multe fisiere
https://nodejs.org/en/download


Ok deja incepem https://bulma.io/documentation/start/syntax/

 Bulma consists of elements and components defined in dozens of .scss files, that you can load individually with the @use keyword.


Tu lucrezi cu fisiere scss care importa prostii din libraria bulma. Alea trebuie compilate ca sa mearga ca css-uri.
https://stackoverflow.com/questions/71902017/in-what-way-can-we-compile-our-scss-or-sass-file-to-the-css-file


Al doilea e mai util: https://stackoverflow.com/questions/60602125/how-to-import-scss-files-into-html-files


### LOG 22 septembrie

Ok nu merge sass watch ala zice ca 

```
Compilation Error
Error: Can't find stylesheet to import.
  ╷
2 │ @use "bulma/sass/base";
  │ ^^^^^^^^^^^^^^^^^^^^^^
  ╵
  Inventrrr/static/scss/style.scss 2:1  root stylesheet
--------------------
Watching...
--------------------
```

Eu am instalat bulma dar naiba stie unde ca trebuie in radacina proiectului. De asemenea npm install are cateva optiuni la comanda care merita sa citesti despre ele [link](https://medium.com/@pkcibiyanna/understanding-save-vs-save-dev-in-npm-whats-the-difference-22e1ed0d5c3e).

Ideea e ca nu e bine s afolosest `-g` pentru ca instaleaza pachetul global in sistem -> portabilitate 0. Proiectele descarcate ar trb sa aiba requremnts in `package.json` ceea cu `-g` nu se intampla.

Vom folosi `--save-dev` pentru a instala doar in development. Va fi deja inclus in productie.

```
# IN FOLDERUL RADACINA PROIECTULUI!!!
npm install --save-dev sass
```

CACAT TREBUOE `PACKAGE.JSON`

Mda deci urmeaza de aici: https://docs.npmjs.com/using-npm-packages-in-your-projects 

DECI DECI, cand faci `npm install <>` el automat iti face un folder `node_modules` daca nu ai package.json in foldeul curent. POTI SA IL STERGI PUR SI SIMPLU SI SA REINSTALEZI 
Daca nu stii unde se afla: `npm root`.

Extensia nu e prea helpful pentru ca cauta node_modules langa static/scss/style.css

```
npm init

npm install bulma
npm install --save-dev sass
npx sass --watch static/scss/style.scss static/css/style.css
npx sass --load-path=node_modules --watch static/scss/style.scss static/css/style.css
```

Erau greseli in aboit.html, nu se pun ghilimele duble in interoiurl href sau rel sau whatever.

[CULORI BULMA](https://bulma.io/documentation/helpers/color-helpers/)
[CONTAINER BULMA](https://bulma.io/documentation/layout/container/)



The container is a simple utility element that allows you to center content on larger viewports. It can be used in any context, but mostly as a direct child of one of the following:

    navbar
    hero
    section
    footer



[LEVEL FOARTE MISTO](https://versions.bulma.io/0.7.0/documentation/layout/level/)
OK ASTA IL PUNEM LA PAGINA DE START SI AL ACU CASUTA DE CAUTARE IL PUNEM LA TABEL?

TEMPLATE GRATIS : https://versions.bulma.io/0.7.0/documentation/layout/hero/

NAVBAR: https://bulma.io/documentation/components/navbar/
