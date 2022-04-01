# Rezerva programarea la pasapoarte

Cateodata ne grabim sa prindem un loc la serviciul de pasapoarte. Din pacate, multa lume se programeaza de pe 2-3 adrese de mail pentru a avea *backup*, iar cei care au cu adevarat nevoie nu apuca un loc

# Cum se foloseste

Ai nevoie de Python 3+. Inlocuieste "iasiID" cu ID-ul localitatii in care vrei sa te programezi. 
Pentru a afla acest ID, deschide developer tools in browser, intra pe epasapoarte.ro, alege "Pasaport simplu electronic" si alege o localitate.
In tab-ul Network vei vedea ID-ul de care ai nevoie: https://monosnap.com/file/o9Bzjot77IQkcXIAubUkup8a9DOA4X

Inlocuieste `wantedDate = datetime.strptime("2022-06-10T00:00:00", '%Y-%m-%dT%H:%M:%S') `cu data inaintea careia ai nevoie de programare (data maxima) si ruleaza scriptul.

Lasa-l sa mearga si, la un moment dat, va incepe sa iti vorbeasca in boxe/casti "Found a sloooot", indicand faptul ca este o data disponibila in localitatea aleasa de tine si mai mica decat data maxima pe care ai introdus-o.
