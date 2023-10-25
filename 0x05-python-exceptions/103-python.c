#include <Python.h>

/**
 * print_python_list - Print information about a Python list object.
 * @p: PyObject pointer to the list.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (PyList_Check(p))
    {
        size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++)
        {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    }
    else
    {
        printf("  [ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: PyObject pointer to the bytes object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (PyBytes_Check(p))
    {
        size = PyBytes_Size(p);
        printf("[.] Python bytes object info\n");
        printf("  [.] Size: %ld\n", size);
        str = PyBytes_AsString(p);

        printf("  [.] Trying string: %s\n", str);
        printf("  [.] First %ld bytes: ", (size > 10) ? 10 : size);
        for (i = 0; i < size && i < 10; i++)
        {
            printf("%02hhx", str[i]);
            if (i < 9)
                printf(" ");
        }
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: PyObject pointer to the float object.
 */
void print_python_float(PyObject *p)
{
    char *repr;

    if (PyFloat_Check(p))
    {
        printf("[.] Python float info\n");
        repr = PyOS_double_to_string(PyFloat_AS_DOUBLE(p), 'r', 0,
		Py_DTSF_ADD_DOT_0, NULL);
        printf("  [.] value: %s\n", repr);
    }
    else
    {
        printf("  [ERROR] Invalid Float Object\n");
    }
}
