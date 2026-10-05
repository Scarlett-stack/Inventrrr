# Style implementations log file

## TODOS

- [x] TODO 1.1: Customize welcome page and add butons to redirect to display and add product
- [x] TODO 1.2: Refactor size, fit banner, adjust upper navbar menu
- [] TDOO 2: Customize and add a login page 
- [] TODO 3: Implement dark mode toggle
- [] TODO 3.1: Implement icons for navbar menu items
- [] TODO 4: Customize product listing table 
- [] TODO 5: Customize product add page
- [] TODO 6: Implement scroll menu for cards in home page

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

Vom folosi `--save-dev` pentru a instala doar in development. Va fi deja inclus in productie. NU INSTALA NICIODATA IN PRODUCTIE

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


### LOG 30 SEPTEMBRIE

- am reusit sa facem mai mica poza: se poate seta direct cu css niste dimensiuni sau poti cu procent eu am folosit dimensiuni
https://stackoverflow.com/questions/2233076/how-to-resize-an-image-in-pure-html-css-while-keeping-its-proportions


### LOG 4 OCTOMBRIE

- am schimbat dimensiunile imaginii in procente pentru ca aparent toata lume ape stack overflow asa face
- problema noua: imi pune aiurea butoanele alea cu link din meniu. Si inainte facea asa dar le impingea efectiv sub. Acuma se suprapune cu imaginea
- Da, este o problema de viewport: adica partea de ecran care se afseaza curent. In exemplele cu bulma nu exista sectiune de head acolo, unde dai instructiuni pt afisare si chestii de chars si alte cacaturi https://developer.mozilla.org/en-US/docs/Glossary/Layout_viewport

- Ok deci am scos div intermediar de dianinte de img (cel din a>) si am bagat stilul direct in tagul de imagine. 
- Ce a rrezolvat problema a fost faptul ca am importat componenta navbar din bulma in fisierul .scss 

- Am importat `helpers` (@use "../../node_modules/bulma/sass/helpers";) si a rezzolvat problema cu centrarea body-ului hero. 
- Inca am butoanele prea in dreapta la meniul de sus
- Si nu am linia separatoar intre navbar si body (banuies ca trb imprtate alea di  grid?)
- Pentru stilat am gasit chestia asta: https://www.testmuai.com/blog/bulma-css-framework/ (de asemenea gemini halucineaza si inventeaza componente de stil care nu exista)
- O sa folosim sections in loc de containers a ca nu prea inteleg ce se intampla acolo: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section
- Ideea e ca trb sa aiba un header astea idk
- SI organizate pe columns !! https://bulma.io/documentation/columns/ si cards: https://bulma.io/documentation/components/card/
- mda nush arata oribil si nu se incadreaza bine butoanele facem cu card

Tip de componentă,max-width recomandat,Motivație
Carduri de acțiuni / Pop-up-uri simple,380px – 420px,"Compact, ideal pentru 2 butoane sau un mesaj rapid."
Formulare de Login / Register,400px – 480px,Spațiu perfect pentru input-uri de text și etichete (labels).
Formulare complexe (Add Product),600px – 700px,Oferă loc pentru 2 coloane de input-uri (ex: Nume
Tabele de date / Dashboard,960px – 1200px,Necesită lățime mare pentru coloane multiple.


- smeckeria cu 0 auto: https://stackoverflow.com/questions/3170772/what-does-auto-do-in-margin-0-auto

- SPACING HELPERS FOARTE IMPORTANT SE APLICA PENTRU ELEMENTUL CURENT: https://bulma.io/documentation/helpers/spacing-helpers/

Cum facem sa bagam un meniul scrolling in centru cu cardurile alea?

Deci putem sa ne folosim de scrollul implicit al paginii: Columns Responsiveness: Bulma Column Layouts

Cum le grupezi: Pui un wrapper `<div class="columns is-multiline is-centered">`, iar fiecare card stă într-un `<div class="column is-4">` . Cica pe tel se face stacking cu fiecare card.
Sau:
Le bagi pe toate intrun container si trbs a permiti overflow: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow

- Am schimbat theme in ceva mai light problema e ca hoverul implicit e light si nu se vede cum trebuie
- E timpul s amodificam variabile sass!! Mergem in fisierul scss. Putem sa le punem si inainte si dupa dar eu o sa le pun dupa. I de aici de jos: https://bulma.io/documentation/components/navbar/

Sa ma bata mama ca nici nu s0-au deranjat sa puna toat ealea le-am gasit aici: https://www.geeksforgeeks.org/css/bulma-navbar-variables/
Sinataxa e asa: `$property-name: property-value;`

- Nevermind aparent s-a updatat cacatul asta si nu merge decat cu with nu mai merge a adefinesti tu separat vezi aici: https://bulma.io/documentation/customize/with-sass/

- Deci ce inseamna `!important` ? Practic ii spui browserului sa ignore orice alta regula de oriunde altundeva care ar mai exista pe elementul ala si sa foloseasc ace ai definit tu. Altfel s-ar lua in ordine si s-ar aplica ultima!

- O SA FOLOSIM DOAR METODA DE VARIABILE CSS NU SCSS PENTRU CA E MAI USOR ASA DE GASIT: https://bulma.io/documentation/features/css-variables/

Este o metoda standard in css: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties

- De ce zic a e mai usor? Tocmai am cautat hover in fisierul sursa de navbar si am gasit ceva dubios cu delta si cum calculeaza bulma luminosiztatea nu vrei asa ceva crede-ma.

