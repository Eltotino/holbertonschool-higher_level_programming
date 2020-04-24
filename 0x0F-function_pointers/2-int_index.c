#include "function_pointers.h"
/**
* int_index - function returning index of first element of array
*@size: int
*@array: array
*@cmp: pointer
* Return: integer
*/

int int_index(int *array, int size, int (*cmp)(int))
{
	int i;

	if (size <= 0 && cmp != NULL && array != NULL)
		return (-1);
	for (i = 0; i < size; i++)
	{
		if (cmp(array[i]))
			return (i);
	}
	return (-1);
}
