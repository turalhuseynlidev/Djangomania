# **Django** Proje2:
## TODO List Projesi

### Projenin Amaçları:
* Model Yapısını Anlamak
* Django ORM Query ile Çalışmak
* MVT İlişkisini Anlamak
* Django Shell Kullanımını Anlamak
* Django Shell'de Query Kullanımı
* OneToOneField, ForeignKey ve ManyToManyField Yapılarını Anlamak
* Context Prosessor ile Genel Verileri Site içerisinde Kullanmak
* DEBUG Mode
* Settings Dosyasını Daha Fazla Tanımak

![ToDo-List Yapisi](assets/todo-list.png)

## Django ORM Query:
```shell
python manage.py shell

```python
# Todo Modelini import etmek:
from todo.models import Todo
Todo.objects.all() - # Butun obyektleri goster
Todo.objects.count() - # Butun obyektleri say
Todo.objects.create(title='Shell uzerinde yaradilan todo obyekti') -  # Yeni obyekt yarat
Todo.objects.create(title='YENI IS ACTIVLE Shell uzerinde yaradilan obyekt', is_active=True)
Todo.objects.filter(is_active=True) - aktiv obyektleri gosterir
Todo.objects.filter(is_active=True).count() - aktiv obyektlerin sayini gosterer
```

```python
# Todo Modelini import etmek:
from todo.models import Todo

# Tum Objeler:
Todo.objects.all()

# Tum objeleri say:
Todo.objects.all().count()

# Yeni Todo olusturmak:
Todo.objects.create(title="Shell Uzerinden Olusturulan Todo")
Todo.objects.create(title="Shell Uzerinden Yeni Olusturulan Todo", is_active=True)

# is_active olanlari goster
Todo.objects.filter(is_active=True)  # SELECT * FROM todo WHERE is_active=True

# is_active olanlari say:
Todo.objects.filter(is_active=True).count()

# UPDATE:
# Yapilan sorguya uyan objelerin istenilen alanlari degistirilebilir..
Todo.objects.filter(is_active=False).update(is_active=True)
# Title icinde Django gecenleri bul ve Django ekle
todos = Todo.objects.(title__icontains="django")
# Title icinde Django gecmeyenleri bul ve Django ekle
todos = Todo.objects.exclude(title__icontains="django")

#UPDATE:
#Yapilan sorguya uyan objelerin istenilen alanlari degistirilebilir:
Todo.objects.filter(is_active=False).update(is_active=True)

#title kismine EKLEME YAPMAK: 
for item in todos:
    item.title = f"{item.title} - Django"
    item.save()
```
## ƏGƏR BÜTÜN DB-DEKİ İTEMLERİ SİLSEN, ASAGİDAKİ KODLA BERPA EDE BİLERSEN.BU KODU YADDA SAXLA KOD SENİN OZ KESFİNDİ
from todo.models import Todo

list = ["Django", "Python-Django", "Deneme-Django",
        "Shell uzerinde yaradilan obyekt-Django",
        "YENI IS ACTIVLE Shell uzerinde yaradilan obyekt-Django",
        "Daha bir shell uzerinden pythonla elave edilen obyekt-Django",
        "Javascript-Django"]

for item,  in list:
    Todo.objects.create(title=item)



## LAZIM OLAN TELEBE GORE OBYEKTIN CAGIRILMASI:
Todo.objects.get(id=1)
Todo.objects.get(pk=1)  eyni seydir.

# Bu kod ile requirement icersinde qeyd olunan paketleri proyekte ceke bilerik
pip freeze > requirements.txt




#TODO - Usere todo elave etmek accessi verilmesi, ve ancaq oz yaratdigi todo-lari gore bilmeli>>
#       1.models.py - from django.contrib.auth.models import User
#       2.models.py - class Todo(models.Model):
#                       user = models.ForeignKey(User, on_delete=models.CASCADE) 
#       burada on_detele = models.CASCADE oldugu ucun bu user silinerse, onun yaratdigi todo-lar da silinecekdir.
#       3.venv - python manage.py makemigrations
Bunu etdikde Django bizden default olaraq eger user olmasa ne vermeli oldugunu sorusur
user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1) yazsaq default olaraq 1 atir.
Eger biz table-i yeni yaradan vaxt user columnu yaratmis olsaydiq onda hec bir sual vermezdi
#       4.venv - python manage.py migrate
#       5. views.py faylina gediril ve :

def todo_detail_view(request, category_slug, id):
        todo = get_object_or_404(Todo, category__slug=category_slug,  pk=id, user=request.user)
        context = dict(
            todo = todo,
            todos = Todo.objects.filter(is_active=True)
    )
        return render(request, 'todo/todo_detail.html', context)