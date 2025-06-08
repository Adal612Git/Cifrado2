// cifrado_vigenere.cpp
// Compilacion: g++ cifrado_vigenere.cpp -o cifrado_vigenere.exe
#include <iostream>
#include <string>

int main() {
    std::string clave;
    std::string texto;
    if (!std::getline(std::cin, clave)) return 0;
    std::getline(std::cin, texto);
    std::string resultado;
    int n = clave.size();
    int j = 0;
    for (char c : texto) {
        if (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z')) {
            char base = ('a' <= c && c <= 'z') ? 'a' : 'A';
            char k = clave[j % n];
            int offset = ('a' <= k && k <= 'z') ? k - 'a' : ('A' <= k && k <= 'Z') ? k - 'A' : 0;
            resultado += static_cast<char>(base + (c - base + offset) % 26);
            j++;
        } else {
            resultado += c;
        }
    }
    std::cout << resultado << std::endl;
    return 0;
}
