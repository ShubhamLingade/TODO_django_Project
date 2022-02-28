from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('add_task',views.load_task,name='add_task'),
    path('insert_task',views.insert_task),
    path('editTask/<int:tid>', views.editTask, name='editTask'),
    path('updateTask/<int:tid>', views.updateTask, ),
    path('delTask/<int:tid>', views.deleteTask, name='delTask'),

    path('load_list',views.load_list,name='load_list'),
    path('insert_list',views.insertListTask),
    path('editList/<int:lid>',views.editList,name='editList'),
    path('updateList/<int:lid>', views.updateList,),
    path('delTaskList/<int:tid>', views.deleteTaskList, name='delTaskList'),

    path('add_custem', views.load_custem, name='add_custem'),
    path('insert_custem', views.insert_custem),
    path('editcustem/<int:cid>', views.editcustom, name='editcustem'),
    path('updatecustem/<int:cid>', views.updatecustem, ),
    path('delcustem/<int:tid>', views.deletecustem, name='delcustem'),

    path('add_tags', views.load_tags, name='add_tags'),
    path('insert_tags', views.insert_tags),
    path('edittags/<int:gid>', views.edittags, name='edittags'),
    path('updatetags/<int:gid>', views.updatetags, ),
    path('deltags/<int:tid>', views.deletetags, name='deltags'),

]