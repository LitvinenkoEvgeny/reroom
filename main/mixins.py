from . import models


class ContactInfoMixin(object):
    """ Add contact data in template context """
    def get_context_data(self, **kwargs):
        context = super(ContactInfoMixin, self).get_context_data(**kwargs)
        context['contact'] = models.ContactInfo.objects.first()
        return context
