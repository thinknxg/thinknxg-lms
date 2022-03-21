import frappe

def execute():
    frappe.reload_doc("lms", "doctype", "lms_course")
    courses = frappe.get_all("LMS Course", {"status": ("is", "not set")}, ["name", "is_published"])
    for course in courses:
        status = "Approved" if course.is_published else "In Progress"
        frappe.db.set_value("LMS Course", course.name, "status", status)