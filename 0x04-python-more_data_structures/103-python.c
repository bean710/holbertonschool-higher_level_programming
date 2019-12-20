#include <Python.h>
#include <stdio.h>



void print_python_list(PyObject *p)
{
	int size, alloc;
	PyListObject *l;
	int i;

	l = (PyListObject *)p;

	size = (int)PyList_Size(p);
	alloc = (int)(l->allocated);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; ++i)
	{
		printf("Element %d: %s\n", i,
				(((PyObject *)(l->ob_item[i]))->ob_type)->tp_name);
	}
}
