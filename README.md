# Projet Machine Learning : Summer olympic medals

Par :
- Oumar HAIDARA
- Oumar MAREGA
- Timmy KHAMSITHIDETH
- Willy DOUANGPASEUT

### Contexte
Le but de ce projet est de realiser un kmean sur un jeu de données : Summer olympic medals (1976-2008)
Partager par cluster, correler et predire etc
### Jeu de données

[data](https://www.kaggle.com/divyansh22/summer-olympics-medals) : Summer olympic medals (1976-2008)

## Configuration

### Configurer le virtualenv si nécessaire
    
La configuration d'un [virtualenv](https://virtualenv.pypa.io/en/stable/) est optionelle. Elle est recommendée si vous utilisez un IDE tel que PyCharm par exemple, afin de mieux isoler les dépendances entre celles du projet et de votre système. 
```sh
# création de l'environnement virtuel
python3 -m venv ./venv #(sur Linux / Mac)
python3 -m venv .\venv #(Sur Windows)
# activation de l'environnement
.\venv\Scripts\Activate.ps1 # (Si vous êtes sur powershell)
.\venv\Scripts\Activate.bat # (Sur tout autre shell windows)
source ./venv/bin/activate # (Linux/Mac) 
```

### Récupération du projet

```sh
git clone git@github.com:OUMAREGA/summer-olympic-medals-1976-to-2008.git
cd summer-olympic-medals-1976-to-2008
```

### Installation des dépendances
[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui
va nous permettre d'installer tout ce qui est nécessaire à ce projet.

Cette étape **n'est nécessaire que si** vous souhaitez éditer notre projet, ou démarrer notre IHM Streamlit.

Il faut exécuter la commande suivante dans le dossier `news` (de préférence sous un virtualenv) :

`pip install -r requirements.txt`

### Démarrer Flask

```
python	app.py
```

ou

```
flask run
```

### Démarrer le front-end vuejs

```
cd views/summer-olympic-medals
npm install
npm run serve
```

### Jupyter Notebooks

Dans un terminal à partir du répertoire racine du projet, exécutez la commande

```
jupyter notebook
```
ou
```
python -m jupyter notebook
```