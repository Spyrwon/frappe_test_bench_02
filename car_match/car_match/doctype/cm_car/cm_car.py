# Copyright (c) 2026, SPI and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CMCar(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from car_match.car_match.doctype.cm_car_bookings.cm_car_bookings import CMCarBookings
		from frappe.types import DF

		active_bookings: DF.Table[CMCarBookings]
		availability: DF.Literal["Available", "Unavailable"]
		colour: DF.Data | None
		license_no: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "CM Car"
