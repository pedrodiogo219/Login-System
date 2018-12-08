from app import db
"""
class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)


	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email

	def __repr__(self):
		return "<User %r>" % self.username


class Post(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', foreign_keys=user_id)

	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id

	def __repr__(self):
		return "<Post %r>" % self.id

class Follow(db.Model):
	__tablename__ = "follow"

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	user = db.relationship('User', foreign_keys=user_id)
	follower = db.relationship('User', foreign_keys=follower_id)
	

"""

class Shopping(db.Model):
	__tablename__= "shopping"

	nome = db.Column(db.String(70), primary_key=True)
	endereco = db.Column(db.String(70), nullable=False)
	horarioFuncionamento = db.Column(db.String(40))
	telefone = db.Column(db.String(15), nullable=False)

	def __init__(self, n, e, h, t):
		self.nome=n
		self.e=e
		self.horarioFuncionamento=h
		self.telefone=t


class Loja(db.Model):
	__tablename__ = "loja"

	codloja = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nomeloja = db.Column(db.String(30), nullable=False)
	piso = db.Column(db.Integer, nullable=False)
	numloja = db.Column(db.Integer, nullable=False)
	telefone = db.Column(db.String(15))
	site = db.Column(db.String(70))


class Categoria_Loja(db.Model):
	__tablename__ = "categoria_loja"

	loja = db.Column(db.Integer, db.ForeignKey('loja.codloja'), primary_key=True)
	categoriaLoja = db.Column(db.String(30), primary_key=True)

	loja_fk = db.relationship('Loja', foreign_keys=loja)


class CasaEspetaculos(db.Model):
	__tablename__ = "casaespetaculos"

	codcasa = db.Column(db.Integer, primary_key=True)
	nomecasa = db.Column(db.String(30), nullable=False)
	telefone = db.Column(db.String(15))
	piso = db.Column(db.Integer, nullable=False)
	numero = db.Column(db.Integer, nullable=False)
	site = db.Column(db.String(70))


class Usuario(db.Model):
	__tablename__ = "usuario"

	codpessoa= db.Column(db.Integer, primary_key=True)
	nome= db.Column(db.String(100), nullable=False)
	telefonefixo= db.Column(db.String(15))
	telefonecelular= db.Column(db.String(15))
	email= db.Column(db.String(60), nullable=False, unique=True)
	senha= db.Column(db.String(20), nullable=False)


class Assinante(db.Model):
	__tablename__ = "assinante"

	codpessoa= db.Column(db.Integer, primary_key=True)
	nome= db.Column(db.String(100), nullable=False)
	telefonefixo= db.Column(db.String(15))
	telefonecelular= db.Column(db.String(15))
	email= db.Column(db.String(60), nullable=False, unique=True)
	senha= db.Column(db.String(20), nullable=False)


class Funcionario_Loja(db.Model):
	__tablename__ = "funcionario_loja"

	codpessoa = db.Column(db.Integer, primary_key=True)
	codfuncionario = db.Column(db.Integer, nullable=False)
	loja = db.Column(db.Integer, db.ForeignKey('loja.codloja'))
	nome = db.Column(db.String(100), nullable=False)
	telefonefixo = db.Column(db.String(15))
	telefonecel = db.Column(db.String(15))
	email = db.Column(db.String(60), nullable=False, unique=True)
	senha = db.Column(db.String(20), nullable=False)

	loja_fk = db.relationship('Loja', foreign_keys=loja)


class Funcionario_Casa_Espetaculos(db.Model):
	__tablename__ = "funcionario_casa_espetaculos"

	codpessoa = db.Column(db.Integer, primary_key=True)
	codfuncionario = db.Column(db.Integer)
	casaespetaculos = db.Column(db.Integer, db.ForeignKey('casaespetaculos.codcasa'))
	nome = db.Column(db.String(100), nullable=False)
	telefonefixo = db.Column(db.String(15))
	telefonecel = db.Column(db.String(15))
	email = db.Column(db.String(60), unique=True, nullable=False)
	senha = db.Column(db.String(20), nullable=False)

	casaespetaculos_fk = db.relationship('CasaEspetaculos', foreign_keys=casaespetaculos)


class Estacionamento(db.Model):
	__tablename__ = "estacionamento"

	nome = db.Column(db.String(70), primary_key=True)
	shopping = db.Column(db.String(70), db.ForeignKey('shopping.nome'))
	telefone = db.Column(db.String(15), nullable=False)
	numvagas = db.Column(db.Integer, nullable=False)
	horariofuncionamento = db.Column(db.String(40), nullable=False)

	shopping_fk = db.relationship('Shopping', foreign_keys=shopping)


