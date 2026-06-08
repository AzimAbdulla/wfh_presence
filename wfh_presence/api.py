import frappe


@frappe.whitelist(allow_guest=True)
def checkin(employee):
    doc = frappe.get_doc({
        "doctype": "Employee Checkin",
        "employee": employee,
        "log_type": "IN",
        "time": frappe.utils.now_datetime()
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "checkin": doc.name
    }


@frappe.whitelist(allow_guest=True)
def checkout(employee):
    doc = frappe.get_doc({
        "doctype": "Employee Checkin",
        "employee": employee,
        "log_type": "OUT",
        "time": frappe.utils.now_datetime()
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "checkin": doc.name
    }


@frappe.whitelist(allow_guest=True)
def heartbeat(employee):
    return {
        "status": "success",
        "employee": employee,
        "timestamp": frappe.utils.now_datetime()
    }


@frappe.whitelist(allow_guest=True)
def test():
    return {
        "status": "success",
        "message": "WFH Presence API Working"
    }
