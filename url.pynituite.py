path()�֐�:
path()�֐��́ADjango��URL���[�e�B���O�ɂ����āAURL�p�^�[���Ƃ���ɑΉ�����r���[���}�b�s���O���邽�߂Ɏg�p�����֐��ł��Burlpatterns���X�g����path()�֐����g�p���邱�ƂŁA�����URL�p�^�[���ɑ΂��Ăǂ̃r���[�����s���邩���`���܂��B
�������iroute�j:
���[�e�B���O�p�^�[�����w�肵�܂��B�����URL�̈ꕔ�ł���Ahttp://yourdomain.com/�̌�ɑ��������ł��B���̕����ɑ΂��ă}�b�`���O���s���A�Y������r���[���Ăяo����܂��B
��URL
�������iview�j:
URL�ɃA�N�Z�X���ꂽ�Ƃ��Ɏ��s�����r���[���w�肵�܂��B�r���[�͊֐��܂��̓N���X�x�[�X�r���[�Ƃ��Ē�`����܂��B�Ⴆ�΁Aviews.index��index�r���[���Ăяo����邱�Ƃ��Ӗ����܂��B
���r���[�̍s����w��
��O�����ikwargs�j:
�L�[���[�h�����������Ƃ��ēn�����Ƃ��ł��܂��B����ɂ��A�r���[�ɒǉ��̃p�����[�^��n�����Ƃ��ł��܂��B
���p�����[�^�������̒l�ɂȂ�

��l�����iname�j:
URL�p�^�[���ɖ��O�����܂��B����ɂ��A�e���v���[�g��r���[����URL�𐶐�����ۂɁA���O���g����URL���Q�Ƃł��܂��B

���Œ���������Ƒ������͕K�v


�@�p�����[�^�͒l�����ł悢
/articles/42/
�Aname=�͊��K


include()�֐��́ADjango��URL�ݒ�ɂ����āA�ʂ̃A�v���P�[�V������URL�ݒ���C���N���[�h���邽�߂Ɏg�p����܂��B����ɂ��A�����̃A�v���P�[�V�����Ԃ�URL�ݒ�����ʓI�ɊǗ����A���W���[���������߂邱�Ƃ��ł��܂��B

myproject/
������ myproject/
��   ������ settings.py
��   ������ urls.py
��   ������ ...
��
������ blog/
��   ������ urls.py
��   ������ views.py
��   ������ ...
��
������ top/
��   ������ urls.py
��   ������ views.py
��   ������ ...
��
������ manage.py

from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from top import views as top_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # blog�A�v���P�[�V������URL�ݒ���C���N���[�h
    path('top/', include('top.urls')),    # top�A�v���P�[�V������URL�ݒ���C���N���[�h
    # ���̃v���W�F�N�g�S�̂�URL�ݒ�
]
