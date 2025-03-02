
## - [NAS Projet](#nas-projet)
- [**NAS Projet**](#nas-projet)
  - [**Introduction**](#introduction)
    - [**Le prélude**](#le-prélude)
    - [**Présentation des modules principaux**](#présentation-des-modules-principaux)
      - [**discord.py**](#discordpy)
      - [**requests**](#requests)
      - [**dotenv**](#dotenv)
      - [**flask**](#flask)
  - [**Présentation du bot**](#présentation-du-bot)
    - [**Fonctionnalités**](#fonctionnalités)
      - [**Informations**](#informations)
      - [**Gestion**](#gestion)
  - [**Configurer chez vous**](#configurer-chez-vous)
    - [**Ouverture des ports**](#ouverture-des-ports)
    - [**Variables d'environnement**](#variables-denvironnement)
  - [**Hébergement**](#hébergement)
    - [**Render**](#render)
    - [**UpTimerBot**](#uptimerbot)
  - [**Crédits**](#crédits)
    - [**Arrgonn**](#arrgonn)
 

# **NAS Projet**
## **Introduction**
### **Le prélude**
Maintenant que le NAS est configuré avec les services souhaités (dans mon cas, JellyFin & Minecraft Server), il nous faut un moyen de le gérer facilement. Quoi de plus facile qu'un bot Discord !

### **Présentation des modules principaux**
#### **discord.py**
- Module de Discord nous permettant d'interagir avec le bot.
#### **requests**
 - Le module `requests` va nous servir à envoyer nos requêtes vers le serveur distant, pour vérifier son état ou l'éteindre.
#### **dotenv**
 - Module servant à protéger nos données via des variables d'environnement, à utiliser avec le module `os`.
#### **flask**
 - Module qui va nous permettre de créer une route et de pouvoir pinger le serveur lorsqu'il tourne sur le service d'hébergement afin de le maintenir en ligne.

## **Présentation du bot**
### **Fonctionnalités**
Nous allons diviser les fonctionnalités en deux parties : une partie **informations** pour obtenir des renseignements, et la partie **gestion** pour tout ce qui concerne les actions à effectuer directement sur le NAS.
#### **Informations**
- **IP [Jellyfin/Minecraft] & Server status** : Permet d'obtenir l'IP et le port du serveur, ainsi que le statut du service demandé (Jellyfin ou Minecraft).

#### **Gestion**
- **wake_up_nas** : Permet d'allumer le serveur via le WOL (Wake On LAN) en envoyant un paquet magique avec le module `wakeonlan`.
- **Stop** : Arrête le serveur.
- **killprocess** : Permet d'arrêter un processus en cours.
- **start_process** : Lance un service en utilisant le module `SSH`.


## **Configurer chez vous**
Lorsque vous allez configurer vos services, un port leur sera attribué. Faites-leur une redirection de port via votre routeur.
### **Ouverture des ports**
- Pour **Orange**, vous pouvez consulter ce guide pour savoir comment ouvrir un port sur une Livebox : [Ouvrir un port sur une Livebox Orange](https://www.worldofmicro.fr/ouvrir-un-port-sur-une-livebox-orange/)
- Pour **Free**, suivez ce guide pour ouvrir un port sur votre Freebox : [Ouvrir un port sur Freebox](https://www.touteladomotique.com/comment-ouvrir-port-freebox/)

### **Variables d'environnement**
```c
DISCORD_TOKEN=votre_discord_token
MY_SERVER=votre_nas_ip
MAC_ADRESS=votre_adresse_mac
PORT_JELLYFIN=votre_jellyfin_port
PORT_MINECRAFT=votre_minecraft_port
```
## **Hébergement**
### **Render**
### **UpTimerBot**
## **Crédits**
### [**Arrgonn**](https://github.com/Arrgonn)


