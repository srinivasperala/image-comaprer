# image-comaprer
python script used to compare images

moduł do python3, służący do porównywania obrazków, wyświetlania ich podobieństw i listowania


przykłady użycia:

####porównanie dwóch obrazków
Sposób użycia:
```
python3 szperacz.py <img1> <img2>
```
  
####przeszukanie dogłebne podaniej ścieżki w poszukiwaniu doplikatów, podmianie ich i wypisaniu ich w logach
Sposób użycia:
```
python3 szperacz.py <wzór_do_porównania> <obrazek_do_podmiany> <ścieżka_przeszukiwania> <plik_do_logów> <minimalny_%_porównania>
```
Przykład:
```
python3 szperacz.py wzór.jpg nowy.png /media/user.dzp-c.ap.lan/ log_file.txt 91
```
  
####przeszukanie dogłebne podaniej ścieżki w celu znalezienia u wypisania duplikatów
Sposób użycia:
```
python3 poszukiwacz.py <wzór_do_porównania> <ścieżka_przeszukiwania> <plik_do_logów> <minimalny_%_podobieństwa>
```
Przykład:
```
python3 szperacz.py wzór.jpg /media/user.dzp-c.ap.lan/ log_file.txt 80
```
