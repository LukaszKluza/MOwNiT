05.03.2024 Łukasz Kluza 
„Laboratorium” 01

## Arytmetyka Komputerowa

#### Treści zadań 

**_Zadanie 1._**
Znaleźć _"maszynowe epsilon"_, czyli najmniejszą liczbę _a_, taką że _a_+1>1

**_Zadanie 2._**

Rozważamy problem ewaluacji funkcji sin(x), m.in. propagację błędu danych wejściowych, tj. błąd wartości funkcji ze względu na zakłócenie h w argumencie x:

- Ocenić błąd bezwzględny przy ewaluacji sin(x)

- Ocenić błąd względny przy ewaluacji sin(x)
  
- Ocenić uwarunkowanie dla tego problemu

- Dla jakich wartości argumentu x problem jest bardzo czuły ?

**_Zadanie 3._**

Funkcja sinus zadana jest nieskończonym ciągiem

$$
    sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots
$$

- Jakie są błędy progresywny i wsteczny jeśli przybliżamy funkcję sinus biorąc tylko pierwszy człon rozwinięcią, tj.sin(x) ≈ x, dla x = 0.1, 0.5 i 1.0 ?

- Jakie są błędy progresywny i wsteczny jeśli przybliżamy funkcję sinus biorąc pierwsze dwa człony rozwinięcią, tj.sin(x) ≈ x - x^3/6, dla x = 0.1, 0.5 i 1.0 ?

**_Zadanie 4._**

Zakładamy że mamy znormalizowany system zmiennoprzecinkowy z β = 10, p = 3, L = -98

- Jaka jest wartość poziomu UFL (underflow) dla takiego systemu ?

- Jeśli x = 6.87 x 10^(-97) i y = 6.81 x 10^(-97), jaki jest wynik operacji x – y ?

#### Rozwiązania

**_Zadanie 1._**
Dla przykładu w języku programowanie python łatow możemy sprawdzć ile wynosi _"maszynowe epsilon"_:
```python
print(sys.float_info.epsilon )
#2.220446049250313e-16
```

**_Zadanie 2._**

- Błąd względny
$$
\Delta f(x) =  \lvert sinx \cdot (1+\epsilon) - sin(x)\rvert
$$

- Błąd bezwzględny 
$$
\frac{\Delta f(x)}{x} = \lvert \frac{sinx \cdot (1+\epsilon) - sin(x)}{x} \rvert
$$

**_Zadanie 3._**

Wartość na wartość _sin(x)_ wyprowadzony za pomocą wzoru _Taylora_

$$
    sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots
$$


__Wzory__:
y = f(x), gdzie \( f: \mathbb{R} \rightarrow \mathbb{R} \)
Błąd progresywny: \( \Delta = |\hat{y} - y| \)
Błąd wsteczny: \( \Delta = |\hat{x} - x| \)


- Błąd progresywny i wsteczny dla przybliżonego wzorem: _sin(x) ≈ x_ gdzie x = 0.1, 0.5 i 1.0.

\(y = sin(x)\)
\(\hat{y} = x, \hat{x} = arcsin(\hat{y})\)
Błąd progresywny: \( \Delta = |\hat{y} - y| = |x-sin(x)| \)
Błąd wsteczny: \( \Delta = |\hat{x} - x| = |arcsin(\hat{x})-x| \)


| Wyniki/Dane |__\(\hat{y}\)__| __\(\hat{x} = arcsin(x)\)__ | __\(sin(x)\)__ |Błąd progresywny | Błąd wsteczny |
|:-----------:|:-------------:|:---------------------------:|:--------------:|:---------------:|:-------------:|
|  _x=0.1_    |     _0.1_     |  \(arcsin(0.1)=0.1001674\)  |  0.0998334     |    0.0001666    |   0.0001674   |
|  _x=0.5_    |     _0.5_     |  \(arcsin(0.5)=0.5235987\)  |  0.4794255     |    0.0205745    |   0.0235987   |
|  _x=1.0_    |     _1.0_     |  \(arcsin(1.0)=1.5707963\)  |  0.8414709     |    0.1585291    |   0.5707963   |


- Błąd progresywny i wsteczny dla przybliżonego wzorem: _sin(x) ≈ x_ gdzie x = 0.1, 0.5 i 1.0.

\(y = sin(x)\)
\(\hat{y} = x, \hat{x} = arcsin(\hat{y})\)
Błąd progresywny: \( \Delta = |\hat{y} - y| = |x-sin(x)| \)
Błąd wsteczny: \( \Delta = |\hat{x} - x| = |arcsin(\hat{x})-x| \)


| Wyniki/Dane |__\(\hat{y}\)__| __\(\hat{x} = arcsin(x)\)__ | __\(sin(x)\)__ |Błąd progresywny | Błąd wsteczny |
|:-----------:|:-------------:|:---------------------------:|:--------------:|:---------------:|:-------------:|
|  _x=0.1_    |     _0.1_     |  \(arcsin(0.1)=0.1001674\)  |  0.0998334     |    0.0001666    |   0.0001674   |
|  _x=0.5_    |     _0.5_     |  \(arcsin(0.5)=0.5235987\)  |  0.4794255     |    0.0205745    |   0.0235987   |
|  _x=1.0_    |     _1.0_     |  \(arcsin(1.0)=1.5707963\)  |  0.8414709     |    0.1585291    |   0.5707963   |




