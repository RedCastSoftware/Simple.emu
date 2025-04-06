#include <stdio.h>
#include <string.h>

int main() {
    int number = 10;
    int i = 0;
    int t = 0;
    char j[100];
    char icarus_mem[100] = "the";
    int icarus_meem = 10;
        printf("mov/load: ");
        scanf("%[^\n]", j);
        printf("Command: %s\n", j);
        if (strcmp(j, "stablenf") == 0) {
            while (i == t){
                printf("    StabilityTest %d    ", i);
                i++;
                t++;
            }
        }
        if (strcmp(j, "stablef") == 0) {
            while (i == t){
                printf("Stability Test %d\n", i);
                i++;
                t++;
            }
        }
        if (strstr(j, "mov") != NULL) {
            char *newov = j + 4;
            printf("Mov detected %s\n", newov);
            strcat(icarus_mem, newov);
            printf("Memory: %s\n", icarus_mem);
        }
        if (strstr(j, "load") != NULL) {
            printf("%s\n", icarus_mem);
        }    
        
    return 0;
}