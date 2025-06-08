// busqueda_lineal.cpp
// Compilacion: g++ busqueda_lineal.cpp -o busqueda_lineal.exe
#include <iostream>
#include <sstream>
#include <vector>

int main() {
    std::string linea;
    if (!std::getline(std::cin, linea)) return 0;
    std::stringstream ss(linea);
    std::vector<int> datos;
    int x;
    while (ss >> x) datos.push_back(x);

    int buscar;
    if (!(std::cin >> buscar)) return 0;

    int indice = -1;
    for (size_t i = 0; i < datos.size(); ++i) {
        if (datos[i] == buscar) {
            indice = static_cast<int>(i);
            break;
        }
    }
    std::cout << indice << std::endl;
    return 0;
}
