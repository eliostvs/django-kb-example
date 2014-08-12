from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy

from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout

from kb.forms import SearchForm


class ExampleSearchForm(SearchForm):

    def __init__(self, *args, **kwargs):
        super(ExampleSearchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.form_action = reverse_lazy('kb:search')
        self.helper.layout = Layout(
            FieldWithButtons(
                Field('q', placeholder="Type your question"),
                StrictButton('Search', type='submit',
                             css_id='btn-search',
                             css_class='btn btn-default')
            )
        )
