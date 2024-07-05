#include "palindrome.h"

/**
 * is_palindrome - checks if a number is a palindrome
 * n: number to check
 * Return: 1 if palindrome, 0 if not
 */


int is_palindrome(unsigned long n){

    unsigned long reversed = 0, remainder, original;

    original = n;

    while (n != 0){
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (original == reversed)
        return (1);
    else
        return (0);
}
