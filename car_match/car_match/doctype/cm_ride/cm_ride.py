# Copyright (c) 2026, SPI and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CMRide(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		car: DF.Link | None
		driver: DF.Link | None
		email: DF.Data | None
		requested_by: DF.Link | None
		ride_order: DF.Link | None
		status: DF.Literal["Requested", "Assigning Driver", "Assigning Vehicle", "Confirmed", "In Progress", "Complete", "Cancelled"]
	# end: auto-generated types

	_DOCTYPE_NAME = "CM Ride"
