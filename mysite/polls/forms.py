# contact/forms.py
from django import forms
from django.conf import settings
from django.core.mail import send_mail, EmailMessage








class ContactForm(forms.Form):
    betreff = forms.CharField(max_length=50, required=True)
    name = forms.CharField(max_length=120, label='Name')
    email = forms.EmailField(required=False,)
    handy = forms.IntegerField()
    von = forms.CharField(max_length=70)
    nach = forms.CharField(max_length=70)
    abholung = forms.CharField(max_length=70)
    anmerkung = forms.CharField(max_length=150, required=False)
    #attachment = forms.FileField(widget=forms.FileInput,required=False,)

    def clean_attachment(self):
        attachment = self.cleaned_data.get('attachment')
        if attachment:
            if attachment.size > 1024 * 1024 * 10:  # 10 MB
                raise forms.ValidationError("File size must not exceed 10 MB")
        return attachment


    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        # Subject wird als Handy benutzt.
        subject = cl_data.get('betreff')
        handy = cl_data.get('handy')
        von_adresse = cl_data.get('von')
        nach_adresse = cl_data.get('nach')
        abholzeitpunkt = cl_data.get('abholung')
        #payload = ContactForm.attachment.validate()

        msg = f'Betreff: {subject}\n\nEmail: {from_email}'
        msg += f'\nName: {name}'
        msg += f'\nHandynummer: {handy}'
        msg += f'\nAbholung: {abholzeitpunkt}\n\n'
        msg += f'\nVon: {von_adresse}\n\n'
        msg += f'\nNach: {nach_adresse}\n\n'


        msg += cl_data.get('anmerkung')





        return subject, msg,

    def send(self):
        subject, msg = self.get_info()

        email = EmailMessage(
            subject=subject,
            body=msg,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.RECIPIENT_ADDRESS],
        )

        attachment = self.cleaned_data.get('attachment')
        print(attachment)
        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        email.send()



