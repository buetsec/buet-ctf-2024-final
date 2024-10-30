#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int foo = 0;

void callme() {
  asm volatile("pop %%rdi\n\t"
               "ret"
               :
               :
               : "rdi");
}

void setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  if (foo == 0xdada) {
    callme();
  }
}

void win() { system("/bin/sh"); }

int main() {
  setup();
  char name[64];
  printf("Name: ");
  fgets(name, 64, stdin);
  char welcome[120];
  sprintf(welcome, "Welcome %s", name);
  printf("She sells sea shell\0");
  printf("\nBy the sea shore\n");
  printf(welcome);
  char key[120];
  printf("License key: ");
  fgets(key, 400, stdin);
  return 0;
}
