// cifrado_cesar.cpp
// Compilacion: g++ cifrado_cesar.cpp -o cifrado_cesar.exe
#include <iostream>
#include <string>

char cifrar_letra(char c, int clave) {
    if ('a' <= c && c <= 'z') {
        return 'a' + (c - 'a' + clave) % 26;
    } else if ('A' <= c && c <= 'Z') {
        return 'A' + (c - 'A' + clave) % 26;
    }
    return c;
}

int main() {
    int clave;
    std::string texto;
    if (!(std::cin >> clave)) return 0;
    std::cin.ignore();
    std::getline(std::cin, texto);
    int ajuste = ((clave % 26) + 26) % 26; // manejar claves negativas
    for (char &c : texto) {
        c = cifrar_letra(c, ajuste);
    }
    std::cout << texto << std::endl;
    return 0;
}
