#include "holberton.h"
/**
* times_table - Just count
*
* Return: Always 0 (Success)
*
*/
void times_table(void)
{
int n, m, x;

for (n = 0; n <= 9; n++)
{
for (m = 0; m <= 9; m++)
x = m * n;
if (x >= 10)
{
_putchar(' ');
_putchar((x / 10) + '0');
_putchar((x % 10) + '0');
}
else
{
if (m != 0)
{
_putchar(' ');
_putchar(' ');
}
_putchar(x + '0');

if (m != 9)
{
_putchar(',');
}
if (m == 9)
{
_putchar('\n');
}
m = 0;
}
}
}
