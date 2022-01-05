# A django project template

安装的包：

django==3.2

django-admin-tailwind

django-tailwind

django-crispy-forms

crispy-tailwind

django-filter

django-htmx

django-extensions




django-tables2用改造了base.html（tailwindcss）的版本



1. 全部使用tailwindcss 

2. 在base.html里载入htmx

3. 在base.html里载入alpinejs

4. 在base.html里设计好navbar，footer

5. 一个demo app，展示如何使用django-admin-tailwind, django-tables2

   
#使用步骤
1. python3 -m venv django3base
2. source django3base/bin/activate
3. pip install -r requirements.txt
4. python manage.py runserver_plus
5. python magage.py tailwind start  (另一个terminal窗口)





