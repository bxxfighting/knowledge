### 在flask中配置使用alembic

官方文档:

1. 开始使用alembic和手动生数据库改动的使用方法

   http://alembic.zzzcomputing.com/en/latest/tutorial.html#the-migration-environment


2. 自己生成数据库改动的使用方法

   http://alembic.zzzcomputing.com/en/latest/autogenerate.html

具体使用按照文档来就可以，只我在按照文档操作时遇到的两个问题

1. alembic.ini中数据库配置

   sqlalchemy.url = mysql+pymysql://xx:xx@192.168.31.88/trace

   > 我用的是mysql，client是pymysql

2. env.py中target_metadata配置

   在这里有两个问题:

   第一个：你在```from myapp import mymodel```或者网上很多```from myapp import db```，这里有一个问题，如果你直接这么调用，一般都会说找不到myapp的，很多人的解决办法是: 

   ```
   import sys
   sys.path.append('..')
   from myapp import db
   ```

   这样看似解决了问题，首先这种写法是不能通过flake8检查的，而且这并不是一个根本解决办法。

   那么现在我们就要明白为什么这么可以解决问题，这是因为sys.path.append()增加了python包的查找路径而已，所以我们只要把自己的项目路径增加到python的查找路径上就可以了。

   ```
   export PYTHONPATH=$PYTHONPATH:/home/xx/workspace/trace
   ```

   > 这个```/home/xx/workspace/trace```是我的项目根路径
   >
   > 这样就可以不再需要在代码中加sys.path.append之类的内容了
   >
   > 这个export最好写到系统启动就会执行的脚本中，比如```/etc/profile```中

   第二个：```target_metadata = db.metadata```

   这里有一个可能会遇到的问题，这个db，必须是跟app发生了关系的db，也就是```db = SQLAlchemy(app)```或者```db.init_app(app)```，我当时遇到的问题就是：

   ```
   # app.py
   db = SQLAlchemy()

   def create_app():
   	app = Flask('name')
   	config_db(app)
   	return app
   	
   def config_db(app):
   	db.init_app(app)
   	
   if __name__ == '__main__':
   	app = create_app()
   ```

   > 从我上面的代码可以看出，我如果在导入```from app import db```这时候我导入的是仅仅是```db = SQLAlchemy```这个db，还并没有和app发生关系呢

   ​