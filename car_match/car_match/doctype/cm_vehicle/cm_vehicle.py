# Copyright (c) 2026, SPI and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CMVehicle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from car_match.car_match.doctype.cm_car.cm_car import CMCar
		from frappe.types import DF

		available_vehicles: DF.Table[CMCar]
		image: DF.AttachImage | None
		manufacturer: DF.Data | None
		model: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "CM Vehicle"
