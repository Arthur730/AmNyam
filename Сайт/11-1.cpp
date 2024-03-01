#include <iostream>
#include <string>
using namespace std;

string encrypt_caesar(string text, int shift) {
  string encrypted_text = "";
  for (char& c : text) {
    if (isalpha(c)) {
      char base = islower(c) ? 'a' : 'A';  
      c = (c - base + shift) % 26 + base;  
    }
    encrypted_text += c;
  }
  return encrypted_text;
}

int main() {
  string text;
  int shift;
  cin >> text;
  cin >> shift;
  cout << encrypt_caesar(text, shift);
  
}