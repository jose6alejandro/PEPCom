from django import forms 
from crud_problems_app.models import User_Create_Problem

class Form_Create_problem(forms.ModelForm):  
            
    class Meta:
        model = User_Create_Problem
        fields = '__all__'

        widgets = {
            "name": forms.TextInput(            
                attrs={
                "placeholder" : "Ejemplo: Las pelotas blancas",                
                "class": "form-control"
            }),
            "question": forms.TextInput(
                attrs={
                "placeholder" : "Ejemplo: ¿Cúal de las pelotas finalizó el recorrido?",                
                "class": "form-control"
            }),
            "correct_option": forms.TextInput(
                attrs={
                "placeholder" : "Opción correcta",                
                "class": "form-control"
            }),
            "distractor1": forms.TextInput(
                attrs={
                "placeholder" : "Distractor  1",                
                "class": "form-control"
            }),
            "distractor2": forms.TextInput(
                attrs={
                "placeholder" : "Distractor  2",                
                "class": "form-control"
            }),
            "distractor3": forms.TextInput(
                attrs={
                "placeholder" : "Distractor  3",                
                "class": "form-control"
            }),
            "explanation": forms.Textarea(
                attrs={
                "placeholder" : "Agregue una breve explicación",                
                "class": "form-control", 
                "rows": "5"
            }),
            "abstraction": forms.CheckboxInput(
                attrs={
                "class": "selectgroup-input", 
            }),
            "decomposition": forms.CheckboxInput(
                attrs={
                "class": "selectgroup-input", 
            }),
            "algorithms": forms.CheckboxInput(
                attrs={
                "class": "selectgroup-input", 
            }),
            "generalization": forms.CheckboxInput(
                attrs={
                "class": "selectgroup-input", 
            }),
            "evaluation": forms.CheckboxInput(
                attrs={
                "class": "selectgroup-input", 
            })
        }




