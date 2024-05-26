#include <iostream>
#include <cstring>
#include <iomanip>
#include "hardware.h"

using namespace std;

HARDWARE_ITEM records[99];

void CreateEmptyDatabase(void) {
    int rec_num = 0;
    for (int i = 0; i < 100; i++) {
        rec_num++;
        records[i].record_num = rec_num;
    }
    FILE* fs = fopen("hardware.dat", "wb");
    fwrite(&records, sizeof(HARDWARE_ITEM), 100, fs);
    fclose(fs);
}

void AddUpdateRecord() {
    FILE* fs = fopen("hardware.dat", "r+b");
    fwrite(&records, sizeof(HARDWARE_ITEM), 100, fs);
    fclose(fs);
}

void ListItems() {
    cout << setw(10) << left << "Record #" << setw(35) << left << "Tool name" << setw(12) << left << "Quantity" << setw(5) << left << "Cost" << '\n';
    cout << setw(10) << left << "---------" << setw(35) << left << "-------------------------------" << setw(12) << left << "----------" << setw(5) << left << "-----" << '\n';
    FILE* fs = fopen("hardware.dat", "rb");
    HARDWARE_ITEM item;
    int items_count = 0;
    while (fread(&item, sizeof(HARDWARE_ITEM), 1, fs)) {
        // items_count = items_count + 1;
        if (item.is_active == 1) {
            cout << setw(10) << left << item.record_num << setw(35) << left << item.tool_name << setw(12) << left << item.quantity << setw(5) << left << item.cost << '\n';
        }
    }
    fclose(fs);
}


