from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("read/",read),
    path("create/<int:id>",create),
    path("retrive/<int:id>",retrive),
    path("delete/<int:id>",delete),
    path("update/<int:id>",update),
    path("createstuid/",createstuid),
    path("retrivestuid/<int:id>",retrive_studentid),
    path("deletestuid/<int:id>",student_delete),
    path("updatestuid/<int:id>",updatestuid),
    path("readallstuid/",readallstuid),
    path("return/<int:id>",returning_book),
        path("return/<int:id>",returning_book),

        path("return/<int:id>",returning_book),

        path("return/<int:id>",returning_book),

        path("return/<int:id>",returning_book),

        path("return/<int:id>",returning_book),

]
