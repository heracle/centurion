# centurion

Joc de tip "probots" sau "crobots".
In acest joc, pe un camp de lupta se bat mai multe tancuri; tancurile nu
 sunt controlate direct de jucatori, ci actioneaza pe baza unor programe de
 inteligenta artificiala scrise in prealabil de jucatori; practic, in
 prealabil, fiecare jucator scrie un program de inteligenta artificiala
 (sub forma unui fisier sursa text scris intr-un limbaj definit special in
 acest scop), apoi din meniul jocului se incarca aceste fisiere si se
 asociaza fiecare cate unui tanc, apoi se declansaza lupta; lupta
 propriuzisa poate fi urmarita pe ecran, dar jucatorii nu mai pot interveni
 asupra tancurilor - ele actioneaza autonom, pe baza programului asociat;
 evident, va castiga (supravietui) tancul cu programul cel mai bun.
Jocul va implementa facilitatile:
 - limbajul in care vor fi programate tancurile va contine cel putin:
  * structuri de control de tip if, while, sau macar instructiuni de salt
     conditionat (if) si neconditionat (goto) la etichete;
  * instructiuni de calcul aritmetic cu numere reale;
  * instructiuni specifice de actionat facilitatile tancurilor (tun,
     deplasare, etc.) si de consultat tabla (pentru a detecta obstacole,
     tancuri inamice, etc.);
  * posibilitatea de a defini variabile reale proprii (eventual vectori si
     matrici de reali);
 - rularea programelor asociate tancurilor se va face in paralel
  (intretesut), a.i. un tanc poate pierde nu numai daca algoritmul sau
  este mai slab ci si daca operatiile pe care le face sunt prea complexe si
  necesita timp de calcul mai lung - pana se va "gandi" ce trebuie sa faca
  inamicul va pleca din pozitia in care a fost detectat sau il va distruge;
 - tancurile vor putea fi configurabile - jucatorul va putea specifica
  (din meniul jocului) ce facilitati sa aibe tancurile (tun, mitraliera,
  rachete, radar, etc.) iar limbajul de programare va permite utilizarea
  acestora (prin instructiuni specifice); fiecare facilitate va avea un
  cost si avantaje/dezavantaje, a.i. jucatorii sa nu poata sau sa nu fie
  interesati sa opteze mereu pentru toate facilitatile la un loc;
 - fiecare tip de arma va avea puteri distructive diferite, iar tancurile
  vor avea un nivel de "sanatate" care se va diminua cu fiecare lovitura
  primita; cand ajunge la 0 tancul explodeaza si este distrus;
 - se va putea juca pe echipe: din meniul jocului se va putea specifica
  numarul de echipe si numarul de tancuri din fiecare echipa; limbajul de
  programare va permite recunoasterea si distingerea tancurilor din aceeasi
  echipa de cele adverse; fiecare tanc insa va avea programul lui;
 - grafica jocului va fi cat mai frumoasa, permitand cel putin:
  * afisarea tancurilor si a unor elemente de decor - unele distructibile,
     altele nu;
  * distingerea grafica a facilitatilor (tun, mitraliera, etc.) cu care
     este inzestrat fiecare tanc;
  * culori diferite pentru fiecare echipa; fiecare tanc va fi insotit de un
     text care permite identificarea jucatorului care l-a programat (textul
     va fi scris in programul asociat si luat de joc de acolo) si de un
     numar sau bara care indica nivelul curent de "sanatate";
  * proiectilele trase vor fi desenate in deplasarea lor; proiectilele trase
     de arme diferite (tun, racheta, etc.) vor fi desenate diferit;
  * explozii animate.
Indicatie: pe Internet exista programe similare, inclusiv sursa lor, si
 pot fi preluate parti din aceste surse.