# Copyright (c) 2026, SPI and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CMRideBooking(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date_and_time: DF.Datetime | None
		email: DF.Data | None
		no_of_passengers: DF.Int
		pickup_location: DF.Data | None
		requested_by: DF.Link | None
		ride_type: DF.Literal["One way", "Roundtrip"]
	# end: auto-generated types

	_DOCTYPE_NAME = "CM Ride Booking"
