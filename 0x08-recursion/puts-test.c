#include "holberton.h"
#include <stdio.h>
/**
* _puts_recursion - function that prints a string, followed by a new line
 * @s: pointer
 * Return: always success
*/
void _puts_recursion(char *s)
{
	if (*s != '\0')
		{
			_putchar(*s);
			_puts_recursion(++s);

		}
		else
		_putchar('\n');
			
}
