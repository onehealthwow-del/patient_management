# Copyright (c) 2024, wowit and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Patients(Document):
	def before_insert(self):
		self.set_full_name()

	def before_save(self):
		self.set_full_name()

	
	def set_full_name(self):
		parts = [self.first_name, self.second_name, self.third_name, self.last_name]
		self.full_name = " ".join([p for p in parts if p])
