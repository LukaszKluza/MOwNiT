Łukasz Kluza, 12.03.2024
„Laboratorium” 02

## Arytmetyka Komputerowa (cd.)

#### Treści zadań 

**_Zadanie 1._**
Napisać algorytm do obliczenia funkcji wykładniczej \(e^x\) przy pomocy nieskończonych szeregów
\(e^x= 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \)

 
- (1a) Wykonując sumowanie w naturalnej kolejności, jakie kryterium zakończenia obliczeń przyjmiesz ?


- (1b) Proszę przetestować algorytm dla: \(x= \pm 1, \pm 5, \pm 10\) i porównać wyniki z wynikami wykonania standardowej funkcji _exp(x)_

- (1c) Czy można posłużyć się szeregami w tej postaci do uzyskania dokładnych wyników dla _x < 0_ ?

- (1d) Czy możesz zmienić wygląd szeregu lub w jakiś sposób przegrupować składowe żeby uzyskać dokładniejsze wyniki dla _x < 0_ ?

**_Zadanie 2._** 
Które z dwóch matematycznie ekwiwalentnych wyrażeń \(x^2 - y^2\) oraz \((x - y)\cdot (x + y)\) może być obliczone dokładniej w arytmetyce zmienno-przecinkowej i dlaczego?

Dla jakich wartości _x_ i _y_, względem siebie, istnieje wyraźna różnica w dokładności dwóch wyrażeń ?

**_Zadanie 3._**
Zakładamy że rozwiązujemy równanie kwadratowe \(ax^2 + bx + c = 0,  a = 1.22, b = 3.34 i c = 2.28 \), wykorzystując znormalizowany system zmienno-przecinkowy z podstawa _beta = 10_ i dokładnością _p = 3_.

- (a) ile wyniesie obliczona wartość \(b^2 - 4ac\)?

- (b) jaka jest dokładna wartość wyróżnika w rzeczywistej (dokładnej) arytmetyce?

- (c) jaki jest względny błąd w obliczonej wartości wyróżnika?

#### Rozwiązania
**_Zadanie 1._**
**_Zadanie 2._**
**_Zadanie 3._**

\(f(x) = 1.22x^2 + 3.34x + 2.28 = 0,\)

- (a)
- (b) Rzeczywista wartość wyróżnika:
  \(\Delta = b^2 - 4ac = 3.34^2 -4 \cdot 1.22 \cdot 2.28 = 11.1556 - 11.1264 = 0.0292 \)
- (c)