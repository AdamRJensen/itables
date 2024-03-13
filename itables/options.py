"""Global options for ITables.

These parameters are documented at
https://mwouts.github.io/itables/advanced_parameters.html
"""

from .utils import find_package_file

"""Table layout, see https://datatables.net/reference/option/layout
NB: to remove a control, replace it by None"""
layout = {
    "topStart": "pageLength",
    "topEnd": "search",
    "bottomStart": "info",
    "bottomEnd": "paging",
}

"""Show the index? Possible values: True, False and 'auto'. In mode 'auto', the index is not shown
if it has no name and its content is range(N)"""
showIndex = "auto"

"""Default datatables classes. See https://datatables.net/manual/styling/classes"""
classes = "display nowrap"

"""Default table style. Use
- 'table-layout:auto' to compute the layout automatically
- 'width:auto' to fit the table width to its content
- 'margin:auto' to center the table.
Combine multiple options using ';'."""
style = "table-layout:auto;width:auto;margin:auto;caption-side:bottom"

"""Additional tags like e.g. caption"""
tags = ""

"""Maximum bytes before downsampling a table"""
maxBytes = 2**16

"""Maximum number of rows or columns before downsampling a table"""
maxRows = 0
maxColumns = 200

"""By default we don't sort the table"""
order = []

"""Pre dt code"""
pre_dt_code = ""

"""Optional table footer"""
footer = False

"""Column filters"""
column_filters = False

"""Should a warning appear when we have to encode an unexpected type?"""
warn_on_unexpected_types = True

"""Should a warning appear when the deprecated 'dom' is used?"""
warn_on_dom = True

"""The DataTable URL for the connected mode, see https://datatables.net/download/"""
dt_url = "https://www.unpkg.com/dt_for_itables@2.0.1/dt_bundle.js"

"""The DataTable bundle for the offline mode"""
dt_bundle = find_package_file("dt_for_itables/dt_bundle.js")
