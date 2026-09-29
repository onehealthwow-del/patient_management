# Copyright (c) 2024, wowit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Visits(Document):
	def autoname(self):
		if self.visit_no_his:
			self.name = self.visit_no_his

	def before_insert(self):
		self.resolve_patient_identifier()

	def resolve_patient_identifier(self):
		if not self.patient_identifier:
			return
		
		# تحقق إذا كان السجل موجوداً مباشرة
		patient_exists = frappe.db.get_value("Patients", self.patient_identifier, "name")
		if patient_exists:
			return
		
		# ابحث بالـ MRN
		patient = frappe.db.get_value("Patients", {"mrn": self.patient_identifier}, "name")
		if patient:
			self.patient_identifier = patient
		else:
			frappe.log_error(
				f"Patient not found for identifier: {self.patient_identifier}",
				"Visits Patient Resolution Warning"
			)