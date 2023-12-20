path()関数:
path()関数は、DjangoのURLルーティングにおいて、URLパターンとそれに対応するビューをマッピングするために使用される関数です。urlpatternsリスト内でpath()関数を使用することで、特定のURLパターンに対してどのビューを実行するかを定義します。
第一引数（route）:
ルーティングパターンを指定します。これはURLの一部であり、http://yourdomain.com/の後に続く部分です。この部分に対してマッチングが行われ、該当するビューが呼び出されます。
＊URL
第二引数（view）:
URLにアクセスされたときに実行されるビューを指定します。ビューは関数またはクラスベースビューとして定義されます。例えば、views.indexはindexビューが呼び出されることを意味します。
＊ビューの行先を指定
第三引数（kwargs）:
キーワード引数を辞書として渡すことができます。これにより、ビューに追加のパラメータを渡すことができます。
＊パラメータが引数の値になる

第四引数（name）:
URLパターンに名前をつけます。これにより、テンプレートやビュー内でURLを生成する際に、名前を使ってURLを参照できます。

＊最低限第一引数と第二引数は必要


①パラメータは値だけでよい
/articles/42/
②name=は慣習


include()関数は、DjangoのURL設定において、別のアプリケーションのURL設定をインクルードするために使用されます。これにより、複数のアプリケーション間でURL設定を効果的に管理し、モジュール性を高めることができます。

myproject/
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── ...
│
├── blog/
│   ├── urls.py
│   ├── views.py
│   ├── ...
│
├── top/
│   ├── urls.py
│   ├── views.py
│   ├── ...
│
└── manage.py

from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from top import views as top_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # blogアプリケーションのURL設定をインクルード
    path('top/', include('top.urls')),    # topアプリケーションのURL設定をインクルード
    # 他のプロジェクト全体のURL設定
]
