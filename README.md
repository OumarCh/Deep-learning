# Projet Deep Learning : Standford Dogs breed

Par :
- Oumar HAIDARA
- Oumar MAREGA
- Timmy KHAMSITHIDETH
- Willy DOUANGPASEUT

### Contexte
Le but de ce projet est de determiner la race d'un chien avec un photo.
Pour cela nous allons faire du Convolution Neural Network(CNN) et du TransfertLearning
### Jeu de données

http://vision.stanford.edu/aditya86/ImageNetDogs/

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
git clone git@github.com:OumarCh/Deep-learning.git
cd Deep-learning
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
cd views/standford-dog-breed
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

### Models

Pour télécharger model_dog.h5  [ici](https://drive.google.com/file/d/1ZKChkrjc2K05_G10XP7u0GFFQKpjS8FU/view?usp=sharing)
et transfert_learning.h5  [ici](https://drive.google.com/file/d/1ZKChkrjc2K05_G10XP7u0GFFQKpjS8FU/view?usp=sharing)