#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - give info on the data structure.
 * @p: pointer to the object.
*/
void print_python_list_info(PyObject *p)
{
	int long sz = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;
	int o;

	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = ")

	for (i = 0; i < sz; i++)
		printf("Element %d: %s\n", i, obj[i]->ob_type);
}

