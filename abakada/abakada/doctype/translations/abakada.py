import frappe
from frappe.model.document import Document


def set_default_context(context):
    """
        Inject or set pre-defined values to the context dictionary
        Args:
            context: Website Context
    """
    context['details'] = "ERPNext Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu scelerisque felis imperdiet proin fermentum leo vel orci porta. Duis ut diam quam nulla porttitor massa id neque. Cursus turpis massa tincidunt dui ut ornare lectus sit amet. Urna nec tincidunt praesent semper feugiat nibh sed pulvinar proin. Nulla at volutpat diam ut venenatis tellus. Vitae nunc sed velit dignissim sodales ut eu. Arcu cursus euismod quis viverra nibh cras pulvinar mattis. Sit amet mauris commodo quis imperdiet massa tincidunt. Nisl rhoncus mattis rhoncus urna. Magnis dis parturient montes nascetur ridiculus mus mauris. Amet luctus venenatis lectus magna fringilla urna. In nibh mauris cursus mattis molestie a. Placerat orci nulla pellentesque dignissim enim sit. Sit amet commodo nulla facilisi. In pellentesque massa placerat duis ultricies lacus sed. Fermentum leo vel orci porta non pulvinar. Orci eu lobortis elementum nibh"
    context['img_alt'] = "Abakada Studios"
    context['img_url'] = "https://www.abakadastudios.com/wp-content/uploads/2022/06/Layer-2.png"


def get_site_context(context):
    """
        Get and pass the context and doc if its not None.
    """
    if context.doc is not None:
        doc = context.doc
        search_context(context, doc)


def search_context(context, doc):
    """
        Will perform deep search from context.
        Available types are List, String and Dictionary.
        Args:
            context: Context
            doc: Doctype?
    """
    for c in context:
        if type(context[c]) is list:
            for l in context[c]:
                if type(l) is dict:
                    for k,v in l.items():
                        l[k] = replace_context(v, doc)

        if type(context[c]) is str:
            context[c] = replace_context(context[c], doc)

        if type(context[c]) is frappe._dict:
            for fd in context[c]:
                context[c][fd] = replace_context(context[c][fd], doc)


def replace_context(context, doc):
    """
        Replace the word/phrase with another word/phrase.
        Args:
            context: Context
            doc: Doctype?
    """
    return context.replace(doc._from, doc._to)
