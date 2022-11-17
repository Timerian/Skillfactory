from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'head',
            'text',
            'categories',
            'author'
        ]

    def set_fields(self, data):
        # The temporary data for checking the uniqueness of the value of the fields
        temp_data = None

        for field in self.fields:
            field_data = data.get(field)

            if field_data:
                exec(f"{field} = field_data")
            elif field_data is None:
                raise ValidationError({field: "The field is required"})
            elif field_data == temp_data:
                raise ValidationError("All fields must have a unique value")

            temp_data = field_data

    def clean(self):
        cleaned_data = super().clean()
        self.set_fields(cleaned_data)
        return cleaned_data


class ArticleForm(BasePostForm, forms.ModelForm):
    pass


class NewsForm(BasePostForm, forms.ModelForm):
    pass


class SubscribeForm(forms.ModelForm):
    pass
