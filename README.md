# Cifrado2

Este proyecto contiene una interfaz grafica en Python (Tkinter) que ejecuta 
algoritmos implementados en C++. Se incluyen cuatro programas sencillos:

- `cifrado_cesar.cpp`
- `cifrado_vigenere.cpp`
- `busqueda_lineal.cpp`
- `round_robin.cpp`

Cada archivo puede compilarse en un ejecutable `.exe` con `g++` de la siguiente
forma:

```
 g++ cifrado_cesar.cpp -o cifrado_cesar.exe
 g++ cifrado_vigenere.cpp -o cifrado_vigenere.exe
 g++ busqueda_lineal.cpp -o busqueda_lineal.exe
 g++ round_robin.cpp -o round_robin.exe
```

Luego ejecute `python3 interfaz.py` para abrir la interfaz.
