# Beatbox

Konstrukcja katalogu: 

   beatbox.py     # glówna "aplikacja"

   readme.txt     # dodatkowe informacje o programie (m.in. opis plików, rozszerzen itp.)

   innymodul1.py  # dodatkowy modul, nazwa dowolna
   ...
   innymodulN.py  # dodatkowy modul, nazwa dowolna (musza byc co najmniej 2 dodatkowo)

   utworX/         # katalog, nazwa dowolna, definicja utworu
       sample01.wav # plik .wav, nazwa sampleUV.wav, gdzie UV to 2 cyfry
       ...
       sampleXY.wav # jw.

       track01.txt  # definicja sciezki 01, nazwa trackUV, gdzie UV to 2 cyfry
       ...
       trackAB.txt  # jw.

       defs.txt     # konfiguracja (m.in. bpm, zobacz nizej)

       song.txt     # okresla kolejnosc odgrywanych sciezek (zob. nizej)

W folderze utworX znajduja sie sciezki, sample, definicja i kolejnosc sciezek w utworze. 
Sample sa w formacie Wav.

Wygenerowanie utworu  z katalogu utworX odbywa sie nsatepujaco:

1. Wpisujemy w konsoli: ./beatbox.py 'utworX/'
2. klikamy ENTER
3. W folderze utworX pojawil sie nowy plik muzyczny w formacie wav o nazwie utworX.wav

Wygenerowane pliki:
utwor1 - "Szla dzieweczka do laseczka" - zmiksowany utwór
utwor2 - "Gdybym mial gitare..."  - zmiksowany utwór
utwor3 - zmiksowany utwór