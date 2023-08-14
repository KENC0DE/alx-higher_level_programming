#include <stdio.h>
#include <Python.h>
#include <listobjct.h>
#include <object.h>

/**
 * print_python_list_info - give info on the data structure.
 * @p: pointer to the object.
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyObject *dt;

	if (p == NULL)
		return;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
		printf("[*] Allocated = %zd\n", PyList_GET_SIZE(p));
	}
	for (i = 0; i < PyList_Size(p); ++i)
	{
		dt = PyList_GetItem(p, i);

		printf("Element %zd: ", i);

		if (PyLong_Check(dt))
			printf("int\n");
		else if (PyFloat_Check(dt))
			printf("float\n");
		else if (PyUnicode_Check(dt))
			printf("str\n");
		else if (PyList_Check(dt))
			printf("list\n");
		else if (PyTuple_Check(dt))
			printf("tuple\n");
		else
			return;
	}
}
