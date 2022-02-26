#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now();
    int coins_flipped = 0;
    while (coins_flipped < 1000000000) {
        // duration_cast<seconds>(high_resolution_clock::now() - start).count() < 5
        rand();
        coins_flipped++;
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << coins_flipped << endl;
    cout << duration.count() << endl;
    return 0;
}