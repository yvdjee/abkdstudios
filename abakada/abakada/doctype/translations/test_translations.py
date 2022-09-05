# # Copyright (c) 2022, Kerwin and Contributors
# # See license.txt

# # import frappe
# from frappe.tests.utils import FrappeTestCase


# class TestTranslations(FrappeTestCase):
# 	pass

import frappe
import frappe.defaults

from frappe.tests.utils import FrappeTestCase


def create_events():
    if frappe.flags.test_events_created:
        return

    frappe.set_user("Administrator")
    doc = frappe.get_doc({
        "doctype": "Event",
        "subject":"_Test Event 1",
        "starts_on": "2014-01-01",
        "event_type": "Public"
    }).insert()

    doc = frappe.get_doc({
        "doctype": "Event",
        "subject":"_Test Event 2",
        "starts_on": "2014-01-01",
        "event_type": "Private"
    }).insert()

    doc = frappe.get_doc({
        "doctype": "Event",
        "subject":"_Test Event 3",
        "starts_on": "2014-01-01",
        "event_type": "Public"
        "event_individuals": [{
            "person": "test1@example.com"
        }]
    }).insert()

    frappe.flags.test_events_created = True


class TestEvent(FrappeTestCase):
    def setUp(self):
        create_events()

    def tearDown(self):
        frappe.set_user("Administrator")

    def test_allowed_public(self):
        frappe.set_user("test1@example.com")
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
            {"subject":"_Test Event 1"}))
        self.assertTrue(frappe.has_permission("Event", doc=doc))

    def test_not_allowed_private(self):
        frappe.set_user("test1@example.com")
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
            {"subject":"_Test Event 2"}))
        self.assertFalse(frappe.has_permission("Event", doc=doc))

    def test_allowed_private_if_in_event_user(self):
        doc = frappe.get_doc("Event", frappe.db.get_value("Event",
            {"subject":"_Test Event 3"}))

        frappe.set_user("test1@example.com")
        self.assertTrue(frappe.has_permission("Event", doc=doc))

    def test_event_list(self):
        frappe.set_user("test1@example.com")
        res = frappe.get_list("Event", filters=[["Event", "subject", "like", "_Test Event%"]], fields=["name", "subject"])
        self.assertEqual(len(res), 2)
        subjects = [r.subject for r in res]
        self.assertTrue("_Test Event 1" in subjects)
        self.assertTrue("_Test Event 3" in subjects)
        self.assertFalse("_Test Event 2" in subjects)
