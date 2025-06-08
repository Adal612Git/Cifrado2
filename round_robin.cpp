// round_robin.cpp
// Compilacion: g++ round_robin.cpp -o round_robin.exe
#include <iostream>
#include <sstream>
#include <queue>
#include <vector>

struct Proceso {
    int id;
    int restante;
};

int main() {
    std::string linea;
    if (!std::getline(std::cin, linea)) return 0;
    std::stringstream ss(linea);
    std::vector<Proceso> procesos;
    int duracion;
    int id = 1;
    while (ss >> duracion) {
        procesos.push_back({id++, duracion});
    }
    int quantum;
    if (!(std::cin >> quantum)) return 0;

    std::queue<Proceso> cola;
    for (const auto &p : procesos) cola.push(p);

    std::vector<std::string> pasos;
    int tiempo = 0;
    while (!cola.empty()) {
        Proceso p = cola.front();
        cola.pop();
        int uso = std::min(p.restante, quantum);
        p.restante -= uso;
        tiempo += uso;
        std::ostringstream paso;
        paso << "P" << p.id << " ejecuta " << uso << " (t=" << tiempo << ")";
        pasos.push_back(paso.str());
        if (p.restante > 0) {
            cola.push(p);
        }
    }
    for (const auto &s : pasos) {
        std::cout << s << std::endl;
    }
    return 0;
}
