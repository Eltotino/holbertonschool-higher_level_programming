#include "holberton.h"
#include <stdlib.h>
/**
*argstostr - function that concatenates arg of a prog
* @ac : int
* @av : char
* Return: a character
*/
char *argstostr(int ac, char **av)
{
	int i;
	int j;
	int k;
	char *s;

	if (ac == 0 || av == NULL)
		return (NULL);
	for (i = 0; i < ac; i++)
	{
		for (j = 0; av[i][j]; j++)
			k++;
	}
	s = malloc(sizeof(char) * k + 1 + ac);
	k = 0;
		for (i = 0; i < ac; i++)
	{
		for (j = 0; av[i][j]; j++)
		{
			s[k] = av[i][j];
			k++;
		}
		s[k] = '\n';
		k++;
	}
	return (s);
}
