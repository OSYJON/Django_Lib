# آماده سازی

اگر از یک محیط مجازی استفاده می‌کنید آن را فعال کنید (مخصوص لینوکس)

```bash
source <مسیر_محیط_مجازی>/bin/activate
```

# ساخت پروژه

- `django-admin startproject library` ---> ساخت ساختار اصلی پروژه
- `python manage.py startapp extend` ---> ساخت یک اَپ


# تنطیمات اولیه

- #### کد زیر را به INSTALLED_APPS اضافه کنید

```python
"extend.apps.ExtendConfig",
```

- #### کدهای زیر را در فایل تنظیمات اصلی پروژه اضافه کنید

```python
AUTH_USER_MODEL = 'extend.UserExtend'
ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': '<database_name>',
		'USER': '<username>',
		'PASSWORD': '<database_password>',
		'HOST': 'localhost',
		'PORT': '3306',
	}
}
```

# گسترش توانایی‌های کاربر جَنگو

### فایل extend/models.py را باز کنید

```python
	from django.db import models
	from django.contrib.auth.models import AbstractUser
	from django.contrib.auth.models import User

	class userExtend(AbstractUser):
		mobile_text = models.CharField('موبایل', max_length=11, blank=False)
		ncode_text = models.CharField('کد ملی', max_length=10, blank=False)
		mobile_status = models.BooleanField('وضعیت تایید موبایل', default=False, blank=False)
	   	email_status = models.BooleanField('وضعیت تایید ایمیل', default=False, blank=False)
    		is_admin = models.BooleanField(default=False, blank=False)
    		credit = models.DecimalField('اع‍تبار', default=1000000, blank=False, max_digits=10, decimal_places=0)
```


`python manage.py migrate`

- اگر در اجرای کد بالا با خطا مواجه شدید از این کد بهره بگیرید
  `python manage.py makemigrations extend`


# مدل کاربر جدید را در پنل ادمین به نمایش بگذارید

```python
from django.contrib import admin
from .models import userExtend

class userExtendadmin(admin.ModelAdmin):
    list_display = [
                                    "id", "is_superuser", "first_name",
				    "last_name", "mobile_text", "ncode_text",
				    "mobile_status", "email_status", "is_admin",
				    "credit"
				   ]

	# Register your models here.
	admin.site.register(userExtend, userExtendadmin)
```

# یک کاربر ادمین پدید آورید

`python manage.py createsuperuser`


# باقی اَپ‌ها را ایجاد کنید

```bash
python manage.py startapp book
```
```bash
python manage.py startapp users
```

- این برنامه‌ها را نیز به INSTALLED_APPS اضافه کنید
- مدل‌های این دو برنامه را در فایل‌های models.py خودشان بنویسید
- مد‌ل‌های آنها را در فایل‌‎های admin.py خودشان رجیستر کنید

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```

---