class Hotel(db.Model):
	__tablename__ = "hotel"

	nome = db.Column(db.String(70), primary_key=True)
	shopping = db.Column(db.String(70), db.ForeignKey('shopping.nome'))
	site = db.Column(db.String(70), nullable=False)
	endereco = db.Column(db.String(70), nullable=False)

	shopping_fk = db.relationship('Shopping', foreign_keys=shopping)


class Servicos(db.Model):
	__tablename__ = "servicos"

	codservico = db.Column(db.Integer, primary_key=True)
	shopping = db.Column(db.String(70), db.ForeignKey('shopping.nome'))
	nome = db.Column(db.String(70), nullable=False)
	horariofuncionamento = db.Column(db.String(40), nullable=False)
	descricao = db.Column(db.String(300), nullable=False)
	localizacao = db.Column(db.String(70), nullable=False)

	shopping_fk = db.relationship('Shopping', foreign_keys=shopping)


class Sala(db.Model):
	__tablename__ = "sala"

	codsala = db.Column(db.Integer, primary_key=True)
	numsala = db.Column(db.Integer, nullable=False)
	numcadeiras = db.Column(db.Integer, nullable=False)
	_3D = db.Column(db.Boolean)
	casaespetaculos = db.Column(db.Integer, db.ForeignKey('casaespetaculos.codcasa'))

	casa_fk = db.relationship('CasaEspetaculos', foreign_keys=casaespetaculos)


class Newsletter(db.Model):
	__tablename__ = "newsletter"

	codnewsletter = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.Date, nullable=False)
	conteudo = db.Column(db.Text, nullable=False)
	categoria = db.Column(db.String(30), nullable=False)


class ESPETACULO(db.Model):
	__tablename__ = "espetaculo"

	cod_espetaculo = db.Column(db.Integer, primary_key=True)
	sala = db.Column(db.Integer, db.ForeignKey('sala.codsala'))
	nome = db.Column(db.String(70), nullable=False)
	duracao = db.Column(db.Integer, nullable=False)
	descricao = db.Column(db.String(300), nullable=False)
	classificacao = db.Column(db.Integer, nullable=False)
	linguagem = db.Column(db.String(30), nullable=False)

	fk_sala =  db.relationship('sala', foreign_keys=sala)


class CATEGORIA_ESPETACULO(db.Model):
	__tablename__ = "categoria_espetaculo"

	espetaculo = db.Column(db.Integer, db.ForeignKey('espetaculo.cod_espetaculo'),primary_key=True)
	categoria_espetaculo = db.Column(db.String(30),  primary_key=True)

	fk_espetaculo = db.relationship('espetaculo', foreign_keys=espetaculo)



class PRODUTO(db.Model):
	__tablename__ = "produto"

	cod_produto = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(30), nullable=False)


class CATEGORIA_PRODUTO(db.Model):
	__tablename__ = "categoria_produto"

	produto = db.Column(db.Integer, db.ForeignKey('produto.cod_produto'), primary_key=True)
	categoria_produto = db.Column(db.String(30), primary_key=True)

	fk_produto = db.relationship('produto', foreign_keys=produto)



class ENVIA_PARA(db.Model):
	__tablename__ = "envia_para"

	assinante = db.Column(db.Integer, db.ForeignKey('assinante.codpessoa'), primary_key=True)
	newsletter =  db.Column(db.Integer, db.ForeignKey('newsletter.codnewsletter'),  primary_key=True)

	fk_assinante = db.relationship('assinante', foreign_keys=assinante)
	fk_newsletter = db.relationship('newsletter', foreign_keys=newsletter)


class CONTEM(db.Model):
	__tablename__ = "contem"

	loja = db.Column(db.Integer,  db.ForeignKey('loja.codloja', primary_key=True))
	produto = db.Column(db.Integer,  db.ForeignKey('produto.cod_produto'), primary_key=True)

	fk_loja = db.relationship('loja', foreign_keys=loja)
	fk_produto = db.relationship('produto', foreign_keys=produto)
	

class SESSAO(db.Model):
	__tablename__ = "sessao"

	cod_sessao = db.Column(db.Integer, primary_key=True)
	espetaculo = db.Column(db.Integer, db.ForeignKey('espetaculo.cod_espetaculo'), primary_key=True)
	data = db.Column(db.Date,  nullable=False)
	hora = db.Column(db.Time, nullable=False)

	fk_espetaculo = db.relationship('espetaculo', foreign_keys=espetaculo)