import firebase_admin
from firebase_admin import credentials, firestore

# Caminho para o arquivo de credenciais
cred = credentials.Certificate("firebase/credentials.json")

# Inicializa o app Firebase
firebase_admin.initialize_app(cred)

# Cria o cliente Firestore
db = firestore.client()