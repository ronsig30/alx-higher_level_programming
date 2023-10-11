#include <Python.h>
#include <stdio.h>

/**
 *print_python_list - Print basic information about a Python list object.
 *@p: A pointer to a Python object.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(list);
	Py_ssize_t i;

	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);

		for (i = 0; i < size; i++)
		{
			printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
	}
}
