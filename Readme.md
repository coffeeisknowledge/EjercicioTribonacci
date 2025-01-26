# Solucion y Explicacion

Una computadora comienza imprimiendo los números 2023, 2024 y 2025.
Luego continúa imprimiendo sin parar la suma de los últimos 3 números que imprimió: 6072, 10121, 18218, …

## Analisis

Como se puede observar, tenemos una serie similar a la de Fibonacci; con la diferencia que esta considera la suma de los tres terminos anteriores para obtener el siguiente. Por lo que podemos expresar la relacion de recurrencia para un termino en la posicion "n" de la siguiente manera:

$$
T_n = T_{n-1} + T_{n-2} + T_{n-3}
$$

> En donde el valor de "n" debe ser mayor a 3.

Lo que satisface los siguientes numeros de la posicion donde n es mayor que 3, ejemplo:

$$
10121_{t5} = 6072_{t4} + 2025_{t3} + 2024_{t2}
$$

Ahora, con el algebra lineal podemos representar de forma matricial esta relacion de recurrencia como:

$$
\begin{bmatrix}
T_{n} \\
T_{n-1} \\
T_{n-2}
\end{bmatrix} = 

\begin{bmatrix}
T_{n-1} + T_{n-2} + T_{n-3} \\
T_{n-1} \\
T_{n-2}
\end{bmatrix}
$$

Si observamos, nos damos cuenta que podemos expresar la matriz del lado derecho en forma de multiplicacion matricial:

$$
\begin{bmatrix}
T_{n} \\
T_{n-1} \\
T_{n-2}
\end{bmatrix} = 

\begin{bmatrix}
1 & 1 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}

*

\begin{bmatrix}
T_{n-1} \\
T_{n-2} \\
T_{n-3}
\end{bmatrix}
$$

Entonces si llamamos a esa nueva matriz "A", en donde:

$$
A =
\begin{bmatrix}
1 & 1 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
$$

Podemos ver que al multiplicar la matriz "A" con la otra matriz, se sigue cumpliendo con la ecuacion inicial, de modo que:

$$
\begin{bmatrix}
T_{n} \\
T_{n-1} \\
T_{n-2}
\end{bmatrix} = 

A
*

\begin{bmatrix}
T_{n-1} \\
T_{n-2} \\
T_{n-3}
\end{bmatrix}
$$

> Nota: Puede validar esta ecuacion reemplazando y resolviendo con los valores de "T" para cualquier elemento de nuestra serie, en donde el elemento "n" que vaya a evaluar sea mayor a 3. 

> Recuerda, "n" representa el valor de la posicion de un elemento en nuestra serie 2023, 2024, 2025, 6072, 10121...

Para este punto, podemos hacernos la siguiente pregunta ¿Que sucede con los 3 primeros elementos de nuestra secuencia? Claramente ellos sirven como condiciones iniciales para la relacion de recurrencia. Asi que debemos agregarlos a nuestra forma matricial ¿Pero como?

Si nos fijamos otra vez en nuestra ecuacion y la reemplazamos por valores de nuestra secuencia, podemos observar un patron:

> Ejemplo para el elemento de valor n = 6

$$
\begin{bmatrix}
18218 \\
10121 \\
6072
\end{bmatrix} = 

A
*

\begin{bmatrix}
10121 \\
6072 \\
2025
\end{bmatrix}
$$

Algo interesante sucede cuando aplicamos la formula otra vez en la matriz de la derecha:

$$
\begin{bmatrix}
10121 \\
6072 \\
2025
\end{bmatrix} =

A
*

\begin{bmatrix}
6072 \\
2025 \\
2024
\end{bmatrix}
$$

Y ahora reemplazamos esta nueva expresion en el ejemplo inicial:

$$
\begin{bmatrix}
18218 \\
10121 \\
6072
\end{bmatrix} = 

A
*

\begin{bmatrix}
10121 \\
6072 \\
2025
\end{bmatrix}
$$


$$
\begin{bmatrix}
18218 \\
10121 \\
6072
\end{bmatrix} = 

A
*
(
A
*

\begin{bmatrix}
6072 \\
2025 \\
2024
\end{bmatrix})
$$

Y si lo volvemos a aplicar:

$$
\begin{bmatrix}
6072 \\
2025 \\
2024
\end{bmatrix} = 

A
*

\begin{bmatrix}
2025 \\
2024 \\
2023
\end{bmatrix}
$$

$$
\begin{bmatrix}
18218 \\
10121 \\
6072
\end{bmatrix} = 

A
*

A
*

(A
*

\begin{bmatrix}
2025 \\
2024 \\
2023
\end{bmatrix})
$$

$$
\begin{bmatrix}
18218 \\
10121 \\
6072
\end{bmatrix} = 

A^3
*

\begin{bmatrix}
2025 \\
2024 \\
2023
\end{bmatrix}
$$

En este punto, podemos ver que ya no podemos reducir mas la matriz del lado derecho porque ya alcazamos los 3 valores iniciales de nuestra secuencia. Asimismo, observamos que la potencia para la matriz "A" es igual a:

$$
n-3; donde: n > 3
$$

> Esto se corrobora comparando la ecuacion con los valores de nuestra para n > 3.

Ya con esto, podemos establecer la siguiente formula general: 

$$
\begin{bmatrix}
T_{n} \\
T_{n-1} \\
T_{n-2}
\end{bmatrix} = 

A^{n-3}
*

\begin{bmatrix}
T_3 \\
T_2 \\
T_1
\end{bmatrix}
$$

En donde, para nuestro secuencia en especifico 2023, 2024, 2025...
$$
T_3 = 2025,
T_2 = 2024,
T_1 = 2021
$$
