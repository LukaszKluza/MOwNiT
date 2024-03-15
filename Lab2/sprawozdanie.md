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
Zakładamy że rozwiązujemy równanie kwadratowe \(ax^2 + bx + c = 0,  a = 1.22, b = 3.34 ,  c = 2.28 \), wykorzystując znormalizowany system zmienno-przecinkowy z podstawa _beta = 10_ i dokładnością _p = 3_.

- (a) ile wyniesie obliczona wartość \(b^2 - 4ac\)?

- (b) jaka jest dokładna wartość wyróżnika w rzeczywistej (dokładnej) arytmetyce?

- (c) jaki jest względny błąd w obliczonej wartości wyróżnika?

#### Rozwiązania
**_Zadanie 1._**

- Program do wyliczania wartości \(e^x\):
```python 
def e_to_x(x):
  e1, e2 = 0, 1
  iterator  = 1
  power = 1
  while e1 != e2:
      e1 = e2 
      e2 += (x**iterator)/power
      iterator += 1
      power *= iterator
  return e2    
```
Powyższy algorytm oblicza przybliżoną wartość wyrażenia \(e^x\) poprzez iteracyjne dodawanie kolejnych wyrazów szeregu Taylora dla funkcji \(e^x\), dopóki różnica \(|e1-e2|\) jest większa niż _epsilon maszynowy_ tj.  \(\Delta e > \epsilon \)

- Testowanie i porównanie algorytmu dla: \(x= \pm 1, \pm 5, \pm 10  \pm 100\) z wynikami standardowej funkcji _exp(x)_: 

```python
  X = [1,-1,5,-5,10,-10, 100,-100]
  for x in X:
    print(f"e^{x}: {e_to_x(x)}, exp: ({math.exp(x)}) difference: {math.fabs(e_to_x(x)-math.exp(x))}")
```
  
| \(x\) | e^x                     | Mathematical Value     | Difference             |
| ----- | ----------------------- | ---------------------- | ---------------------- |
| 1     | 2.7182818284590455      | 2.718281828459045      | 4.440892098500626e-16  |
| -1    | 0.36787944117144245     | 0.36787944117144233    | 1.1102230246251565e-16 |
| 5     | 148.41315910257657      | 148.4131591025766      | 2.842170943040401e-14  |
| -5    | 0.006737946999086907    | 0.006737946999085467   | 1.4398204850607499e-15 |
| 10    | 22026.46579480671       | 22026.465794806718     | 7.275957614183426e-12  |
| -10   | 4.5399929433607724e-05  | 4.5399929762484854e-05 | 3.2887713006472113e-13 |
| 100   | 2.6881171418161356e+43  | 2.6881171418161356e+43 | 0.0                    |
| -100  | -2.8756582514726483e+26 | 3.720075976020836e-44  | 2.8756582514726483e+26 |

Analizując powyższe dane zauważamy, że nasz algorytm całkiem dobrze radzi sobie z wyznaczamien wartośći \(e^x\) ale tylko w tedy kiedy \(x > 0\). Natomiast dla wartości ujemnych dokładność tego algorytmu jesty już dużo mniejsza, a nawet dla \(x = 100\) obserwujemy sprzeczności ponieważ \(\forall_{x} ~e^x > 0 \). 

- Aktualizacja algorytmu tak aby poprawić jego wydajność dla \(x < 0\).
Aby nasz algorytm działał porpawnie dla  \(x < 0\) to wystarczy zmienieć sposób jego wywołania zauważając, że \(e^{-x} = \frac{1}{e^x}\).

```python
  X_plus = [1,5,10,100]
  for x in X_plus:
    print(f"e^{x}: {e_to_x(x)}, exp: ({math.exp(x)}) difference: {math.fabs(e_to_x(x)-math.exp(x))}")
    print(f"e^{x}: {1/e_to_x(x)}, exp: ({math.exp(-x)}) difference: {math.fabs(1/e_to_x(x)-math.exp(-x))}")
```
| \(x\) | \(x^x\)                | Mathematical Value     | Difference             |
| ----- | ---------------------- | ---------------------- | ---------------------- |
| 1     | 2.7182818284590455     | 2.718281828459045      | 4.440892098500626e-16  |
| -1    | 0.3678794411714423     | 0.36787944117144233    | 5.551115123125783e-17  |
| 5     | 148.41315910257657     | 148.4131591025766      | 2.842170943040401e-14  |
| -5    | 0.006737946999085469   | 0.006737946999085467   | 1.734723475976807e-18  |
| 10    | 22026.46579480671      | 22026.465794806718     | 7.275957614183426e-12  |
| -10   | 4.539992976248486e-05  | 4.5399929762484854e-05 | 6.776263578034403e-21  |
| 100   | 2.6881171418161356e+43 | 2.6881171418161356e+43 | 0.0                    |
| -100  | 3.7200759760208356e-44 | 3.720075976020836e-44  | 4.9784122222889134e-60 |



**_Zadanie 2._**
**_Zadanie 3._**

\(f(x) = 1.22x^2 + 3.34x + 2.28 = 0,\)

- (a)
- (b) Rzeczywista wartość wyróżnika:
  \(\Delta = b^2 - 4ac = 3.34^2 -4 \cdot 1.22 \cdot 2.28 = 11.1556 - 11.1264 = 0.0292 \)
- (c)