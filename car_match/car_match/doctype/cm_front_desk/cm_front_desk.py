# Copyright (c) 2026, SPI and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CMFrontDesk(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		employee_details: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "CM Front Desk"
