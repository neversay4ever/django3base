.. _query-string-fields:

Query string fields
===================

Tables pass data via the query string to indicate ordering and pagination
preferences.

The names of the query string variables are configurable via the options:

- ``order_by_field`` -- default: ``'sort'``
- ``page_field`` -- default: ``"page"``
- ``per_page_field`` -- default: ``"per_page"``, **note:** this field currently
  is not used by ``{% render_table %}``

Each of these can be specified in three places:

- ``Table.Meta.foo``
- ``Table(..., foo=...)``
- ``Table(...).foo = ...``

If you are using multiple tables on a single page, you will want to prefix these
fields with a table-specific name, in order to prevent links on one table
interfere with those on another table::

    def people_listing(request):
        config = RequestConfig(request)
        table1 = PeopleTable(Person.objects.all(), prefix="1-")  # prefix specified
        table2 = PeopleTable(Person.objects.all(), prefix="2-")  # prefix specified
        config.configure(table1)
        config.configure(table2)

        return render(request, 'people_listing.html', {
            'table1': table1,
            'table2': table2
        })
