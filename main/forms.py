from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"class":"w-full px-5 py-1 text-gray-700 bg-gray-200 rounded", 
                                                                            "id":"username",
                                                                            "name":"username",
                                                                            "type":"text",
                                                                            "required":"",
                                                                            "placeholder":"",
                                                                            "aria-label":"username"
                                                                            }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"w-full px-5  py-1 text-gray-700 bg-gray-200 rounded",
                                                                                "id":"password",
                                                                                "name":"password",
                                                                                "type":"password",
                                                                                "required":"",
                                                                                "placeholder":"",
                                                                                "aria-label":"password"
                                                                                }))
