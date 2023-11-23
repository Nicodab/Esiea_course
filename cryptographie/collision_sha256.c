#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

#define HASH_SIZE 32  // Taille du hash SHA-256 en octets
#define TRUNCATED_HASH_SIZE 8  // Taille que vous souhaitez stocker

// Structure pour représenter un élément de la séquence
typedef struct Node {
    char hash[TRUNCATED_HASH_SIZE];
    struct Node* next;
} Node;

// Fonction de hachage SHA-256
void hash_function(const char* message, char* hash) {
    unsigned char hash_result[HASH_SIZE];
    SHA256((const unsigned char*)message, strlen(message), hash_result);

    // Troncature du hash
    for (int i = 0; i < TRUNCATED_HASH_SIZE; ++i) {
        snprintf(hash + i * 2, 3, "%02x", hash_result[i]);
    }
}

// Fonction pour trouver une collision
void find_collision(const char* initial_message, long max_iterations) {
    Node* hare = malloc(sizeof(Node));
    Node* tortoise = malloc(sizeof(Node));

    // Initialisation des éléments de la séquence
    hash_function(initial_message, hare->hash);
    strcpy(tortoise->hash, hare->hash);
    hare->next = NULL;
    tortoise->next = NULL;

    for (int i = 1; i <= max_iterations; ++i) {
        // Avancer le lièvre de deux étapes
        hash_function(hare->hash, hare->hash);
        hash_function(hare->hash, hare->hash);

        // Avancer la tortue d'une étape
        hash_function(tortoise->hash, tortoise->hash);

        // Vérifier s'il y a collision
        if (strncmp(hare->hash, tortoise->hash, TRUNCATED_HASH_SIZE) == 0) {
            printf("Collision found at iteration %d:\n", i);
            printf("Message hare: %.8s\n", hare->hash);
            printf("Message tortoise: %.8s\n", tortoise->hash);

            // Libérer la mémoire
            free(hare);
            free(tortoise);
            return;
        }

        // Ajouter un nouveau nœud à la séquence
        Node* new_node_hare = malloc(sizeof(Node));
        Node* new_node_tortoise = malloc(sizeof(Node));
        hash_function(hare->hash, new_node_hare->hash);
        hash_function(tortoise->hash, new_node_tortoise->hash);
        new_node_hare->next = hare->next;
        hare->next = new_node_hare;
        new_node_tortoise->next = tortoise->next;
        tortoise->next = new_node_tortoise;
    }

    printf("No collision found after %ld iterations.\n", max_iterations);

    // Libérer la mémoire
    while (hare != NULL) {
        Node* temp = hare;
        hare = hare->next;
        free(temp);
    }

    while (tortoise != NULL) {
        Node* temp = tortoise;
        tortoise = tortoise->next;
        free(temp);
    }
}

int main() {
    // Message initial "hello" et 2^25 itérations max
    find_collision("hello", 4294967296);

    return 0;
}
