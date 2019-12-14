#include "Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to the python object
 *
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t i = 0, size;
	PyObject *obj;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		while (i < size)
		{
			obj = list->ob_item[i];
			type = obj->ob_type;
			printf("Element %ld: %s\n", i, type->tp_name);
			i++;
		}
	}
}
