from django import forms
#Create your forms here.
class RegistrationForm(forms.Form):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # user_name = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # mobile = forms.IntegerField()
    # email = forms.EmailField()
    First_Name = forms.CharField(
        label="Enter FirstName",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'FirstName',
                'class': 'form-control'
            }
        )
    )
    Last_Name = forms.CharField(
        label="Enter Your LastName",
        widget=forms.TextInput(
            attrs={
                'placeholder':'LastName',
                'class':'form-control'

            }
        )
    )
    User_Name= forms.CharField(
        label="Enter Your UserName",
        widget=forms.TextInput(
            attrs={
                'placeholder':'UserName',
                'class':'forms-control'
            }
        )
    )
    Password= forms.CharField(
        label="Enter Your PassWord",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'forms-control'
            }
        )
    )
    Mobile= forms.CharField(
        label="Enter Your MobileNumber",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile Number',
                'class':'forms-control'
            }
        )
    )
    Email_id= forms.EmailField(
        label="Enter Your EmailId",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email Id',
                'class':'forms-control'
            }
        )
    )
class LoginForm(forms.Form):
    User_Name = forms.CharField(
        label="Enter Your USerName",
        widget=forms.TextInput(
            attrs={
                'placeholder':'UserName',
                'class':'form-control'
            }
        )
    )
    Password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your feedback'
            }
        )
    )
from multiselectfield import MultiSelectFormField
class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    mobile = forms.CharField(
        label="Enter Your MobileNumber",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'forms-control'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your EmailId",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email Id',
                'class': 'forms-control'
            }
        )
    )
    COURSES_CHOICES = (
        ('Python', 'PYTHON'),
        ('Django', 'DJANGO'),
        ('Rest Api', 'REST API'),
        ('Mysql', 'MYSQL')
    )
    courses =MultiSelectFormField(max_length=300, choices=COURSES_CHOICES,label="Select Required Coures:")
    TRAINER_CHOICES = (
        ('Ravi', 'RAVI'),
        ('Sai', 'SAI'),
        ('Hari', 'HARI')
    )
    trainer = MultiSelectFormField(max_length=300, choices=TRAINER_CHOICES,label="Select Required Trainer:")
    BRANCHES_CHOICES = (
        ('Hyd', 'HYDERABAD'),
        ('Pune', 'PUNE'),
        ('Chennai', 'CHENNAI')
    )
    branches = MultiSelectFormField(max_length=300, choices=BRANCHES_CHOICES,label="Select Required Branches:")

    date=forms.DateField(
        widget=forms.SelectDateWidget(),label="Enter Your Date:"
    )
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect,choices=GENDER_CHOICES,label="Select Your Gender:"
    )