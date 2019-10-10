# SPD - Exercici 3: Xifrat i índex de coincidència

**Autor:** Francesc Xavier Bullich Parra

## Métode de xifratge

[Veure fitxer funcions](https://github.com/fxbp/spd-ex3/blob/master/funcions.py)
[Veure fitxer xifrat](https://github.com/fxbp/spd-ex3/blob/master/xifrat.py)
[Veure fitxer desxifrat](https://github.com/fxbp/spd-ex3/blob/master/desxifrat.py)

He escollit la següent combinació de métodes de xifratge per realitzar l'exercici:

- Xifrat PlayFair com a xifrat per substitució
- Xifrat RailFence com a xifrat per transposició


Per xifrar els missatges primer aplico el xifrat playFair i un cop xifrat aplico la transposició amb RailFence. Obviament per desxifrar s'haurà d'aplicar el procès invers.

### Xifrat PlayFair

El xifrat PlayFair es un xifrat de substitució poligràfic per parelles de caràcters. Per tant cada cop que es fa una substitucio és fa per a 2 caràcters alhora. Donat que és poligràfic, el xifrat d'un càracter concret pot resultar en varis caracters diferents, segons la parella que l'acompanya.

El métode es el mateix que hi ha als apunts per el tema 3 però he modificat la mida de la taula a 6 x 6 per poder tenir en compte més simbols com l'espai el punt o la coma.

He tingut en compte les següents consideracions alhora d'aplicar el métode:

- L'alfabet, tant d'entrada com de sortida, son les lletres minúscules [a-z] més els simbols ' ', '.', ',', '?','!','$',':','(',')' i '-'
- La taula resultant es de 6 x 6
- Els primers caràcters de la taula son els de la clau sense repeticions, es completa la taula amb els caràcters vàlids restants.
- Per poder xifrar correctament s'ha de preprocessar el text. S'ha d'afegir un caràcter no important entre els parells de caràcters iguals. En el meu cas el caràcter es '$' que forma part de l'alfabet

Com s'ha vist a classe aquest xifrat intenta trencar el criptoanàlisi per taules de frequencia. Un fet important es que la taula de xifratge varia en funció de la clau. Per tant la clau juga un paper molt important alhora de mantenir la seguretat del xifratge.

Aquest fet és important, ja que si es dona per suposat que l'algoritme de xifrat pot ser conegut per els altres, la clau és l'unic impediment gran alhora de trencar el xifratge.

### Xifrat RailFence

Utilitzo el mateix xifrat de Railfence vist en l'exercici 1.

- L'alfabet, tant d'entrada com de sortida, son les lletres minúscules [a-z] més els simbols ' ', '.', ',', '?','!','$',':','(',')' i '-'
- El nombre de rails utilitzat és la mida de la clau proporcionada per el PlayFair.

Un cop més es veu la importancia de mantenir en secret la clau per desxifrar el missatge. Com ja s'ha comentat els algorimtes poden ser publics per tant les claus de xifrat jugen un paper molt important.

En els dos mètodes s'utilitza un sistema de clau simetrica.


## Exemples de xifratge

### Exemple de xifratge:

- clau: 'esunaprova'
- text: This is a little test. All text is in the same line. Testing, tested and test.
- fitxers:
  - Entrada: test1.txt
  - SortidaEncritptat: outTest1.txt
  - EntradaEncriptat: outTest1.txt
  - SortidaDesencriptat: dex1.txt

Taula 6x6 amb clau prova:
 ```
 'e', 's', 'u', 'n', 'a', 'p',
 'r', 'o', 'v', 'b', 'c', 'd',
 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'q', 't', 'w', 'x',
 'y', 'z', ' ', '.', ',', '?',
 '!', '$', ':', '(', ')', '-'
 ```

Proces xifrat-desxifrat:

```
python xifrat.py
Entra el nom del fitxer on hi ha el text clar: test1.txt
Entra el nom de fitxer on es guardarà el text xifrat: outTest1.txt
Entra la clau amb la que vols xifrar: esunaprova
ql..piynnhyqubgunguns,.nmm..burq.w,qqt.psh(.liqtmuumepuysn.zfwqysin(ut!.ul?l,mp.
Encryption finalized. Result in outTest1.txt

python desxifrat.py
Entra el nom del fitxer on hi ha el text xifrat: outTest1.txt
Entra el nom de fitxer on es guardarà el resultat de desxifrat: dex1.txt
Entra la clau amb la que vols desxifrar: esunaprova
this is a little test. all text is in the same line. testing, tested and test.
Decrytion finalized. Result in dex1.txt
```

Com és pot observar l'única diferència entre el xifrat i el desxifrat és que no conserva les majúscules.
Tampoc funcionaria si hi hagessin números.


### Exemple 2: text llarg en 1 sola linia:

- clau: 'tenimuntextmesllarg'
- text: Now for manners use has company believe parlors. Least nor party who wrote while did. Excuse formed as is agreed admire so on result parish. Put use set uncommonly announcing and travelling. Allowance sweetness direction to as necessary. Principle oh explained excellent do my suspected conveying in. Excellent you did therefore perfectly supposing described. Not him old music think his found enjoy merry. Listening acuteness dependent at or an. Apartments thoroughly unsatiable terminated sex how themselves. She are ten hours wrong walls stand early. Domestic perceive on an ladyship extended received do. Why jennings our whatever his learning gay perceive. Is against no he without subject. Bed connection unreserved preference partiality not unaffected. Years merit trees so think in hoped we as.

- fitxers:
  - Entrada: testLlarg.txt
  - SortidaEncritptat: outLlarg.txt
  - EntradaEncriptat: outLLarg.txt
  - SortidaDesencriptat: desLLarg.txt

Taula 6x6 amb clau prova:
```
't', 'e', 'n', 'i', 'm', 'u',
'x', 's', 'l', 'a', 'r', 'g',
'b', 'c', 'd', 'f', 'h', 'j',
'k', 'o', 'p', 'q', 'v', 'w',
'y', 'z', ' ', '.', ',', '?',
'!', '$', ':', '(', ')', '-'
```

Proces xifrat-desxifrat:

```
python xifrat.py
Entra el nom del fitxer on hi ha el text clar: testLlarg.txt
Entra el nom de fitxer on es guardarà el text xifrat: outLlarg.txt
Entra la clau amb la que vols xifrar: tenimuntextmesllarg
emkxtlenen:ftizgdsmmiaspsngelg elpccdqlgk?lpymfeneclelmzloosri:nfnxepnovn.s:?.ys:eszozfusplsnulntw?eo,nm,xxebaxms?dmzzae,nlnipmn,nyneciz?imzisdpcncmidlezem!yccy:pvenfcugemaztbnpahmclsxmx,,sssnoxe.:oex:nzq  jjzcasersa pzei:psbqiclbidivehpmjaal:qllmlltrvnl.ezfoes:dpnnmqtmtmeqvmpnuvnlpv:epplqkap,lg.allglimuo,,pcsb:fziiclsrknlpmn:,d.zt:zenz(iqszn.hrntsoezt:z:mondpn:.whyy?:oecli,cctn?um?repmzcn ep:lmgsedssece:ep ennmp,mspesmm.idnzblevgxfnm:?eazpr ipnig,anxnirecsrzzt,wlo?,seilmr:dllnrann:nsecdnebc..tinoljzmlaap:.zmmpemmlgiziz,qfhnxeeuoyefsosvzeucan.xne.:gl vlmnmbcscrpnnl., qzedllinca:mnsxp:w.is xrmss:mjliheusi(typgrslzccgv.,lpsis.znnnpz,cv?dnclilfzulscchcczm?ldnpnzzme .kzonst zoys.,nynfslz:ix.m?nvj,mi.ic?,resnzs)xrprspouiosfpuxineaozxp:zcixottnsb,,nnslybgp:eeasll:slnnhm,n)ellimzeidfu:r.elc ecdqcnelp::t.ans.xallezz:np
Encryption finalized. Result in outLlarg.txt

python desxifrat.py
Entra el nom del fitxer on hi ha el text xifrat: outLlarg.txt
Entra el nom de fitxer on es guardarà el resultat de desxifrat: desLlarg.txt
Entra la clau amb la que vols desxifrar: tenimuntextmesllarg
now for manners use has company believe parlors. least nor party who wrote while did. excuse formed as is agreed admire so on result parish. put use set uncommonly announcing and travelling. allowance sweetness direction to as necessary. principle oh explained excellent do my suspected conveying in. excellent you did therefore perfectly supposing described. not him old music think his found enjoy merry. listening acuteness dependent at or an. apartments thoroughly unsatiable terminated sex how themselves. she are ten hours wrong walls stand early. domestic perceive on an ladyship extended received do. why jennings our whatever his learning gay perceive. is against no he without subject. bed connection unreserved preference partiality not unaffected. years merit trees so think in hoped we as.-
Decrytion finalized. Result in desLlarg.txt
```



## Càlcul de l'índex de coincidència
