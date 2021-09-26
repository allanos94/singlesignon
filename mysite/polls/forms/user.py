from django import forms
TEXT_FIELD = 'text'
SELECT_FIELD = 'select'


class ProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    def __init__(self, *args, **kwargs):
        dynamic_fields = kwargs.pop('fields', [])
        super().__init__(*args, **kwargs)

        for field in dynamic_fields:
            if field['type'] == TEXT_FIELD:
                form_field = forms.CharField()
            elif field['type'] == SELECT_FIELD:
                form_field = forms.ChoiceField(
                    choices=field['choices'],
                )

            form_field.label = field['label']
            form_field.required = field['required']
            form_field.id = field['id']
            form_field.type = field['type']
            self.fields[field['id']] = form_field


