# Phidget Stepper Controllers pkg

Ce package met à disposition des objects créant des serveurs d'action pouvant controller des steppers phidgets.

## step_controller_server

Créer le serveur d'action action_server_name et se connecte au stepper hub_serial, hub_port. Le serveur d'action
permet de controller le stepper step par step. Écoute stop_topic (arrête le moteur si stop_topic reçoit `True`).
Écoute speed_factor_topic pour moduler la vitesse du stepper.

### Importer

Importer la classe
```python
from phidget_stepper_controllers.step_controller_server import StepControllerServer
```

Importer les messages d'action. Voir ci-après pour les spécifications des différents messages.
```python
from phidget_stepper_controllers.msg import StepControllerAction, StepControllerGoal, StepControllerResult, StepControllerFeedback
```

### Création de l'objet

```python
stepper = StepControllerServer(hub_serial, hub_port, name, rescale_factor, stop_topic, speed_factor)
```

Cela créer un serveur d'action ayant pour nom `name`.

 - `hub_serial` : l'identifiant du hub
 - `hub_port` : le port du moteur
 - `name` : le nom du serveur d'action
 - `rescale_factor` (défaut: 1/32) : le factor pour mettre à l'échelle les valeurs de position/vitesse/accélération¹
 - `stop_topic` (optionnel) : le nom du topic pour forcer l'arrêt des moteurs
 - `speed_factor` (optionnel) : le topic pour moduler la vitesse

¹Par défaut, l'unité utilisée par les fonctions de phidgets est le 1/32ᵉ de step (la doc indique 1/16, 
ça dépend de la config du moteur).

### Spécifications des messages

La spécification est la suivante :
```
#goal
int64 steps_goal
int64 velocity_limit
---
#result
int64 steps_done
bool done
---
#feedback
int64 steps_from_start
```

## speed_controller_server

Créer le serveur d'action action_server_name et se connecte au stepper hub_serial, hub_port. Le serveur d'action
permet de controller le stepper en vitesse (steps/s). Écoute stop_topic (arrête le moteur si stop_topic reçoit `True`).
Écoute speed_factor_topic pour moduler la vitesse du stepper.

### Importer

Importer la classe
```python
from phidget_stepper_controllers.speed_controller_server import SpeedControllerServer
```

Importer les messages d'action. Voir ci-après pour les spécifications des différents messages.
```python
from phidget_stepper_controllers.msg import SpeedControllerAction, SpeedControllerGoal, SpeedControllerResult, SpeedControllerFeedback
```

### Création de l'objet

```python
stepper = SpeedControllerServer(hub_serial, hub_port, name, rescale_factor, stop_topic, speed_factor)
```

Cela créer un serveur d'action ayant pour nom `name`.

 - `hub_serial` : l'identifiant du hub
 - `hub_port` : le port du moteur
 - `name` : le nom du serveur d'action
 - `rescale_factor` (défaut: 1/32) : le factor pour mettre à l'échelle les valeurs de position/vitesse/accélération¹
 - `stop_topic` (optionnel) : le nom du topic pour forcer l'arrêt des moteurs
 - `speed_factor` (optionnel) : le topic pour moduler la vitesse

¹Par défaut, l'unité utilisée par les fonctions de phidgets est le 1/32ᵉ de step (la doc indique 1/16, 
ça dépend de la config du moteur).

### Spécifications des messages

La spécification est la suivante :
```
#goal
float64 velocity_limit
---
#result
bool done
---
#feedback
float64 observed_velocity
float64 theoretical_velocity
```

À cause du `speed_factor`, la vitesse envoyée au moteur est `speed_factor*velocity_limit`. `observed_velocity` est la
vitesse mesurée, `theoretical_velocity` est la vitesse "remise à l'échelle" : celle qui aurait du être mesurée si
`speed_factor` était toujours égale à 1.

# Tester ce package

- Connecter un stepper to un hub phidgets
- Configurer config/tests.yaml
- `roslaunch phidget_stepper_controllers test_step.launch`
- `roslaunch phidget_stepper_controllers test_speed.launch`

# Contraintes phidgets importantes

- Impossible d'accéder au même hub depuis deux nœuds différents
- L'unité des fonctions de position/vitesse/acceleration n'est pas le step. Il semble impossible de récupérer le
facteur directement via le code.

# TODOs

- Faire un contrôle par angle
- Tester d'ajouter un "if main" dans les fichiers de class pour pouvoir lancer un serveur depuis un launch file.
Peut-être utile, mais aura le gros désavantage de "condamner" un hub phidgets pour un stepper (cf. Contraintes phidgets importantes).

# Authors

- Sébastien K. (2024) [Contact discord](Séb#4135)

# Sources

1) La documentation de l'api phidgets est disponible dans les pdf.
2) https://roboticsbackend.com/ros-import-python-module-from-another-package/