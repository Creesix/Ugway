# start_robot pkg

Ce package ROS2 humble permet d'utiliser de récupérer la stratégie donnée au robot par l'IHM, et permet le lancement du robot par activation de la tirette. C'est également dans ce package qu'est géré l'arrêt du robot lorsque le temps de jeu est écoulé

### Pour l'utiliser : 

Ajouter les dossier 'start_robot' et 'start_robot_interface' dans le dossier /src de votre workspace ROS2.

Il ne faut pas oublier de source votre environnement ROS2 :
```
source /opt/ros/humble/setup.bash
```

À la racine de votre workspace exécuter les commandes suivantes :

```
colcon build --packages-select start_robot start_robot_interface
```
```
source install/setup.bash
```
Pour tester le serveur et le client, il faut lancer les commandes suivantes dans deux terminaux distincts :
```
ros2 run start_robot client
```
```
ros2 run start_robot server
```

### Troubleshooting

Vous aurez probablement besoin d'installer la librairie "pyserial" nécessaire pour la communication série avec l'écran' :
```
pip install pyserial
```
Pour la gestion des GPIO :
```
pip install RPi.GPIO
```
