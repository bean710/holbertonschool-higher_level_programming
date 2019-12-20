#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	char *bytes;
	int size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = (int)PyBytes_Size(p);
	printf("  size: %d\n", size);
	
	bytes = PyBytes_AsString(p);

	printf("  trying string: %s\n", bytes);

	size = size > 10 ? 10 : size;
	printf("  first %d bytes: ", size);
	for (i = 0; i < size; ++i)
		printf("%02hhx ", bytes[i]);
	printf("\n");
}

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
