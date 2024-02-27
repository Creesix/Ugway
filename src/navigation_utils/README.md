# nav_utils_pkg

Ce package a pour but de rassembler les différents moyens de contrôler les mouvements du
robot. Elle ne contient pas les planners de chemin.

## cmd_vel subscriber pour robot differential

> Souscrit à cmd_vel pour convertir les commandes en vitesse en commande aux moteurs

- _Fichier :_ src/cmd_vel_differential_robot_subscriber.py
- _Include Launch :_ launch/cmd_vel.launch
- _Launch tests (avec config par défaut) :_ launch/cmd_vel_default_conf.launch

__Paramètres :__
 - `navigation_hub` : serial number du hub phidgets
 - `left_wheel_stepper` : port stepper gauche 
 - `right_wheel_stepper` : port stepper droit
 - `entraxe` : (en cm) ecart entre les deux roues
 - `wheel_radius`: (en cm) rayon des roues
 - `step_count` : nombre de steps par rotation du stepper
 - `stop_topic` : le nom du topic à écouter pour les commandes d'arrêt. Voir ci-après 
 - `speed_factor` : le nom du topic à écouter pour les commandes de variation de vitesse. Voir ci-après 
 - `tics_per_step` : tics par step sur le stepper : de combien augmente le compteur 
(du moteur) de position phidgets par steps
 - `encoder_tics_count` : nombre de tics sur l'encodeur
 - `left_wheel_encoder` : port encodeur gauche 
 - `right_wheel_encoder` : port encodeur droit
 - `odom_period` : (en s) le temps entre de mise à jour de l'estimation de l'odométrie.
La valeur minimum est égale à 5 x `encoder.getMinDataRate()` (= 20 ms soit une odomPeriod >= 100 lorsque j'écris ces lignes).
J'ai choisi fois 5 pour garantir que l'odométrie soit correcte, une odom_period proche de `encoder.getMinDataRate()` plus
l'odométrie sera mauvaise (c'est un peu la même idée que le critère de Shanon).

__Topics écoutés :__
 - stop_topic (bool) : permet d'arrêt complet des moteurs si le message publié est `True`.
 - speed_factor (float) : multiplicateur pour le speed des steppers. Peut servir pour éviter des collisions.


__Spécification des messages du serveur d'action :__

```
#goal
float64 velocity_limit
float64 distance_left
float64 distance_right
---
#result
float64 done_distance_left
float64 done_distance_right
bool done
---
#feedback
float64 distance_left_from_start
float64 distance_right_from_start
```

## waypoint trajectory

> Permet de faire déplacer le robot en ligne droite de point clef en point clef.
> Il est *très fortement* conseillé d'utiliser le contrôle des moteurs par cmd_vel : ce 
> code n'a été maintenu à jour que dans le cas où la stack navigation ne fonctionnerait pas
> correctement.

_Dépendance :_ Ce serveur d'action utilise le contrôle par distance.

- _Fichier :_ src/trajectory_action_server.py
- _Include Launch :_ launch/trajectory_follower.launch
- _Launch tests (avec config par défaut) :_ launch/trajectory_follower_default_conf.launch

__Paramètres :__
 - Voir ceux du serveur de contrôle par distance des steppers
 - `use_odom` : si le serveur doit utiliser l'odométrie ou les coordonnées du point précèdent pour calculer le déplacement
 - `trajectory_goal_error` : la tolérance sur l'arrivée (en m)
 - `start` : si la partie a commencé 
 - `is_left_side` : si le robot commence à gauche en regardant la table de face. Dans ce cas toutes 
les trajectoires sont symétrisées
 - `x_depart`, `y_depart`, `angle_depart` :  les coordonnées de départ


__Spécification des messages du serveur d'action :__

```
#goal
float64[] trajDir
float64[] trajX
float64[] trajY
---
#result
bool done
---
#feedback
float64 percentage
```

### Exemple

Voici un exemple d'utilisation du serveur.

Avec le fichier config ci-dessous, on définit notament la position de départ (x_depart, y_depart et angle_depart) et
les trajectoires. Une trajectoires est une liste de points `[le facteur de vitesse, la position en x, la position en y]`
le facteur de vitesse : s'il est négatif le robot se déplace en marche arrière, sinon en marche avant. La vitesse 
absolue est 0.1*abs(facteur de vitesse) m/s. 

```yaml
x_depart: 1
y_depart: 0.2
angle_depart: 1.57
use_odom: true # si on active l'odométrie
trajectory_goal_error: 0.1  # la tolérance sur la position d'arrivé (si l'odométrie est utilisée)

trajectoires:
   - [[1, 0.5, 0.2], [1, 0.5, 0.7], [-1, 1, 0.7], [-1, 1, 0.2]] # square
   - [[1, 0.5, 0.2], [1, 0.75, 0.7], [-1, 1, 0.2]] # triangle
```

Ajouter les lignes (en les complètant) au fichier launch :
```xml
    from launch import LaunchDescription
    from launch_ros.actions import Node
    from ament_index_python.packages import get_package_share_directory
    import os

    def generate_launch_description():
        config_trajectory = os.path.join(get_package_share_directory('pkg'), 'config', 'example_trajectories.yaml')
        config_robot = os.path.join(get_package_share_directory('pkg'), 'config', 'default_params.yaml')

        return LaunchDescription([
            Node(
                package='navigation_utils',
                executable='trajectory_follower',
                name='trajectory_follower',
                output='screen',
                parameters=[config_trajectory, config_robot]
            ),
        ])
```

**Attention :** Le serveur d'action attend que le paramètre `start` soit réglé à true et nécessite `is_left_side`

**Attention :** Il est nécessaire de publié une TF entre map et odom de sorte que map soit en (0,0)

# Auteurs

- Rémi W (2024)
