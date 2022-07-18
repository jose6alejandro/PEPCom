from django import forms 

class Form_Login(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Correo electrónico",                
                "class": "form-control"
            }
        ))    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Contraseña",                
                "class": "form-control"
            }
        ))

class Form_Register(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Nombre",                
                "class": "form-control"
            }
        ))  
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Apellido",                
                "class": "form-control"
            }
        ))      
    email_user = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Correo electrónico",                
                "class": "form-control"
            }
        ))
    user_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Contraseña",                
                "class": "form-control", 
                "id":"txtPassword"
            }
        ))
    access_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Código",
                "class": "form-control"
            }
        ))  
    birthday_date = forms.DateField(
        widget=forms.DateInput(
            format='%d-%m-%Y', 
            attrs={"placeholder" : "Fecha de nacimiento (formato: DD-MM-AAAA)", "class": "form-control", 
                    "title":"Por favor introduzca en el formato correcto"}),
            input_formats=('%d-%m-%Y',)
        )
    user_role = forms.ChoiceField(
        choices=(('', "-- Soy --"),(True, "Estudiante"), (False, "Profesor")), 
        widget=forms.Select(attrs={"class": "form-control"})) 
