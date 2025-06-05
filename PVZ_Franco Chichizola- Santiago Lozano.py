import pygame
import sys
import os
import random

pygame.init()
pygame.mixer.init()
reloj = pygame.time.Clock()

directorio_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(directorio_script)

# Función para cargar imágenes y que si tira error te diga cual es la imagen con error
def f_imagen(ruta_imagen, ancho=None, alto=None):
    ruta_completa = os.path.join(directorio_script, ruta_imagen)
    if not os.path.exists(ruta_completa):
        raise FileNotFoundError(f"No se encontró el archivo '{ruta_imagen}' en el directorio '{directorio_script}'")
    imagen = pygame.image.load(ruta_completa)
    if ancho and alto:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return imagen

#Funcion cargar imagenes con sprites y que si tira error te diga cual es la imagen con error
def cargar_imagenes(carpeta, ancho=None, alto=None):
    imagenes = []
    for nombre_archivo in os.listdir(carpeta):
        if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            ruta = os.path.join(carpeta, nombre_archivo)
            try:
                imagen = pygame.image.load(ruta)
                if ancho and alto:
                    imagen = pygame.transform.scale(imagen, (ancho, alto))
                imagenes.append(imagen)
            except pygame.error as e:
                print(f"Error loading image {ruta}: {e}")
    return imagenes

#costos de cada planta
lanza_costo = 100
gira_costo = 50
nuez_costo = 50
papapum_costo = 25
peta_costo = 150
repetidora_costo = 200
tripitidora_costo = 325
jala_costo = 125
pincho_costo = 100
carnivora_costo = 150
desesporada_costo = 0
cafe_costo = 75
seta_solar_costo = 25
seta_miedosa_costo = 25
seta_humo_costo = 75
petaseta_costo = 125
seta_hielo_costo = 75
hipnoseta_costo  = 75
lanza_hielo_costo = 175
#cargar musica
pygame.mixer.music.load("soundtrack/pvz_titleScreen.mp3")
sonido_podadora = pygame.mixer.Sound("soundtrack/lawnmower.wav")
sonido_DOOM = pygame.mixer.Sound("soundtrack/doomshroom.ogg")
sonido_muerte_planta = pygame.mixer.Sound("soundtrack/plantDie.ogg")
sonido_despertar_seta = pygame.mixer.Sound("soundtrack/mushroomWakeup.ogg")
sonido_victoria = pygame.mixer.Sound("soundtrack/winmusic.wav")
sonido_peta_exp = pygame.mixer.Sound("soundtrack/bomb.ogg")
sonido_humo = pygame.mixer.Sound("soundtrack/fume.ogg")
sonido_carnivora_comer = pygame.mixer.Sound("soundtrack/Chomper Eating a Zombie.mp3")
sonido_hipnosizado = pygame.mixer.Sound("soundtrack/HypnoHipnotisa.mp3")
sonido_exp_jalapeño = pygame.mixer.Sound("soundtrack/Jalapeño Explosion .mp3")
sonido_derrota = pygame.mixer.Sound("soundtrack/losemusic.wav")
sonido_grito = pygame.mixer.Sound("soundtrack/NOOOOOOOOOOO__ _ Plants vs Zombies Sound Effect(MP3_160K).mp3")
sonido_activar_papapum = pygame.mixer.Sound("soundtrack/PotatoMineActivada.mp3")
sonido_exp_papapum = pygame.mixer.Sound("soundtrack/PotatoMineExplosion.mp3")
sonido_sata_solar_crece = pygame.mixer.Sound("soundtrack/SetasolCrece.mp3")
sonido_zombi_comer1 = pygame.mixer.Sound("soundtrack/ZombieBite1 .mp3")
sonido_zombi_comer1 = pygame.mixer.Sound("soundtrack/ZombieBite2.mp3")
sonido_zombi_comer1 = pygame.mixer.Sound("soundtrack/ZombieBite3.mp3")
sonido_semilla = pygame.mixer.Sound("soundtrack/plant.wav")
sonido_plantar = pygame.mixer.Sound("soundtrack/plant2.wav")
sonido_sol = pygame.mixer.Sound("soundtrack/points.wav")
sonido_agarrar = pygame.mixer.Sound("soundtrack/tap.wav")
sonido_golpe = pygame.mixer.Sound("soundtrack/splat2.wav")
sonido_awooga = pygame.mixer.Sound("soundtrack/awooga.wav")
pygame.mixer.music.play(-1)
# Tamaño y carga de imágenes
altura_plantas = 70
ancho_plantas = 70
altura_zombi = 100
ancho_zombi = 130
altura_proyectil = 20
ancho_proyectil = 20
altura_sol = 80
ancho_sol = 80

#imagenes con frames
imagenes_lanza = cargar_imagenes('Imagenes/Peashooter',70,70)
imagenes_gira = cargar_imagenes('Imagenes/SunFlower',70,70)
imagenes_nuez = cargar_imagenes('Imagenes/WallNut',70,70)
imagenes_nuez_poco = cargar_imagenes('Imagenes/WallNut_cracked1',70,70)
imagenes_nuez_roto = cargar_imagenes('Imagenes/WallNut_cracked2',70,70)
imagenes_papapum = cargar_imagenes('Imagenes/PotatoMine',70,70)
imagenes_papapum_des = cargar_imagenes('Imagenes/PotatoMineDes',70,70)
imagenes_carnivora = cargar_imagenes('Imagenes/carnivora',100,100)
imagenes_carnivoraatk = cargar_imagenes('Imagenes/carnivoraatk',100,100)
imagenes_carnivoradig = cargar_imagenes('Imagenes/carnivoradig',100,100)
imagenes_zombi = cargar_imagenes('Imagenes/Zombie',100,130)
imagenes_zombiatk = cargar_imagenes('Imagenes/ZombieAttack',100,130)
imagenes_zombi_congelado = cargar_imagenes('Imagenes/ZombieHielo',100,130)
imagenes_zombiatk_congelado = cargar_imagenes('Imagenes/ZombieAttackHielo',100,130)
imagenes_soles = cargar_imagenes('Imagenes/Sun',80,80)
imagenes_peta = cargar_imagenes('Imagenes/CherryBomb',70,70)
imagenes_repetidora = cargar_imagenes('Imagenes/RepeaterPea',70,70)
imagenes_tripitidora = cargar_imagenes('Imagenes/Threepeater',70,70)
imagenes_jalapeño = cargar_imagenes('Imagenes/Jalapeno',70,70)
imagenes_desesporada_des = cargar_imagenes('Imagenes/PuffShroom',40,40)
imagenes_desesporada_dor = cargar_imagenes('Imagenes/PuffShroomSleep',45,70)
imagenes_pinchohierba = cargar_imagenes('Imagenes/Spikeweed',80,30)
imagenes_cafe = cargar_imagenes('Imagenes/CoffeeBean',40,70)
imagenes_jalapeño_exp = cargar_imagenes('Imagenes/jalapeno_exp',900,100)
imagenes_zombicono = cargar_imagenes('Imagenes/ConeheadZombie',100,130)
imagenes_zombiconoatk = cargar_imagenes('Imagenes/ConeheadZombieAttack',100,130)
imagenes_zombicono_congelado = cargar_imagenes('Imagenes/ConeheadZombieHielo',100,130)
imagenes_zombiconoatk_congelado = cargar_imagenes('Imagenes/ConeheadZombieAttackHielo',100,130)
imagenes_zombicubo = cargar_imagenes('Imagenes/BucketheadZombie',100,120)
imagenes_zombicuboatk = cargar_imagenes('Imagenes/BucketheadZombieAttack',100,120)
imagenes_zombicubo_congelado = cargar_imagenes('Imagenes/BucketheadZombieHielo',100,120)
imagenes_zombicuboatk_congelado = cargar_imagenes('Imagenes/BucketheadZombieAttackHielo',100,120)
imagenes_zombi_explosion = cargar_imagenes('Imagenes/BoomDie',100,130)
imagenes_proyectil_seta = cargar_imagenes('Imagenes/Proyectil/BulletMushRoom',20,20)
imagenes_proyectil_humo = cargar_imagenes('Imagenes/Proyectil/Fume',400,50)
imagenes_lanza_cong = cargar_imagenes('Imagenes/SnowPea', 70, 70)
imagenes_seta_solar = cargar_imagenes('Imagenes/SunShroom', 55, 55)
imagenes_seta_solar_grande = cargar_imagenes('Imagenes/SunShroomBig', 65, 65)
imagenes_seta_solar_dor = cargar_imagenes('Imagenes/SunShroomSleep', 55, 60)
imagenes_seta_miedosa_des = cargar_imagenes('Imagenes/ScaredyShroom', 65, 65)
imagenes_seta_miedosa_miedo = cargar_imagenes('Imagenes/ScaredyShroomCry', 65, 65)
imagenes_seta_miedosa_dor = cargar_imagenes('Imagenes/ScaredyShroomSleep', 65, 65)
imagenes_seta_humo_des = cargar_imagenes('Imagenes/FumeShroom', 70, 70)
imagenes_seta_humo_dor = cargar_imagenes('Imagenes/FumeShroomSleep', 70, 70)
imagenes_seta_humo_atk = cargar_imagenes('Imagenes/FumeShroomAttack', 85, 85)
imagenes_petaseta_des = cargar_imagenes('Imagenes/DoomShroom', 80, 80)
imagenes_petaseta_dor = cargar_imagenes('Imagenes/DoomShroomSleep', 80, 80)
imagenes_petaseta_exp = cargar_imagenes('Imagenes/DoomShroomBoom', 200, 250)
imagenes_seta_hielo_des = cargar_imagenes('Imagenes/IceShroom', 70, 70)
imagenes_seta_hielo_dor = cargar_imagenes('Imagenes/IceShroomSleep', 70, 70)
imagenes_hipnoseta_des = cargar_imagenes('Imagenes/HypnoShroom', 70, 70)
imagenes_hipnoseta_dor = cargar_imagenes('Imagenes/HypnoShroomSleep', 70, 70)
#imagenes 
imagen_proyectil = f_imagen("Imagenes/Proyectil/ProyectilPy.png", 20, 20)
imagen_huergo = f_imagen("Imagenes/huergo.png", 50, 50)
imagen_compu = f_imagen("Imagenes/Computación.png", 50, 50)
imagen_papaexp = cargar_imagenes("Imagenes/PotatoMineExplode", 100, 100)
imagenes_hole = cargar_imagenes("Imagenes/Hole", 70, 70)
imagen_BOOM = cargar_imagenes("Imagenes/BOOM", 300, 200)
imagen_game_over = f_imagen("Imagenes/Fondo/game over.png", 1000, 500)
imagen_oleada = f_imagen("Imagenes/Fondo/zombies are cumming.png", 1000, 500)
imagen_icono_pala = f_imagen("Imagenes/Pala/icono_pala.jpg", 75, 75)
imagen_pala= f_imagen("Imagenes/Pala/pala.webp", 80, 80)
imagen_podadora = f_imagen("Imagenes/podadora/podadora_0.png", 70, 60)
imagen_proyectil_cong= f_imagen("Imagenes/Proyectil/ProyectiSnow.png", 30, 30)
imagen_hielo= f_imagen("Imagenes/IceShroomTrap/IceShroomTrap_0.png", 60, 30)
#imagenes setas dormidas y despiertas
imagenes_desesporada = [imagenes_desesporada_des,imagenes_desesporada_dor]
imagenes_seta_solar = [imagenes_seta_solar,imagenes_seta_solar_dor]
imagenes_seta_miedosa = [imagenes_seta_miedosa_des,imagenes_seta_miedosa_dor]
imagenes_seta_humo = [imagenes_seta_humo_des, imagenes_seta_humo_dor]
imagenes_petaseta = [imagenes_petaseta_des, imagenes_petaseta_dor]
imagenes_seta_hielo = [imagenes_seta_hielo_des, imagenes_seta_hielo_dor]
imagenes_seta_hypno = [imagenes_hipnoseta_des, imagenes_hipnoseta_dor]
#imagenes semillas
imagen_slanza = f_imagen("Imagenes/Seeds/PeashooterSeed.png", 60, 70)
imagen_sgira = f_imagen("Imagenes/Seeds/girasolSeed.png", 60, 70)
imagen_snuez = f_imagen("Imagenes/Seeds/nuezSeed.png", 60, 70)
imagen_spapa = f_imagen("Imagenes/Seeds/papapumSeed.png", 60, 70)
imagen_speta = f_imagen("Imagenes/Seeds/petacerezaSeed.png", 60, 70)
imagen_sjala = f_imagen("Imagenes/Seeds/JalapenoSeed.png", 60, 70)
imagen_scarnivora = f_imagen("Imagenes/Seeds/ChomperSeed.png", 60, 70)
imagen_sseta_hyp = f_imagen("Imagenes/Seeds/HypnoshroomSeed.png", 60, 70)
imagen_sseta_cong = f_imagen("Imagenes/Seeds/IceShroomSeed.png", 60, 70)
imagen_sseta_desesporada = f_imagen("Imagenes/Seeds/puffshroomSeed.png", 60, 70)
imagen_sseta_miedosita = f_imagen("Imagenes/Seeds/ScaredyShroomSeed.png", 60, 70)
imagen_slanza_cong = f_imagen("Imagenes/Seeds/snowpeaSeed.png", 60, 70)
imagen_spincho = f_imagen("Imagenes/Seeds/SpikeweedSeed.png", 60, 70)
imagen_sseta_sol = f_imagen("Imagenes/Seeds/SunShroomSeed.png", 60, 70)
imagen_srepetidora = f_imagen("Imagenes/Seeds/RepeaterPeaSeed.png", 60, 70)
imagen_stripitidora = f_imagen("Imagenes/Seeds/ThreepeaterSeed.png", 60, 70)
imagen_scafe = f_imagen("Imagenes/Seeds/CafeSeed.png", 60, 70)
imagen_sseta_humo = f_imagen("Imagenes/Seeds/FumeShroomSeed.png", 60, 70)
imagen_spetaseta = f_imagen("Imagenes/Seeds/DoomshroomSeed.png", 60, 70)
#imagenes semillas cooldown
imagen_speta_cooldown = f_imagen("Imagenes/Seeds/petacerezaSeedCooldown.png", 60, 70)
imagen_spapa_cooldown = f_imagen("Imagenes/Seeds/papapumSeedCooldown.png", 60, 70)
imagen_slanza_cooldown = f_imagen("Imagenes/Seeds/PeashooterSeedCooldown.png", 60, 70)
imagen_sgira_cooldown = f_imagen("Imagenes/Seeds/girasolSeedCooldown.png", 60, 70)
imagen_snuez_cooldown = f_imagen("Imagenes/Seeds/nuezSeedCooldown.png", 60, 70)
imagen_spapa_cooldown = f_imagen("Imagenes/Seeds/papapumSeedCooldown.png", 60, 70)
imagen_speta_cooldown = f_imagen("Imagenes/Seeds/petacerezaSeedCooldown.png", 60, 70)
imagen_sjala_cooldown = f_imagen("Imagenes/Seeds/JalapenoSeedCooldown.png", 60, 70)
imagen_scarnivora_cooldown = f_imagen("Imagenes/Seeds/ChomperSeedCooldown.png", 60, 70)
imagen_sseta_hyp_cooldown = f_imagen("Imagenes/Seeds/HypnoshroomSeedCooldown.png", 60, 70)
imagen_sseta_cong_cooldown = f_imagen("Imagenes/Seeds/IceShroomSeedCooldown.png", 60, 70)
imagen_sseta_desesporada_cooldown = f_imagen("Imagenes/Seeds/puffshroomSeedCooldown.png", 60, 70)
imagen_sseta_miedosita_cooldown = f_imagen("Imagenes/Seeds/ScaredyShroomSeedCooldown.png", 60, 70)
imagen_slanza_cong_cooldown = f_imagen("Imagenes/Seeds/snowpeaSeedCooldown.png", 60, 70)
imagen_spincho_cooldown = f_imagen("Imagenes/Seeds/SpikeweedSeedCooldown.png", 60, 70)
imagen_sseta_sol_cooldown = f_imagen("Imagenes/Seeds/SunShroomSeedCooldown.png", 60, 70)
imagen_srepetidora_cooldown = f_imagen("Imagenes/Seeds/RepeaterPeaSeedCooldown.png", 60, 70)
imagen_stripitidora_cooldown = f_imagen("Imagenes/Seeds/ThreepeaterSeedCooldown.png", 60, 70)
imagen_scafe_cooldown = f_imagen("Imagenes/Seeds/CafeSeedCooldown.png", 60, 70)
imagen_sseta_humo_cooldown = f_imagen("Imagenes/Seeds/FumeShroomSeedCooldown.png", 60, 70)
imagen_spetaseta_cooldown = f_imagen("Imagenes/Seeds/DoomshroomSeedCooldown.png", 60, 70)
#conjunto semillas
semillas_lanza = (imagen_slanza, imagen_slanza_cooldown)
semillas_gira = (imagen_sgira, imagen_sgira_cooldown)
semillas_nuez = (imagen_snuez, imagen_snuez_cooldown)
semillas_papa = (imagen_spapa, imagen_spapa_cooldown)
semillas_peta = (imagen_speta, imagen_speta_cooldown)
semillas_jala = (imagen_sjala, imagen_sjala_cooldown)
semillas_carnivora = (imagen_scarnivora, imagen_scarnivora_cooldown)
semillas_seta_hyp = (imagen_sseta_hyp, imagen_sseta_hyp_cooldown)
semillas_seta_cong = (imagen_sseta_cong, imagen_sseta_cong_cooldown)
semillas_seta_desesporada = (imagen_sseta_desesporada, imagen_sseta_desesporada_cooldown)
semillas_seta_miedosita = (imagen_sseta_miedosita, imagen_sseta_miedosita_cooldown)
semillas_lanza_cong = (imagen_slanza_cong, imagen_slanza_cong_cooldown)
semillas_spincho = (imagen_spincho, imagen_spincho_cooldown)
semillas_seta_sol = (imagen_sseta_sol, imagen_sseta_sol_cooldown) 
semillas_repetidora = (imagen_srepetidora, imagen_srepetidora_cooldown)
semillas_tripitidora = (imagen_stripitidora, imagen_stripitidora_cooldown)
semillas_cafe = (imagen_scafe, imagen_scafe_cooldown)
semillas_seta_humo = (imagen_sseta_humo, imagen_sseta_humo_cooldown)
semillas_petaseta = (imagen_spetaseta, imagen_spetaseta_cooldown)

imagenes_setas = [semillas_petaseta, semillas_seta_humo,semillas_seta_desesporada,semillas_seta_miedosita,semillas_seta_sol,semillas_seta_cong,semillas_seta_hyp]
blanco = (255, 255, 255)
negro = (0, 0, 0)
font = pygame.font.SysFont(None, 36)
pygame.display.set_caption("Plants vs Zombies - Descripción de Plantas")
# Iniciar el tutorial de plantas

plantas_descripcion = [
    ("COMO JUGAR AL JUEGO 1", imagenes_zombi, 100, "Dispara guisantes a los zombis."),    
    ("COMO JUGAR AL JUEGO 2", imagenes_zombi, 100, "Dispara guisantes a los zombis."),    
    ("COMO JUGAR AL JUEGO 3", imagenes_zombi, 100, "Dispara guisantes a los zombis."),    
    ("Lanzaguisantes", imagenes_lanza, 100, "Dispara guisantes a los zombis."),
    ("Girasol", imagenes_gira, 50, "Genera soles."),
    ("Nuez", imagenes_nuez, 50, "Bloquea el avance de los zombis."),
    ("Papa-Pum", imagenes_papapum, 25, "Cuando esta activada explota cuando un zombi lo pisa."),
    ("Petacereza", imagenes_peta, 150, "Explota en un área 3x3."),
    ("Repetidora", imagenes_repetidora, 200, "Dispara dos guisantes a la vez."),
    ("Tripitidora", imagenes_tripitidora, 325, "Dispara guisantes en tres filas."),
    ("Jalapeño", imagenes_jalapeño, 125, "Quema todos los zombis en una fila."),
    ("Carnívora", imagenes_carnivora, 150, "Devora a un zombi entero."),
    ("Pinchohierba", imagenes_pinchohierba, 100, "Daña a los zombis que lo pisan."),
    ("Desesporada", imagenes_desesporada_des, 0, "Dispara esporas y tiene alcance limitado."),
    ("Seta Solar", imagenes_seta_solar[0], 25, "Genera soles pequeños y cuando crece genera soles normales."),
    ("Seta Miedosa", imagenes_seta_miedosa_des, 25, "Dispara, pero se asusta de los zombis."),
    ("Seta Humo", imagenes_seta_humo_des, 75, "Dispara humo que atraviesa a los zombis."),
    ("Petaseta", imagenes_petaseta_des, 125, "Explota matando todos los zombies y deja un hoyo donde no se pueden plantar plantas."),
    ("Seta Hielo", imagenes_seta_hielo_des, 75, "Congela a todos los zombis en pantalla."),
    ("Hipnoseta", imagenes_hipnoseta_des, 75, "hipnotiza un zombi para que luche por ti."),
]
planta_actual = 0

# Variables del juego
dia = True
ganaste = False
var_sol = 50 #soles, la moneda para comprar plantas
resolucion = [1200, 575]
screen = pygame.display.set_mode((resolucion))
fondo_dia = f_imagen("Imagenes/Fondo/fondo.png", resolucion[0], resolucion[1]) #fondo de dia
fondo_noche = f_imagen("Imagenes/Fondo/fondo_noche.jpg", resolucion[0], resolucion[1]) #fondo de noche
fondo_pantalla1 = f_imagen("Imagenes/Fondo/fondo 1-1.png",resolucion[0],resolucion[1]) #menu del dia 1-1 (primer nivel, dia)
fondo_pantalla2 = f_imagen("Imagenes/Fondo/fondo 1-2.png",resolucion[0],resolucion[1]) #menu del dia 1-2 (segundo nivel, noche)
menu_plantil = f_imagen("Imagenes/Fondo/Menuplanta.png", 650, 75) 
fondo_tutorial = f_imagen("Imagenes/Fondo/fondo tutorial.jpeg", resolucion[0], resolucion[1]) 
imagen_menu_seleccion = f_imagen("Imagenes/Fondo/panelplantaexp.png",600 ,485)
pygame.display.set_caption("Plants vs Zombies")
blanco = (255, 255, 255)
negro = (0, 0, 0)
font = pygame.font.SysFont(None, 36)
planta_actual = 0
contotototo = 0
cuadricula = []
posiciones_x = [400, 500, 600, 700, 800, 900, 1000, 1100, 1200] #posiciones de las casillas en el eje horizontal
posiciones_y = [175, 275, 375, 475, 575] #posiciones de las casillas en el eje vertical
carriles_zombi = []
proyectiles = [] #en esta lista se guardan los proyectiles que se generan
soles = [] #en esta lista se guardan los soles que se generan
tiempo_recarga1 = -1
tiempo_recarga2 = -2
tiempo_recarga3 = -3
tiempo_recarga4= -4
tiempo_recarga5 = -5
tiempo_recarga6 = -6
tiempo_recarga7 = -7
tiempo_recarga8 = -8
imagenes_semillas_plantas_seleccionadas = []
plantas_menu_seleccionadas = [None,None,None,None,None,None,None,None]
zona_muerte = 200 #en que posicion se considera game over
ultimo_sol = 0 #cuando fue el ultimo sol
sol_cooldown = 15000 #tiempo que tarda en aparecer otro sol
perdiste = False
pala_act = False
mouse_estado = False
planta_seleccionada = None
plantulis = []
zombies = []
podadoras = []
ultimo_spawn = 0
cont = 0
zombies_para_ganar = 50
zombies_cont = 0
font = pygame.font.Font(None, 30) 
font_ganaste = pygame.font.Font(None, 200) 
tiempo_interoliadas = 0
posiciones = [
    [(300, 75), (400, 75), (500, 75), (600, 75), (700, 75), (800, 75), (900, 75), (1000, 75), (1100, 75)],
    [(300, 175), (400, 175), (500, 175), (600, 175), (700, 175), (800, 175), (900, 175), (1000, 175), (1100, 175)],
    [(300, 275), (400, 275), (500, 275), (600, 275), (700, 275), (800, 275), (900, 275), (1000, 275), (1100, 275)],
    [(300, 375), (400, 375), (500, 375), (600, 375), (700, 375), (800, 375), (900, 375), (1000, 375), (1100, 375)],
    [(300, 475), (400, 475), (500, 475), (600, 475), (700, 475), (800, 475), (900, 475), (1000, 475), (1100, 475)]
]
inicio = True #esta activado cuando se esta en el menu de inicio del juego
estado_menu_seleccion = False #esta activado cuando se estan seleccionando las plantas del juego
for valor in posiciones_y:
    carriles_zombi.append(False)

#cuadricula que sirve para saber si una casilla de la cuadricula esta ocupada por una planta
for pos in posiciones:
    for filas in pos:
        cuadricula.append([filas, False,None])

# Función para encontrar la posición más cercana dentro del área de selección
def la_posicion(x, y):
    for i, filas in enumerate(posiciones):
        for pos in filas:
            if pos[0] <= x <= pos[0] + 100 and pos[1] <= y <= pos[1] + 100:
                return pos, i
    return None

def mostrar_planta(indice):
    screen.blit(fondo_tutorial,(0,0))

    # Obtener la planta actual
    nombre, imagenes, costo, descripcion = plantas_descripcion[indice]
    # Mostrar el nombre de la planta
    if indice not in (0,1,2):
        texto_nombre = font.render(f"{nombre} - {costo} soles", True, negro)
        screen.blit(texto_nombre, (50, 50))

        # Mostrar la descripción de la planta
        texto_descripcion = font.render(descripcion, True, negro)
        screen.blit(texto_descripcion, (50, 100))

        # Mostrar la imagen de la planta
        imagen = imagenes[0]  #la imagen de la planta
        screen.blit(imagen, (resolucion[0] // 2 , 200))

    
    elif indice == 0:
        texto_nombre = font.render(f"{nombre}", True, negro)
        screen.blit(texto_nombre, (50, 50))

        # Mostrar la descripción de la planta
        texto_descripcion = font.render("Objetivo del juego", True, negro)
        screen.blit(texto_descripcion, (50, 100))
        texto_descripcion = font.render("El objetivo principal de Plants vs. Zombies es detener a los zombies antes de que lleguen a tu casa.", True, negro)
        screen.blit(texto_descripcion, (50, 150))
        texto_descripcion = font.render("Para ello, deberás colocar estratégicamente diferentes tipos de plantas en tu jardín, cada una con", True, negro)
        screen.blit(texto_descripcion, (50, 200))
        texto_descripcion = font.render("habilidades y costos distintos.", True, negro)
        screen.blit(texto_descripcion, (50, 250))
        texto_descripcion = font.render("Recursos básicos: Soles", True, negro)
        screen.blit(texto_descripcion, (50, 300))
        texto_descripcion = font.render("Para poder plantar, necesitarás soles, que son el recurso principal del juego. Los soles pueden caer", True, negro)
        screen.blit(texto_descripcion, (50, 350))
        texto_descripcion = font.render("del cielo de forma aleatoria, o ser generados por plantas especiales como el Girasol o la Seta Solar.", True, negro)
        screen.blit(texto_descripcion, (50, 400))
        texto_descripcion = font.render("Sin soles, no podrás plantar más defensas, así que asegúrate de recogerlos tan pronto como aparezcan.", True, negro)
        screen.blit(texto_descripcion, (50, 450))
        texto_descripcion = font.render("SIGUE EN LA SIGUIENTE", True, negro)
        screen.blit(texto_descripcion, (50, 500))
    
    elif indice == 1:
        texto_nombre = font.render(f"{nombre}", True, negro)
        screen.blit(texto_nombre, (50, 50))

        # Mostrar la descripción de la planta
        texto_descripcion = font.render("Seleccionar Plantas (Click del Ratón): Para seleccionar una planta, simplemente haz", True, negro)
        screen.blit(texto_descripcion, (50, 150))
        texto_descripcion = font.render("click en la planta deseada en el panel superior de la pantalla. Esto la pondrá en el área de", True, negro)
        screen.blit(texto_descripcion, (50, 200))
        texto_descripcion = font.render("selección activa. Una vez seleccionada, puedes colocar la planta en el campo de juego haciendo", True, negro)
        screen.blit(texto_descripcion, (50, 250))
        texto_descripcion = font.render("clic en el lugar donde deseas plantarla.", True, negro)
        screen.blit(texto_descripcion, (50, 300))
        texto_descripcion = font.render("Colocar Plantas (Click del Ratón): Con la planta seleccionada, haz clic en la fila del", True, negro)
        screen.blit(texto_descripcion, (50, 350))
        texto_descripcion = font.render("jardín donde quieres colocarla. Asegúrate de tener suficientes soles para cubrir el costo de la", True, negro)
        screen.blit(texto_descripcion, (50, 400))
        texto_descripcion = font.render("planta. La planta se colocará en el espacio vacío de esa fila.", True, negro)
        screen.blit(texto_descripcion, (50, 450))
        texto_descripcion = font.render("SIGUE EN LA SIGUIENTE", True, negro)
        screen.blit(texto_descripcion, (50, 500))
    elif indice == 2:
        texto_nombre = font.render(f"{nombre}", True, negro)
        screen.blit(texto_nombre, (50, 50))
        texto_descripcion = font.render("Eliminar Plantas (Uso de la Pala): Si decides que una planta no está funcionando o necesitas", True, negro)
        screen.blit(texto_descripcion, (50, 150))
        texto_descripcion = font.render("reemplazarla, puedes usar la Pala. En la parte de arriba a la derecha de la pantalla, selecciona la pala.", True, negro)
        screen.blit(texto_descripcion, (50, 200))
        texto_descripcion = font.render("Luego, haz clic en la planta que deseas eliminar.", True, negro)
        screen.blit(texto_descripcion, (50, 250))
        texto_descripcion = font.render("Esto te permitirá reubicar la planta o colocar una planta diferente en ese lugar", True, negro)
        screen.blit(texto_descripcion, (50, 300))
        texto_descripcion = font.render("te permitirá reubicar la planta o colocar una planta diferente en ese lugar.", True, negro)
        screen.blit(texto_descripcion, (50, 350))
        texto_descripcion = font.render("Recoger Soles (Clic Izquierdo del Ratón): Los soles  pueden ser recogidos", True, negro)
        screen.blit(texto_descripcion, (50, 400))
        texto_descripcion = font.render("haciendo clic en ellos. Asegúrate de recogerlos lo más rápido posible para acumular más soles y", True, negro)
        screen.blit(texto_descripcion, (50, 450))
        texto_descripcion = font.render("poder plantar más defensas.", True, negro)
        screen.blit(texto_descripcion, (50, 500))
    texto_descripcion = font.render("<- TOCA LAS FLECHAS PARA AVANZAR O RETROCEDER EL TUTORIAL ->", True, negro)
    screen.blit(texto_descripcion, (100, 550))
    texto_descripcion = font.render("SALIR DEL TUTORIAL", True, negro)
    screen.blit(texto_descripcion, (975, 550))

def tutorial():
    global planta_actual
    corriendo = True

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos() 
                if 975 <= x <= 1200 and 550 <= y <= 575:
                    corriendo = False
            # moverse entre plantas con las flechitas del teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                        planta_actual = (planta_actual + 1) % len(plantas_descripcion)  # Avanzar a la siguiente planta
                if event.key == pygame.K_LEFT:
                        planta_actual = (planta_actual - 1) % len(plantas_descripcion)  # volver a la planta anterior

        
        # Mostrar la planta actual
        mostrar_planta(planta_actual)

        # Actualizar la pantalla
        pygame.display.flip()

#clases principales
class clase_sol:
    def __init__(self, x, y,produccion):
        self.x = x
        self.y = y
        self.valor = produccion
        self.velocidad = 1.5
        self.altura = 80
        self.ancho = 80
        self.girasol= False
        self.tocado = False
        self.buscar_posicion = True
        self.lugary = 1
        self.spawn = pygame.time.get_ticks()
        self.llego = False
        self.cambiosprites = 10
        self.sprites = imagenes_soles
        self.contador = 0
        self.indice_frame = 0
    
    def dibujar(self):
        screen.blit(self.sprites[self.indice_frame], (self.x-self.ancho, self.y-self.altura))
    #si pasa cierto tiempo el sol desaparece
    def desaparecer(self):
        if self.girasol:
            if self.spawn + 5000 <= pygame.time.get_ticks():
                soles.remove(self)
            if self.tocado:
                sonido_sol.play()
                soles.remove(self)                
        if not self.girasol:
            if self.llego and self.spawn + 5000 <= pygame.time.get_ticks():
                soles.remove(self)
            if self.tocado:
                sonido_sol.play()
                soles.remove(self)

    def mover(self):
        #si no es creado por una planta, que caiga del cielo
        if not self.girasol:
            if self.buscar_posicion:
                self.x = random.choice(posiciones_x)
                self.lugary = random.choice(posiciones_y)
                self.buscar_posicion = False

            if self.y < self.lugary:
                self.y += self.velocidad
                self.llego = True
                self.spawn = pygame.time.get_ticks()
    
    def dibujar_sprites(self):
        self.contador += 1 #por cada frame que pasa (60 por segundo) se le suma uno a ese contador
        if self.contador >= self.cambiosprites: #cuando el numero llega a cierto nuemero, el frame de la planta canbia
            self.contador = 0 # se reinicia el contador
            self.indice_frame += 1 #se le cambia de frame a la planta
            if self.indice_frame >= len(self.sprites): #si recorre todas la imagenes, se reinicia desde cero
                self.indice_frame = 0  

class Proyectil:
    def __init__(self, x, y, linea, daño,desesporada):
        self.nombre = "normal"
        self.x = x
        self.y = y
        self.x_inicial = x
        self.desesporada = desesporada
        self.imagen = imagen_proyectil
        self.velocidad = 5
        self.altura = 10
        self.ancho = 10
        self.daño = daño
        self.linea = linea

    def dibujar(self):
        screen.blit(self.imagen, (self.x, self.y))

    def mover(self):
        #si no es un proyectil "humo", que se mueva
        if not self.nombre == "humo":
            self.x += self.velocidad
   
    def fuera_de_rango(self):
        #si es creada por una seta desesporada, si el disparo llega a mas de 4 casilla desaparezca
        if self.desesporada:
            if self.x_inicial + 400 <= self.x:
                proyectiles.remove(self)
        #si es del tipo humo, que luego de hacer su animacion desaparezca
        if self.nombre == "humo":
            if self.indice_frame == len(self.sprites) -1:
                proyectiles.remove(self)
    def dibujar_sprites(self):
        #si es del tipo de proyectiles con animaciones que lo haga
        if self.nombre == "seta" or self.nombre == "humo":
            self.contador += 1 #por cada frame que pasa (60 por segundo) se le suma uno a ese contador
            if self.contador >= self.cambiosprites: #cuando el numero llega a cierto nuemero, el frame de la planta canbia
                self.contador = 0 # se reinicia el contador
                self.indice_frame += 1 #se le cambia de frame a la planta
                if self.indice_frame >= len(self.sprites): #si recorre todas la imagenes, se reinicia desde cero
                    self.indice_frame = 0  
    

 
    #ver si el proyectil colisionó con algun zombi
    def golpeo(self):
        if self.nombre == "normal": 
                for zombi in zombies:
                    if zombi.x + 20 <= self.x <= zombi.x + altura_zombi and zombi.linea == self.linea and not zombi.explosivo and not zombi.aliado:
                        zombi.vida -= self.daño
                        sonido_golpe.play()
                        proyectiles.remove(self)
                        break
        #este ademas congela a los zombies, relentizandolos
        if self.nombre == "congelado": 
            for zombi in zombies:
                if zombi.x + 20 <= self.x <= zombi.x + altura_zombi and zombi.linea == self.linea and not zombi.explosivo and not zombi.aliado:
                    zombi.vida -= self.daño
                    zombi.congelado = True
                    zombi.cont = 0
                    sonido_golpe.play()
                    proyectiles.remove(self)
                    break
        #es lo mismo que el primero pero es diferente el sprite
        elif self.nombre == "seta":
            for zombi in zombies:
                if zombi.x + 20 <= self.x <= zombi.x + altura_zombi and zombi.linea == self.linea and not zombi.explosivo and not zombi.aliado:
                    zombi.vida -= self.daño
                    sonido_golpe.play()
                    proyectiles.remove(self)
                    break
        #se queda quieto y si un zombi pasa lo atravieza y le pega a los demas
        elif self.nombre == "humo":
            for zombi in zombies:
                if zombi.x + 20 <= self.x <= zombi.x + 400 and zombi.linea == self.linea and not zombi.explosivo and not zombi.aliado:
                        zombi.vida -= self.daño

class Plantas:
    def __init__(self, x, y, linea):
        self.nombre = None
        self.x = x 
        self.y = y
        self.vida = 1
        self.vida_permanente = self.vida
        self.daño = 1
        self.golpe = pygame.time.get_ticks() #cuando fue su ultimo golpe, se usa para el cooldown de los ataques
        self.spawn = pygame.time.get_ticks() #momento en que se genero la planta
        self.imagen = None 
        self.ancho = ancho_plantas #el ancho y alto de las plantas
        self.alto = altura_plantas
        self.seleccionada = False # si esta seleccionada por el mouse 
        self.linea = linea #en que linea esta, 1,2,3,4,5
        self.produccion = 0 #si produce soles cuanto produce
        self.ultima_produccion = 0 #cuando fue su ultima generacion de sol, se usa para el cooldown de la produccion
        self.cooldown = 1 
        self.cambiosprites = 0 #cada cuantos frames cambia de imagen
        self.sprites = None #las imagenes de la animacion
        self.contador = 0
        self.indice_frame = 0 #en que posicion de los sprites esta
        self.partes = False #si tiene varias partes o sprites
        self.hostil = False #si dispara a los zombies
        self.cont = 0
        self.activada = False #si es una papapum, saber si ya esta preparada para explotar
        self.explotada = False #si es una planta explosiva para saber si ya exploto
        self.tiempo_explosion = 0 #en que momento exploto
        self.contator = 0
        self.num_recarga = 0 #que numero de recarga le corresponde para poder saber cuanto tiempo se tiene que esperar para la siguiente planta
        self.intangible = False #si los zombies pueden comerla
        self.comiendo = False #si es una carnivora saber si esta comiendo un zombi
        self.seta = False #si es una seta (las setas suermen de dia)
        self.dormida = False # si es una seta, para saber si esta dormida

    def comprobar(self):
        #comprobar si hay un zombi en su linea para saber si hay que disparar
        for zombi in zombies:
            if zombi.linea == self.linea and zombi.x >= self.x and not zombi.aliado: 
                return True
        return False

    #los ataques de cada planta (con algunas son acciones que realizan acciones)
    def atacar(self):
        hay_zombies = self.comprobar()
        #como es un lazaguisantes, dispara un guisante normal
        if self.nombre == "lanza":
            if hay_zombies and self.golpe <= pygame.time.get_ticks() and self.hostil:
                proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20, self.linea, self.daño, False)
                proyectiles.append(proyectil)
                self.golpe = pygame.time.get_ticks() + self.cooldown
        #como es un lanzaguisantes de hielo. tira guisantes de hielo
        if self.nombre == "lanza_hielo":
            if hay_zombies and self.golpe <= pygame.time.get_ticks() and self.hostil:
                proyectil = proyectil_congelado(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20, self.linea, self.daño, False)
                proyectiles.append(proyectil)
                self.golpe = pygame.time.get_ticks() + self.cooldown
        #tira esporas con rango limitado
        if self.nombre == "desesporada":
            for zombi in zombies:
                if self.x <= zombi.x <= self.x + 300 and self.linea == zombi.linea and self.golpe <= pygame.time.get_ticks() and not self.dormida and not zombi.aliado:
                    proyectil = proyectil_seta(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 +15, self.linea, self.daño,True)
                    proyectiles.append(proyectil)
                    self.golpe = pygame.time.get_ticks() + self.cooldown 
        #tira una especie de humo que daña a los zombies que esten en este
        if self.nombre == "humo":
            if self.sprites == self.sprites_atk and self.indice_frame == 8 and self.golpe <= pygame.time.get_ticks():
                proyectil = proyectil_humo(self.x + self.ancho / 2 + 30, self.y -10, self.linea, self.daño,False)
                proyectiles.append(proyectil)
                sonido_humo.play()
                self.golpe = pygame.time.get_ticks() + 500 
        #dispara esporas 
        if self.nombre == "miedosa":
            for zombi in zombies:
                if self.x <= zombi.x and self.linea == zombi.linea and self.golpe <= pygame.time.get_ticks() and not self.dormida and not self.asustada and not zombi.aliado:
                    proyectil = proyectil_seta(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 , self.linea, self.daño,False)
                    proyectiles.append(proyectil)
                    self.golpe = pygame.time.get_ticks() + self.cooldown
        #explota si tiene un zombi cercano y esta activada
        elif self.nombre == "papapum":
            for zombi in zombies:
                if self.x < zombi.x < self.x + 10 and zombi.linea == self.linea and self.activada and not self.explotada and not zombi.aliado:
                    self.indice_frame = 0
                    self.sprites = imagen_papaexp
                    self.explotada = True
                    sonido_exp_papapum.play()
                    self.tiempo_explosion = pygame.time.get_ticks()
                    zombi.vida -= self.daño
        #disapara dos guisantes normales
        elif self.nombre == "repetidora":
            if hay_zombies and self.golpe <= pygame.time.get_ticks() and self.hostil:
                if self.contator == 1:
                    proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20, self.linea, self.daño, False)
                    proyectiles.append(proyectil)
                    self.golpe = pygame.time.get_ticks() + self.cooldown
                    self.contator = 0
                elif self.contator == 0:
                    proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20, self.linea, self.daño, False)
                    proyectiles.append(proyectil)
                    self.golpe = pygame.time.get_ticks() + 200
                    self.contator = 1       
        #dispara guisantes en la linea de arriba,en su linea y la de abajo
        elif self.nombre == "tripitidora":
            for zombi in zombies:
                if self.linea == 0:
                    if self.golpe <= pygame.time.get_ticks() and self.hostil and zombi.linea in (0, 1) and not zombi.aliado:
                        proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20, self.linea, self.daño, False)
                        proyectiles.append(proyectil)
                        proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20 + 100, self.linea + 1, self.daño, False)
                        proyectiles.append(proyectil)
                        self.golpe = pygame.time.get_ticks() + self.cooldown
                elif self.linea in (2, 3, 1) and not zombi.aliado:
                    if self.golpe <= pygame.time.get_ticks() and self.hostil and zombi.linea in (self.linea + 1, self.linea, self.linea - 1):
                        proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20, self.linea, self.daño, False)
                        proyectiles.append(proyectil)
                        proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20 + 100, self.linea + 1, self.daño, False)
                        proyectiles.append(proyectil)
                        proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20 - 100, self.linea - 1, self.daño, False)
                        proyectiles.append(proyectil)
                        self.golpe = pygame.time.get_ticks() + self.cooldown                   
                else:
                    if self.golpe <= pygame.time.get_ticks() and self.hostil and zombi.linea in (3, 4) and not zombi.aliado:
                        proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20, self.linea, self.daño, False)
                        proyectiles.append(proyectil)
                        proyectil = Proyectil(self.x + self.ancho / 2 + 30, self.y + self.alto / 2 - 20 - 100, self.linea - 1, self.daño, False)
                        proyectiles.append(proyectil)
                        self.golpe = pygame.time.get_ticks() + self.cooldown
        #si un zombi pasa sobre ella le hace daño
        if self.nombre == "pinchohierba":
            for zombi in zombies:
                if self.x-100 <= zombi.x <= self.x and self.golpe <= pygame.time.get_ticks() and zombi.linea == self.linea and not zombi.aliado:
                    zombi.vida -= self.daño 
                    self.golpe = pygame.time.get_ticks() + self.cooldown
        #se come a los zombies
        if self.nombre == "carnivora":
            for zombi in zombies:
                if self.x <= zombi.x <= self.x + 130 and self.golpe <= pygame.time.get_ticks() and not self.comiendo and zombi.linea == self.linea and not zombi.aliado:
                    self.indice_frame = 0
                    self.sprites = imagenes_carnivoraatk
                    self.comiendo = True
                    sonido_carnivora_comer.play()
                    zombies.remove(zombi) 
                    break
        #despierta a las setas ya que duermen al ponerlas
        if self.nombre == "cafe":
            if self.explotada:
                for i,plantita in enumerate(plantulis):
                    if self.x <= plantita.x <= self.x + 80 and plantita.linea == self.linea:
                        if plantita.seta and plantita.dormida:
                            plantulis[i].despertar()
                plantulis.remove(self)            
                
    def dibujar(self):
        self.dibujar_sprites()
        screen.blit(self.sprites[self.indice_frame], (self.x, self.y))

    def comprobar_vida(self):
        #comprueba la vida y si se muere, restaura la casilla que se estaba utilizando
        if self.vida <= 0:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
                    cuadricula[i][2] = None
            plantulis.remove(self)

    def generar_sol(self):
        if self.produccion != 0 and self.ultima_produccion <= pygame.time.get_ticks() and not self.dormida:
            if self.spawn + self.cooldown <= pygame.time.get_ticks():
                self.ultima_produccion = pygame.time.get_ticks() + self.cooldown
                sol = clase_sol(self.x+self.ancho+15,self.y+self.alto,self.produccion)
                sol.girasol = True
                soles.append(sol)
    def dibujar_sprites(self):
        self.contador += 1 #por cada frame que pasa (60 por segundo) se le suma uno a ese contador
        if self.contador >= self.cambiosprites: #cuando el numero llega a cierto nuemero, el frame de la planta canbia
            self.contador = 0 # se reinicia el contador
            self.indice_frame += 1 #se le cambia de frame a la planta
            if self.indice_frame >= len(self.sprites): #si recorre todas la imagenes, se reinicia desde cero
                self.indice_frame = 0  
    def cargar_partes(self):
        if self.partes:
            #la nuez al perder vida cambia de fases
            if self.nombre == "nuez":
                if self.vida > 2* self.vida_permanente / 3:
                    self.sprites = imagenes_nuez
                elif self.vida <= 2* self.vida_permanente / 3 and self.vida > self.vida_permanente / 3:
                    self.sprites = imagenes_nuez_poco
                else:
                    self.sprites = imagenes_nuez_roto
            #activar a la papapum para que pueda explotar
            elif self.nombre == "papapum":
                if self.spawn + self.cooldown <= pygame.time.get_ticks() and self.cont == 0:
                    self.indice_frame = 0
                    self.activada = True
                    self.vida = 100
                    self.sprites = imagenes_papapum
                    sonido_activar_papapum.play()
                    self.cont += 1
            #hacer crecer a la seta solar, para que genere mas soles
            elif self.nombre == "solar":
                if not self.dormida and self.tiempo_despierta + self.crecimiento <= pygame.time.get_ticks() and self.cont == 0:
                    self.indice_frame = 0
                    self.activada = True
                    self.sprites = imagenes_seta_solar_grande
                    sonido_sata_solar_crece.play()
                    self.produccion = 25
                    self.cont += 1
            #se esconde cuando se le acercan zombies
            elif self.nombre == "miedosa":
                self.contator = 0
                if not self.dormida:
                    for zombi in zombies:
                        if self.x -150 <= zombi.x <= self.x +100 and not self.dormida and zombi.linea in (self.linea+1,self.linea,self.linea-1) and not zombi.aliado:
                            self.contator += 1 
                    if self.contator != 0 and self.cont == 1:
                        self.indice_frame = 0
                        self.asustada = True
                        self.sprites = imagenes_seta_miedosa_miedo
                        self.cont = 0

                    if self.cont == 0 and self.contator == 0:
                        self.indice_frame = 0
                        self.asustada = False 
                        self.sprites = imagenes_seta_miedosa_des
                        self.cont = 1


    def explosion(self):
        #si es una planta explosiva, al hacer sus animaciones que exploten
        #explota en un radio de 3x3 casillas matando a todos los zombies
        if self.nombre == "peta":
            if self.indice_frame == 6:
                self.explotada = True
                self.tiempo_explosion = pygame.time.get_ticks()
                self.indice_frame = 0 
                self.sprites = imagen_BOOM
                sonido_peta_exp.play()
                for zombi in zombies:
                    if self.linea == 0:
                        if zombi.linea == self.linea or zombi.linea == self.linea + 1 and not zombi.aliado:
                            if self.x-150 <= zombi.x <= self.x +150:
                                zombi.indice_frame = 0
                                zombi.sprites = imagenes_zombi_explosion
                                zombi.explosivo = True
                    if self.linea == 2 or self.linea == 3 or self.linea == 1 :
                        if zombi.linea == self.linea or zombi.linea == self.linea + 1 or zombi.linea == self.linea - 1 and not zombi.aliado:
                            if self.x-150 <= zombi.x <= self.x +150:
                                zombi.indice_frame = 0
                                zombi.sprites = imagenes_zombi_explosion
                                zombi.explosivo = True
                    if self.linea == 4:
                        if zombi.linea == self.linea or zombi.linea == self.linea - 1 and not zombi.aliado:
                            if self.x-150 <= zombi.x <= self.x +150:
                                zombi.indice_frame = 0
                                zombi.sprites = imagenes_zombi_explosion
                                zombi.explosivo = True
        #explota y mata a todos los zombies de su linea
        elif self.nombre == "jala":
            if self.indice_frame == 7:
                self.explotada = True
                self.tiempo_explosion = pygame.time.get_ticks()
                self.indice_frame = 0 
                self.sprites = imagenes_jalapeño_exp
                sonido_exp_jalapeño.play()
                for zombi in zombies:
                    if self.linea == zombi.linea and not zombi.aliado:
                                zombi.indice_frame = 0
                                zombi.sprites = imagenes_zombi_explosion
                                zombi.explosivo = True
        #explota y mata a todos los zombies
        elif self.nombre == "petaseta":
            if self.indice_frame == 9 and self.sprites == imagenes_petaseta[0]:
                self.explotada = True
                self.tiempo_explosion = pygame.time.get_ticks()
                self.indice_frame = 0 
                self.sprites = imagenes_petaseta_exp
                sonido_DOOM.play()
                for zombi in zombies:
                    if not zombi.aliado:
                        zombi.indice_frame = 0
                        zombi.sprites = imagenes_zombi_explosion
                        zombi.explosivo = True
            elif self.indice_frame == 9 and self.sprites == imagenes_petaseta_exp:
                self.indice_frame = 0
                self.intangible = True
                self.sprites = imagenes_hole
                self.cambiosprites = 5400
        #explota y congela a todos los zombies
        elif self.nombre == "seta_hielo":
            if self.indice_frame == 10 and self.sprites == imagenes_seta_hielo[0]:
                self.explotada = True
                self.tiempo_explosion = pygame.time.get_ticks()
                self.indice_frame = 0 
                for zombi in zombies:
                    if not zombi.aliado:
                        zombi.indice_frame = 0
                        zombi.congelado_parado = True
                        self.cont = 0
                        zombi.congelado = True
        #no explota, cuando se terminan las animaciones, despierta a la planta que se selecciono
        elif self.nombre == "cafe":
            if self.indice_frame == 7:
                self.explotada = True
        #no explota pero al completar sus sprites puede volver a comer a otro zombi
        elif self.nombre == "carnivora":
            if self.comiendo:
                if self.indice_frame == 8 and self.sprites == imagenes_carnivoraatk:
                    self.indice_frame = 0 
                    self.sprites = imagenes_carnivoradig
                    self.tiempo_explosion = pygame.time.get_ticks() 
                if  imagenes_carnivoradig == self.sprites and self.tiempo_explosion + self.cooldown_r <= pygame.time.get_ticks():
                    self.indice_frame = 0 
                    self.sprites = imagenes_carnivora              
                    self.comiendo = False
        #no explota pero cuando completa sus sprites, lanza un proyectil (esta hecho para que quede mas coordinado con el ataque)
        elif self.nombre == "humo":
            self.cont = 0
            for zombi in zombies:
                if self.x <= zombi.x <= self.x + 400 and self.linea == zombi.linea and not self.dormida and not zombi.aliado:
                    self.cont += 1
            if self.cont != 0 and self.contator == 0:     
                self.comiendo = True
                self.indice_frame = 0
                self.sprites = self.sprites_atk 
                self.contator = 1
            if self.cont == 0 and self.contator == 1:     
                self.comiendo = False
                self.indice_frame = 0
                self.sprites = self.sprites_despierta
                self.contator = 0

class Zombies:
    def __init__(self, x, y, linea):
        self.x = x
        self.y = y
        self.vida = 1
        self.daño = 1
        self.golpe = pygame.time.get_ticks()
        self.velocidad = 1
        self.cooldown = 1000
        self.imagen = None
        self.ancho = ancho_zombi #el ancho y alto de las plantas
        self.alto = altura_zombi
        self.linea = linea #en que linea esta, 1,2,3,4,5
        self.comiendo = False #si esta comiendo una planta
        self.cambiosprites = 0 
        self.sprites = None
        self.contador = 0
        self.indice_frame = 0
        self.cambio = False #se para saber si cambio para ejecutar los sprites de explosion
        self.congelado = False #si esta congelado, lo relentiza 
        self.planta_comiendo = None #que planta esta comiendo
        self.explosivo = False #si fue explotado por alguna planta
        self.sprites_moviendo = None #sus sprites cuando se mueve
        self.sprites_comiendo = None #sus sprites cuando come
        self.sprites_moviendo_inv = [] #si esta hipnotiza sus sprites cuando se mueve
        self.sprites_comiendo_inv = [] #si esta hipnotiza sus sprites cuando come
        self.cont = 0
        self.congelado_parado = False #si fue congelado totalmente y no puede ni comer ni caminar
        self.tiempo_congelado = 0 #en que momento fue congelado
        self.conta = 0
        self.aliado = False #si fue hipnotizado
    def dibujar_sprites(self):
        self.contador += 1 #por cada frame que pasa (60 por segundo) se le suma uno a ese contador
        if self.contador >= self.cambiosprites: #cuando el numero llega a cierto nuemero, el frame de la planta canbia
            self.contador = 0 # se reinicia el contador
            self.indice_frame += 1 #se le cambia de frame a la planta
            if self.indice_frame >= len(self.sprites): #si recorre todas la imagenes, se reinicia desde cero
                self.indice_frame = 0  

    def dibujar(self):
        if not self.congelado_parado:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
        elif self.congelado_parado:
            screen.blit(self.sprites_moviendo_congelado[0],(self.x, self.y)) # si se quedo congelado que no se puede mover, sus sprites se quedan quietos
    def atacar(self):
        #el ataque hacia las plantas y zombies hipnotizados
        if not self.explosivo:
            if not self.aliado:
                for planta in plantulis:
                    if planta.x + 10 >= self.x >= planta.x - ancho_plantas and planta.linea == self.linea and not planta.intangible and not self.congelado_parado:
                        self.comiendo = True
                        self.planta_comiendo = planta
                        self.velocidad = 0
                        if pygame.time.get_ticks() - self.golpe >= self.cooldown:
                            #si come la hipnoseta, se hipnotiza
                            if planta.nombre == "hipnoseta" and not planta.dormida:
                                sonido_hipnosizado.play()
                                #hacer que camine para atras
                                self.velocidad_inicial = -self.velocidad_inicial
                                #cargar imagenes inversas
                                for imagen in self.sprites_comiendo:
                                    imagen = pygame.transform.flip(imagen, True, False)
                                    self.sprites_comiendo_inv.append(imagen)
                                for imagen in self.sprites_moviendo:
                                    imagen = pygame.transform.flip(imagen, True, False)
                                    self.sprites_moviendo_inv.append(imagen)
                                self.aliado = True #esta hipnotizado
                                planta.vida -= 100
                            self.golpe = pygame.time.get_ticks() # su ultimo golpe
                            planta.vida -= self.daño #que haga daño
                #saber si esta comiendo o ya termino
                    if self.planta_comiendo not in plantulis:
                        self.comiendo = False
                if len(plantulis) == 0:
                    self.comiendo = False
                if not self.aliado:    
                    for zombi in zombies:
                        if zombi.x - ancho_zombi <= self.x <= zombi.x  and zombi.linea == self.linea and zombi.aliado:
                            self.comiendo = True
                            self.planta_comiendo = zombi #para reutilizar el codigo y variables aunque diga planta se refiere a zombi
                            self.velocidad = 0
                            if pygame.time.get_ticks() - self.golpe >= self.cooldown:
                                self.golpe = pygame.time.get_ticks()
                                zombi.vida -= self.daño      

        #reiniciar las velocidades segun lo congelado que esta
            if not self.comiendo:
                if self.congelado and not self.congelado_parado:
                    self.cooldown = self.cooldown_congelado
                    self.velocidad = self.velocidad_congelado
                elif self.congelado and self.congelado_parado:
                    self.velocidad = 0
                    screen.blit(imagen_hielo,(self.x+40,self.y+100))
                elif not self.congelado:
                    self.cooldown = self.cooldown_inicial
                    self.velocidad = self.velocidad_inicial
            #si el zombi esta hipnotizado que coma a los zombies de su bando
            if self.aliado:
                #cancelar los efectos de congelamiento
                self.congelado = False
                self.congelado_parado = False
                #atacar a los zombies
                for zombi in zombies:
                    if zombi.x + altura_zombi >= self.x >= zombi.x and zombi.linea == self.linea and not zombi.aliado:
                        self.comiendo = True
                        self.planta_comiendo = zombi #para reutilizar el codigo y variables aunque diga planta se refiere a zombi
                        self.velocidad = 0
                        if pygame.time.get_ticks() - self.golpe >= self.cooldown:
                            self.golpe = pygame.time.get_ticks()
                            zombi.vida -= self.daño      
                    #terminar de comer al zombi
                    if self.planta_comiendo not in zombies:
                        self.comiendo = False

    def mover(self):
        if not self.explosivo:
            self.x -= self.velocidad
        
    def esta_congelado(self):
        #el estado de congelamiento no es infinito y esto cancela el estado despues de cierto tiempo
        if self.explosivo:
            self.congelado_parado = False
            self.congelado = False
        if not self.congelado_parado:
            if self.congelado and self.cont == 0:
                self.tiempo_congelado = pygame.time.get_ticks()
                self.cont = 1 #para que no se repita varias veces
            if self.congelado and self.cont == 1 and self.tiempo_congelado + 20000 <= pygame.time.get_ticks():
                self.congelado = False
                self.cont = 0 #para que no se repita varias veces
        else:
            if self.congelado_parado and self.conta == 0:
                self.tiempo_congelado_parado = pygame.time.get_ticks() + 5000 
                self.conta = 1 #para que no se repita varias veces
            elif self.congelado and self.conta == 1 and self.tiempo_congelado_parado <= pygame.time.get_ticks():
                self.congelado_parado = False
                self.conta = 0 #para que no se repita varias veces
    def comprobar_vida(self):
        #¿sigue con vida?
        if not self.explosivo:
            if self.vida <= 0:
                zombies.remove(self)
        elif self.indice_frame == 19:
            zombies.remove(self)
    def perder(self):
        #cuando un zombi pasa cierta zona, perdiste el juego
        global perdiste
        if self.x <= zona_muerte:
            perdiste = True
            sonido_derrota.play()
            sonido_grito.play()
            
    def esta_comiendo(self):
        if not self.explosivo:
            if self.comiendo:
                if self.cambio:
                    self.indice_frame = 0
                    self.cambio = False
                self.sprites = self.sprites_comiendo if not self.congelado else self.sprites_comiendo_congelado   #que elija los sprites normales a menos que este congelado
                if self.aliado:
                    self.sprites = self.sprites_comiendo_inv # si esta hipnotizado que use los sprites inversos 
            else:
                if not self.cambio:
                    self.indice_frame = 0
                    self.cambio = True 
                self.sprites = self.sprites_moviendo if not self.congelado else self.sprites_moviendo_congelado  #que elija los sprites normales a menos que este congelado 
                if self.aliado:
                    self.sprites = self.sprites_moviendo_inv # si esta hipnotizado que use los sprites inversos 
# Clases secundarias
#es otro tipo de pryectil que es una espora, tiene animacion
class proyectil_seta(Proyectil):
    def __init__(self, x, y, linea, daño, desesporada):
        super().__init__(x, y, linea, daño, desesporada)    
        self.nombre = "seta"
        self.daño = daño
        self.x = x
        self.y = y
        self.sprites = imagenes_proyectil_seta
        self.indice_frame = 0
        self.contador = 0
        self.cambiosprites = 10

    def dibujar(self):
        screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
#es otro tipo de pryectil que es un humo que se queda fijo y tiene animacion
class proyectil_humo(Proyectil):
    def __init__(self, x, y, linea, daño, desesporada):
        super().__init__(x, y, linea, daño, desesporada)    
        self.nombre = "humo"
        self.daño = daño
        self.x = x
        self.y = y
        self.sprites = imagenes_proyectil_humo
        self.indice_frame = 0
        self.contador = 0
        self.cambiosprites = 7

    def dibujar(self):
        screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
#es otro tipo de pryectil que es un guisante congelado, de el estado de congelados a los zombies
class proyectil_congelado(Proyectil):
    def __init__(self, x, y, linea, daño, desesporada):
        super().__init__(x, y, linea, daño, desesporada)    
        self.nombre = "congelado"
        self.daño = daño
        self.x = x
        self.y = y
        self.imagen = imagen_proyectil_cong
#tipo de planta seta, esta duerme de dia y se necesita un cafe para despertarlas
class setas(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.seta = True # si es una seta
        self.dormida = True if dia else False #si esta dormida
        self.tiempo_despierta = pygame.time.get_ticks() #momento en el que se desperto
    #metodo para despertar a la planta
    def despertar(self):
        self.sprites = self.sprites_despierta  
        self.dormida = False
        self.indice_frame = 0  
        self.tiempo_despierta = pygame.time.get_ticks()
        sonido_despertar_seta.play()

# Clases de plantas y zombies 
class Lanzaguisantes(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "lanza"
        self.vida = 100
        self.daño = 20
        self.hostil = True
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 2500
        self.imagen = imagenes_lanza[0]
        self.costo = 100
        self.cambiosprites = 6
        self.sprites = imagenes_lanza  
        self.recarga = 7500

class Girasol(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "gira"
        self.vida = 100
        self.daño = 0
        self.imagen = imagenes_gira[0]
        self.costo = 50
        self.cooldown = 10000
        self.produccion = 25
        self.cambiosprites = 6
        self.sprites = imagenes_gira
        self.recarga = 7500

class Nuez(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "nuez"
        self.vida = 1500
        self.vida_permanente = 1500
        self.daño = 0
        self.imagen = imagenes_nuez[0]
        self.costo = 50
        self.cooldown = 10000
        self.cambiosprites = 6
        self.sprites = imagenes_nuez
        self.partes = True
        self.recarga = 30000

class papapum(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "papapum"
        self.vida = 100
        self.vida_permanente = 100
        self.daño = 500
        self.imagen = imagenes_papapum[0]
        self.costo = 25
        self.cooldown = 15000
        self.cambiosprites = 8
        self.sprites = imagenes_papapum_des
        self.partes = True
        self.recarga = 30000
        self.intangible = False

    def dibujar(self):
        if not self.explotada:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
        else:
            self.intangible = True 
            screen.blit(self.sprites[self.indice_frame], (self.x-30, self.y-30))
    
    def comprobar_vida(self):
        if self.vida <= 0 :
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
            plantulis.remove(self)
        elif self.tiempo_explosion + 1000<= pygame.time.get_ticks() and self.explotada:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
            plantulis.remove(self)            

class petacereza(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "peta"
        self.vida = float("inf")
        self.vida_permanente = 1000
        self.daño = 500
        self.imagen = imagenes_peta[0]
        self.costo = 150
        self.cooldown = 15000
        self.cambiosprites = 10
        self.sprites = imagenes_peta
        self.recarga = 50000
    def dibujar(self):
        self.dibujar_sprites()
        if not self.explotada:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
        else:
            screen.blit(self.sprites[self.indice_frame], (self.x-100, self.y-50))

    def comprobar_vida(self):
        if self.tiempo_explosion + 1000<= pygame.time.get_ticks() and self.explotada:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
            plantulis.remove(self)  

class jalapeño(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "jala"
        self.vida = float("inf")
        self.vida_permanente = 1000
        self.daño = 500
        self.imagen = imagenes_jalapeño[0]
        self.costo = 125
        self.cooldown = 15000
        self.cambiosprites = 10
        self.sprites = imagenes_jalapeño
        self.recarga = 50000
    def dibujar(self):
        self.dibujar_sprites()
        if not self.explotada:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
        else:
            screen.blit(self.sprites[self.indice_frame], (300, self.y-30))

    def comprobar_vida(self):
        if self.tiempo_explosion + 1000<= pygame.time.get_ticks() and self.explotada:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
                    cuadricula[i][2] = None
            plantulis.remove(self)  

class Repetidora(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "repetidora"
        self.vida = 100
        self.daño = 10
        self.hostil = True
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 2500
        self.imagen = imagenes_repetidora[0]
        self.costo = 200
        self.cambiosprites = 5
        self.sprites = imagenes_repetidora
        self.recarga = 7500 

class carnivora(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "carnivora"
        self.vida = 100
        self.daño = 10
        self.hostil = True
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 1000
        self.cooldown_r = 15000
        self.imagen = imagenes_carnivora[0]
        self.costo = 150
        self.cambiosprites = 7
        self.sprites = imagenes_carnivora
        self.recarga = 7500 
    def dibujar(self):
        self.dibujar_sprites()
        screen.blit(self.sprites[self.indice_frame], (self.x, self.y-30))

class tripitidora(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "tripitidora"
        self.vida = 100
        self.daño = 10
        self.hostil = True
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 2500
        self.imagen = imagenes_tripitidora[0]
        self.costo = 325
        self.cambiosprites = 5
        self.sprites = imagenes_tripitidora
        self.recarga = 7500

class pinchohierba(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "pinchohierba"
        self.vida = 100
        self.daño = 10
        self.hostil = False
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 1000
        self.imagen = imagenes_pinchohierba[0]
        self.costo = 100
        self.cambiosprites = 5
        self.sprites = imagenes_pinchohierba
        self.recarga = 7500 
        self.intangible = True
    def dibujar(self):
        self.dibujar_sprites()
        screen.blit(self.sprites[self.indice_frame], (self.x-10, self.y+40))

class cafe(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "cafe"
        self.vida = 100
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 1000
        self.imagen = imagenes_cafe[0]
        self.costo = 75
        self.cambiosprites = 8
        self.sprites = imagenes_cafe
        self.recarga = 7500 
        self.intangible = True
    def dibujar(self):
        self.dibujar_sprites()
        screen.blit(self.sprites[self.indice_frame], (self.x+10, self.y-20))

class seta_desesporada(setas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "desesporada"
        self.vida = 100
        self.vida_permanente = 300
        self.daño = 10
        self.hostil = True
        self.imagen = imagenes_desesporada[0][0]
        self.costo = 0
        self.cooldown = 2500
        self.cambiosprites = 10
        self.sprites = imagenes_desesporada[1] if dia else imagenes_desesporada[0]
        self.sprites_despierta = imagenes_desesporada[0]
        self.partes = False
        self.recarga = 7500

    def dibujar(self):
        self.dibujar_sprites()
        if not self.dormida:
            screen.blit(self.sprites[self.indice_frame], (self.x+15, self.y+25))
        elif self.dormida:
            screen.blit(self.sprites[self.indice_frame], (self.x+15, self.y-5))

class seta_solar(setas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "solar"
        self.vida = 100
        self.vida_permanente = 300
        self.daño = 10
        self.hostil = False
        self.produccion = 15
        self.imagen = imagenes_seta_solar[0][0]
        self.costo = 25
        self.cooldown = 15000
        self.crecimiento = 40000
        self.cambiosprites = 5
        self.sprites = imagenes_seta_solar[1] if dia else imagenes_seta_solar[0]
        self.sprites_despierta = imagenes_seta_solar[0]
        self.partes = True
        self.recarga = 7500

    def dibujar(self):
        self.dibujar_sprites()
        if not self.dormida:
            screen.blit(self.sprites[self.indice_frame], (self.x-2, self.y+5))
        elif self.dormida:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
        elif self.activada:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))

class seta_miedosa(setas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "miedosa"
        self.vida = 100
        self.vida_permanente = 300
        self.daño = 10
        self.asustada = False
        self.hostil = False
        self.imagen = imagenes_seta_miedosa[0][0]
        self.costo = 25
        self.cooldown = 2500
        self.cambiosprites = 5
        self.sprites = imagenes_seta_miedosa[1] if dia else imagenes_seta_miedosa[0]
        self.sprites_despierta = imagenes_seta_miedosa[0]
        self.partes = True
        self.recarga = 7500

class seta_humo(setas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "humo"
        self.vida = 100
        self.vida_permanente = 300
        self.daño = 10
        self.hostil = False
        self.imagen = imagenes_seta_humo[0][0]
        self.costo = 75
        self.cooldown = 2500
        self.cambiosprites = 5
        self.sprites = imagenes_seta_humo[1] if dia else imagenes_seta_humo[0]
        self.sprites_despierta = imagenes_seta_humo[0]
        self.sprites_atk = imagenes_seta_humo_atk
        self.partes = True
        self.recarga = 7500
        
    def dibujar(self):
        self.dibujar_sprites()
        if self.sprites == self.sprites_atk:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y -15))
        elif self.dormida:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
        elif not self.dormida:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))

class petaseta(setas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "petaseta"
        self.vida = float("inf") if not self.dormida else 100
        self.daño = 500
        self.imagen = imagenes_petaseta[0][0]
        self.costo = 125
        self.cooldown = 15000
        self.cambiosprites = 10
        self.sprites = imagenes_petaseta[1] if dia else imagenes_petaseta[0]
        self.sprites_despierta = imagenes_petaseta[0]
        self.sprites_explosion = imagenes_petaseta_exp
        self.recarga = 50000
    def dibujar(self):
        self.dibujar_sprites()
        if self.sprites == imagenes_petaseta[1]:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y-10))
        elif self.sprites == imagenes_petaseta[0]:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y-10))
        elif self.sprites == imagenes_petaseta_exp:
            screen.blit(self.sprites[self.indice_frame], (self.x-65, self.y-180))
        elif self.sprites == imagenes_hole:
            screen.blit(self.sprites[self.indice_frame], (self.x, self.y))
    def comprobar_vida(self):
        if self.vida <= 0:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
                    cuadricula[i][2] = None
            plantulis.remove(self)
        if self.sprites == imagenes_hole and self.indice_frame == 2:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
                    cuadricula[i][2] = None
            plantulis.remove(self)

class seta_hielo(setas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "seta_hielo"
        self.vida = float("inf") if not self.dormida else 100
        self.daño = 500
        self.imagen = imagenes_seta_hielo[0][0]
        self.costo = 75
        self.cooldown = 15000
        self.cambiosprites = 8
        self.sprites = imagenes_seta_hielo[1] if dia else imagenes_seta_hielo[0]
        self.sprites_despierta = imagenes_seta_hielo[0]
        self.recarga = 50000
        
    def comprobar_vida(self):
        if self.vida <= 0:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
                    cuadricula[i][2] = None
            plantulis.remove(self)
        if self.explotada:
            for i,pos in enumerate(cuadricula):
                if self.x -15 == pos[0][0] and self.y -30 == pos[0][1]:
                    cuadricula[i][1] = False
                    cuadricula[i][2] = None
            plantulis.remove(self)

class hipnoseta(setas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "hipnoseta"
        self.vida = 100
        self.daño = 500
        self.imagen = imagenes_seta_hypno[0][0]
        self.costo = 75
        self.cooldown = 15000
        self.cambiosprites = 6
        self.sprites = imagenes_seta_hypno[1] if dia else imagenes_seta_hypno[0]
        self.sprites_despierta = imagenes_seta_hypno[0]
        self.recarga = 30000  

class Lanzaguisantes_hielo(Plantas):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "lanza_hielo"
        self.vida = 100
        self.daño = 10
        self.hostil = True
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 2500
        self.imagen = imagenes_lanza_cong[0]
        self.costo = 175
        self.cambiosprites = 5
        self.sprites = imagenes_lanza_cong
        self.recarga = 7500

class ZombiNormal(Zombies):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "zombi"
        self.vida = 200
        self.daño = 10
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 500
        self.cooldown_congelado = self.cooldown * 2
        self.cooldown_inicial = self.cooldown
        self.imagen = imagenes_zombi[0]
        self.velocidad = 0.2
        self.sprites = imagenes_zombi 
        self.velocidad_inicial = self.velocidad
        self.velocidad_congelado = self.velocidad / 2
        self.sprites_moviendo = imagenes_zombi 
        self.sprites_comiendo = imagenes_zombiatk
        self.sprites_moviendo_congelado = imagenes_zombi_congelado
        self.sprites_comiendo_congelado = imagenes_zombiatk_congelado
        self.indice_frame = 0
        self.cambiosprites = 6

class ZombiCono(Zombies):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "zombi_cono"
        self.vida = 350
        self.daño = 10
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 500
        self.cooldown_congelado = self.cooldown * 2
        self.cooldown_inicial = self.cooldown
        self.imagen = imagenes_zombicono[0]
        self.velocidad = 0.2
        self.velocidad_inicial = self.velocidad
        self.velocidad_congelado = self.velocidad / 2
        self.sprites = imagenes_zombicono 
        self.sprites_moviendo = imagenes_zombicono 
        self.sprites_comiendo = imagenes_zombiconoatk
        self.sprites_moviendo_congelado = imagenes_zombicono_congelado 
        self.sprites_comiendo_congelado = imagenes_zombiconoatk_congelado
        self.indice_frame = 0
        self.cambiosprites = 6

class ZombiCubo(Zombies):
    def __init__(self, x, y, linea):
        super().__init__(x, y, linea)
        self.nombre = "zombi_cubo"
        self.vida = 600
        self.daño = 10
        self.golpe = pygame.time.get_ticks()
        self.cooldown = 500
        self.cooldown_congelado = self.cooldown * 2
        self.cooldown_inicial = self.cooldown        
        self.imagen = imagenes_zombicubo[0]
        self.velocidad = 0.2
        self.velocidad_inicial = self.velocidad
        self.velocidad_congelado = self.velocidad / 2      
        self.sprites = imagenes_zombicubo 
        self.sprites_moviendo = imagenes_zombicubo
        self.sprites_comiendo = imagenes_zombicuboatk 
        self.sprites_moviendo_congelado = imagenes_zombicubo_congelado
        self.sprites_comiendo_congelado = imagenes_zombicuboatk_congelado
        self.indice_frame = 0
        self.cambiosprites = 6

class pala:
    def __init__(self, x, y):
        self.nombre = "pala"
        self.x = x
        self.y = y
        self.imagen = imagen_pala
        self.daño = 9999999999999999999999999
    
    def dibujar(self):
        screen.blit(self.imagen, (self.x, self.y))
    
    def atacar(self):
        for planta in plantulis:
            if self.x <= planta.x <= self.x+ancho_plantas and self.y<= planta.y <= self.y+altura_plantas:
                planta.vida -= planta.vida
                sonido_plantar.play()

class podadora:
    def __init__(self, x, y,linea):
        self.nombre = "podadora"
        self.x = x
        self.y = y
        self.linea = linea
        self.imagen = imagen_podadora
        self.velocidad  = 8
        self.activada = False
        self.cont = 0
    
    def dibujar(self):
        screen.blit(self.imagen, (self.x, self.y+30))

    def activar(self):
        for zombi in zombies:
            if self.x <= zombi.x <= self.x + 40 and self.linea == zombi.linea and self.cont == 0:
                self.activada = True
                self.cont = 1
                sonido_podadora.play()
    def mover(self):
        if self.activada:
            self.x += self.velocidad

    def atacar(self):
        for zombi in zombies:
            if self.x <= zombi.x <= self.x+ 45 and self.linea == zombi.linea and self.activada:
                zombi.vida -= zombi.vida

# Función para spawnear zombies
def spawn_zombi():
    global ultimo_spawn, posiciones_y,cont,zombies_para_ganar,zombies_cont
    if pygame.time.get_ticks() >= ultimo_spawn and zombies_cont <= zombies_para_ganar:
        eleccion = random.randint(0, 4)
        if cont == 3:
            zombi = ZombiCono(1280 - altura_zombi, posiciones_y[eleccion] - ancho_zombi, eleccion)
            zombies.append(zombi)
            cont += 1
            zombies_cont += 1
        elif cont == 5:
            zombi = ZombiCubo(1280 - altura_zombi, posiciones_y[eleccion] - ancho_zombi, eleccion)
            zombies.append(zombi)
            cont = 0
            zombies_cont += 1
        else:
            zombi = ZombiNormal(1280 - altura_zombi, posiciones_y[eleccion] - ancho_zombi, eleccion)
            zombies.append(zombi)
            cont += 1
            zombies_cont += 1
        carriles_zombi[eleccion] = True
        if zombies_cont == int(zombies_para_ganar * 0.6):
            sonido_awooga.play()
            screen.blit(imagen_oleada,(600-400,300-200))
        if zombies_cont <= zombies_para_ganar* 0.6:
            ultimo_spawn = pygame.time.get_ticks() + 8000
        else:
            if tiempo_interoliadas>= pygame.time.get_ticks():
                ultimo_spawn = pygame.time.get_ticks() + 900
                if zombies_cont == int(zombies_para_ganar* 0.8):
                    tiempo_interoliadas = pygame.time.get_ticks() + 5000
#ver que planta hay se selecciono y su posicion en la lista
def que_planta(pos, costo):
    if plantas_menu_seleccionadas[pos] == "lanza":
        return lanza_costo if costo else Lanzaguisantes(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "gira":
        return gira_costo if costo else Girasol(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "nuez":
        return nuez_costo if costo else Nuez(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "papapum":
        return papapum_costo if costo else papapum(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "peta":
        return peta_costo if costo else petacereza(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "repetidora":
        return repetidora_costo if costo else Repetidora(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "tripitidora":
        return tripitidora_costo if costo else tripitidora(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "jala":
        return jala_costo if costo else jalapeño(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "pinchohierba":
        return pincho_costo if costo else pinchohierba(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "carnivora":
        return carnivora_costo if costo else carnivora(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "desesporada":
        return desesporada_costo if costo else seta_desesporada(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "cafe":
        return cafe_costo if costo else cafe(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "solar":
        return seta_solar_costo if costo else seta_solar(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "miedosa":
        return seta_miedosa_costo if costo else seta_miedosa(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "lanza_hielo":
        return lanza_hielo_costo if costo else Lanzaguisantes_hielo(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "humo":
        return seta_humo_costo if costo else seta_humo(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "petaseta":
        return petaseta_costo if costo else petaseta(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "seta_hielo":
        return seta_hielo_costo if costo else seta_hielo(0, 0, 0)
    if plantas_menu_seleccionadas[pos] == "hipnoseta":
        return hipnoseta_costo if costo else hipnoseta(0, 0, 0)
#ver que semilla hay se selecciono y su posicion en la lista
def que_semilla(pos):
    if plantas_menu_seleccionadas[pos] == "lanza":
        return semillas_lanza
    if plantas_menu_seleccionadas[pos] == "gira":
        return semillas_gira
    if plantas_menu_seleccionadas[pos] == "nuez":
        return semillas_nuez
    if plantas_menu_seleccionadas[pos] == "papapum":
        return semillas_papa
    if plantas_menu_seleccionadas[pos] == "peta":
        return semillas_peta
    if plantas_menu_seleccionadas[pos] == "repetidora":
        return semillas_repetidora
    if plantas_menu_seleccionadas[pos] == "tripitidora":
        return semillas_tripitidora
    if plantas_menu_seleccionadas[pos] == "jala":
        return semillas_jala
    if plantas_menu_seleccionadas[pos] == "pinchohierba":
        return semillas_spincho
    if plantas_menu_seleccionadas[pos] == "carnivora":
        return semillas_carnivora
    if plantas_menu_seleccionadas[pos] == "desesporada":
        return semillas_seta_desesporada
    if plantas_menu_seleccionadas[pos] == "cafe":
        return semillas_cafe
    if plantas_menu_seleccionadas[pos] == "solar":
        return semillas_seta_sol
    if plantas_menu_seleccionadas[pos] == "miedosa":
        return semillas_seta_miedosita
    if plantas_menu_seleccionadas[pos] == "lanza_hielo":
        return semillas_lanza_cong
    if plantas_menu_seleccionadas[pos] == "humo":
        return semillas_seta_humo
    if plantas_menu_seleccionadas[pos] == "petaseta":
        return semillas_petaseta
    if plantas_menu_seleccionadas[pos] == "seta_hielo":
        return semillas_seta_cong  
    if plantas_menu_seleccionadas[pos] == "hipnoseta":
        return semillas_seta_hyp  
#saber en que posicion hay un "None" para reemplazarlo por una planta (es como un estilo sort para que se elija la planta y no queden espacios vacios)
def encontrar_el_None():
    pos = None
    for a,i in enumerate(plantas_menu_seleccionadas):
        if i == None:
            pos = a
            break
    return pos 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not inicio and not estado_menu_seleccion:
            if not perdiste:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #ver posicion del mouse
                    x, y = pygame.mouse.get_pos()
                    #si el click toco un sol que lo agarre
                    for sol in soles:
                        if sol.x > x > sol.x - ancho_sol and sol.y > y > sol.y - altura_sol:
                            sol.tocado = True
                            var_sol += sol.valor
                    #ver si se seleccionó una planta
                    if not mouse_estado:
                        if 420 <= x <= 480 and y <= 71 and var_sol >= que_planta(0, True) and tiempo_recarga1 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(0, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 1

                        elif 485 <= x <= 545 and y <= 71 and var_sol >= que_planta(1, True) and tiempo_recarga2 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(1, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 2

                        elif 550 <= x <= 610 and y <= 71 and var_sol >= que_planta(2, True) and tiempo_recarga3 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(2, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 3

                        elif 615 <= x <= 675 and y <= 71 and var_sol >= que_planta(3, True) and tiempo_recarga4 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(3, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 4

                        elif 680 <= x <= 740 and y <= 71 and var_sol >= que_planta(4, True) and tiempo_recarga5 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(4, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 5

                        elif 745 <= x <= 805 and y <= 71 and var_sol >= que_planta(5, True) and tiempo_recarga6 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(5, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 6

                        elif 810 <= x <= 865 and y <= 71 and var_sol >= que_planta(6, True) and tiempo_recarga7 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(6, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 7

                        elif 870 <= x <= 935 and y <= 71 and var_sol >= que_planta(7, True) and tiempo_recarga8 <= pygame.time.get_ticks():
                            planta_seleccionada = que_planta(7, False)
                            mouse_estado = True
                            sonido_agarrar.play()
                            planta_seleccionada.num_recarga = 8
                        
                        elif 950 <= x <= 1025 and y <= 71 and not pala_act:
                            planta_seleccionada = pala(0,0)
                            pala_act = True
                            mouse_estado = True
                            sonido_agarrar.play()
                    else:
                        #comprobar si la posicion es valida,si es valida comprobar que casilla es
                        posi = la_posicion(x, y)   
                        if not pala_act and posi is not None:
                            posicion, linea = posi
                            if posicion is not None and planta_seleccionada is not None:
                                planta = planta_seleccionada
                                planta.x = posicion[0] + 15
                                planta.y = posicion[1] + 30
                                planta.linea = linea
                                #comprobar si la casilla esta ocupada
                                for lugar in cuadricula:
                                    if lugar[0] == posicion and not lugar[1] and planta.nombre != "cafe":
                                        lugar[1] = True
                                        lugar[2] = planta
                                        var_sol -= planta.costo
                                        planta.golpe = pygame.time.get_ticks() + planta.cooldown
                                        plantulis.append(planta)
                                        #refrescar los tiempos de recarga
                                        if planta.num_recarga == 1:
                                            tiempo_recarga1 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        elif planta.num_recarga == 2:
                                            tiempo_recarga2 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        elif planta.num_recarga == 3:
                                            tiempo_recarga3 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        elif planta.num_recarga == 4:
                                            tiempo_recarga4 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        elif planta.num_recarga == 5:
                                            tiempo_recarga5 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        elif planta.num_recarga == 6:
                                            tiempo_recarga6 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        elif planta.num_recarga == 7:
                                            tiempo_recarga7 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        elif planta.num_recarga == 8:
                                            tiempo_recarga8 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                        planta_seleccionada = None  # Deselecciona la planta después de colocarla
                                        mouse_estado = False  # Resetea el estado del mouse
                                        sonido_semilla.play()
                                    elif lugar[0] == posicion and lugar[1] and planta.nombre == "cafe":
                                        if lugar[2].seta and lugar[2].dormida:
                                            var_sol -= planta.costo
                                            planta.golpe = pygame.time.get_ticks() + planta.cooldown
                                            plantulis.append(planta)
                                            #refrescar los tiempos de recarga
                                            if planta.num_recarga == 1:
                                                tiempo_recarga1 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            elif planta.num_recarga == 2:
                                                tiempo_recarga2 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            elif planta.num_recarga == 3:
                                                tiempo_recarga3 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            elif planta.num_recarga == 4:
                                                tiempo_recarga4 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            elif planta.num_recarga == 5:
                                                tiempo_recarga5 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            elif planta.num_recarga == 6:
                                                tiempo_recarga6 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            elif planta.num_recarga == 7:
                                                tiempo_recarga7 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            elif planta.num_recarga == 8:
                                                tiempo_recarga8 = pygame.time.get_ticks() + planta_seleccionada.recarga
                                            planta_seleccionada = None  # Deselecciona la planta después de colocarla
                                            mouse_estado = False  # Resetea el estado del mouse
                                            sonido_semilla.play()
                        elif pala_act and posi is not None:
                                #hacer que la pala remueva plantas
                                planta_seleccionada.x = posi[0][0]
                                planta_seleccionada.y = posi[0][1]
                                planta_seleccionada.atacar()
                                pala_act = False
                                planta_seleccionada = None
                                mouse_estado = False                  

                        else:
                            #cancelar el click ya que no se selecciono una posicion valida
                            mouse_estado = False
                            planta_seleccionada = None
                            pala_act = False
        elif inicio:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos() 
                #salir del menu de inicio
                if 612 <= x <= 1090 and 100 <= y <= 170:
                    estado_menu_seleccion = True
                    inicio= False   
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("soundtrack/musicaPvz.mp3")
                    pygame.mixer.music.play(-1)
                elif 961 <= x <= 1058 and 472 <= y <= 532:
                    tutorial()     
                elif 1073 <= x <= 1166 and 473 <= y <= 570:
                    running = False 
        elif estado_menu_seleccion:
             if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                el_none = encontrar_el_None()
                if 430 <= x <= 490 and 133 <= y <= 203:
                    if "lanza" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "lanza"
                    elif "lanza" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("lanza")
                        plantas_menu_seleccionadas.append(None)

                elif 498 <= x <= 558 and 133 <= y <= 203:
                    if "gira" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "gira"
                    elif "gira" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("gira")
                        plantas_menu_seleccionadas.append(None)

                elif 566 <= x <= 626 and 133 <= y <= 203:
                    if "nuez" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "nuez"
                    elif "nuez" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("nuez")
                        plantas_menu_seleccionadas.append(None)

                elif 634 <= x <= 694 and 133 <= y <= 203:
                    if "papapum" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "papapum"
                    elif "papapum" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("papapum")
                        plantas_menu_seleccionadas.append(None)

                elif 702 <= x <= 762 and 133 <= y <= 203:
                    if "peta" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "peta"
                    elif "peta" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("peta")
                        plantas_menu_seleccionadas.append(None)

                elif 770 <= x <= 830 and 133 <= y <= 203:
                    if "repetidora" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "repetidora"
                    elif "repetidora" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("repetidora")
                        plantas_menu_seleccionadas.append(None)

                elif 838 <= x <= 898 and 133 <= y <= 203:
                    if "tripitidora" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "tripitidora"
                    elif "tripitidora" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("tripitidora")
                        plantas_menu_seleccionadas.append(None)

                elif 906 <= x <= 966 and 133 <= y <= 203:
                    if "jala" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "jala"
                    elif "jala" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("jala")
                        plantas_menu_seleccionadas.append(None)

                elif 430 <= x <= 490 and 208 <= y <= 278:
                    if "pinchohierba" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "pinchohierba"
                    elif "pinchohierba" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("pinchohierba")
                        plantas_menu_seleccionadas.append(None)
                
                elif 498 <= x <= 558 and 208 <= y <= 278:
                    if "carnivora" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "carnivora"
                    elif "carnivora" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("carnivora")
                        plantas_menu_seleccionadas.append(None)
                elif 634 <= x <= 694 and 208 <= y <= 278:
                    if "desesporada" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "desesporada"
                    elif "desesporada" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("desesporada")
                        plantas_menu_seleccionadas.append(None)
                elif 566 <= x <= 626 and 283 <= y <= 353:
                    if "cafe" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "cafe"
                    elif "cafe" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("cafe")
                        plantas_menu_seleccionadas.append(None)
                elif 702 <= x <= 762 and 208 <= y <= 278:
                    if "solar" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "solar"
                    elif "solar" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("solar")
                        plantas_menu_seleccionadas.append(None)
                elif 770 <= x <= 830 and 208 <= y <= 278:
                    if "miedosa" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "miedosa"
                    elif "miedosa" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("miedosa")
                        plantas_menu_seleccionadas.append(None)
                elif 838 <= x <= 898 and 208 <= y <= 278:
                    if "humo" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "humo"
                    elif "humo" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("humo")
                        plantas_menu_seleccionadas.append(None)
                elif 906 <= x <= 966 and 208 <= y <= 278:
                    if "petaseta" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "petaseta"
                    elif "petaseta" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("petaseta")
                        plantas_menu_seleccionadas.append(None)
                elif 430 <= x <= 490 and 283 <= y <= 353:
                    if "seta_hielo" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "seta_hielo"
                    elif "seta_hielo" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("seta_hielo")
                        plantas_menu_seleccionadas.append(None)
                elif 498 <= x <= 558 and 283 <= y <= 353:
                    if "hipnoseta" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "hipnoseta"
                    elif "hipnoseta" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("hipnoseta")
                        plantas_menu_seleccionadas.append(None)
                elif  566 <= x <= 626  and 208 <= y <= 278:
                    if "lanza_hielo" not in plantas_menu_seleccionadas and None in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas[el_none] = "lanza_hielo"
                    elif "lanza_hielo" in plantas_menu_seleccionadas:
                        plantas_menu_seleccionadas.remove("lanza_hielo")
                        plantas_menu_seleccionadas.append(None)
                elif 600 <= x <= 800 and 517 <= y <= 557 and None not in plantas_menu_seleccionadas:
                    contador = 0
                    for i in range(5):
                        poda = podadora(250,contador + 75,i)
                        podadoras.append(poda)
                        contador += 100
                    estado_menu_seleccion = False

    if not inicio and not estado_menu_seleccion:
        #cargar en pantalla las imagenes de las semillas,fondo y el menu donde se ponen las semillas
        if dia:
            screen.blit(fondo_dia, (0, 0))
        else:
            screen.blit(fondo_noche, (0, 0))
        screen.blit(menu_plantil, (300, 0))
# Verificar el estado de recarga y blit para cada semilla
        if tiempo_recarga1 <= pygame.time.get_ticks():
            screen.blit(que_semilla(0)[0], (420, 1))
        else:
            screen.blit(que_semilla(0)[1], (420, 1))

        if tiempo_recarga2 <= pygame.time.get_ticks():
            screen.blit(que_semilla(1)[0], (485, 1))
        else:
            screen.blit(que_semilla(1)[1], (485, 1))

        if tiempo_recarga3 <= pygame.time.get_ticks():
            screen.blit(que_semilla(2)[0], (550, 1))
        else:
            screen.blit(que_semilla(2)[1], (550, 1))

        if tiempo_recarga4 <= pygame.time.get_ticks():
            screen.blit(que_semilla(3)[0], (615, 1))
        else:
            screen.blit(que_semilla(3)[1], (615, 1))

        if tiempo_recarga5 <= pygame.time.get_ticks():
            screen.blit(que_semilla(4)[0], (680, 1))
        else:
            screen.blit(que_semilla(4)[1], (680, 1))

        if tiempo_recarga6 <= pygame.time.get_ticks():
            screen.blit(que_semilla(5)[0], (745, 1))
        else:
            screen.blit(que_semilla(5)[1], (745, 1))

        if tiempo_recarga7 <= pygame.time.get_ticks():
            screen.blit(que_semilla(6)[0], (810, 1))
        else:
            screen.blit(que_semilla(6)[1], (810, 1))

        if tiempo_recarga8 <= pygame.time.get_ticks():
            screen.blit(que_semilla(7)[0], (875, 1))
        else:
            screen.blit(que_semilla(7)[1], (875, 1))

        screen.blit(imagen_icono_pala,(950,0))
        pos_mouse = pygame.mouse.get_pos()
        if not perdiste:
            spawn_zombi()
            #texto de soles para que aparezca en pantalla
            texto = f"{var_sol}"
            text_surface = font.render(texto, True, (0,0,0))
            text_rect = text_surface.get_rect(center=(350, 65))  
            screen.blit(text_surface, text_rect)
            #crear soles en el modo dia
            if dia:
                if ultimo_sol <= pygame.time.get_ticks():
                    ultimo_sol = pygame.time.get_ticks() + sol_cooldown
                    solsito = clase_sol(1,1,25)
                    soles.append(solsito)
            #hacer que la planta seleccionada siga al mouse           
            #los metodos de los diferentes objetos
            for planta in plantulis:
                planta.cargar_partes()
                planta.comprobar_vida()
                planta.dibujar()
                planta.atacar()
                planta.generar_sol()
                planta.explosion()
            for zombi in zombies:
                zombi.dibujar_sprites()
                zombi.dibujar()
                zombi.mover()
                zombi.comprobar_vida()
                zombi.atacar()
                zombi.esta_comiendo()
                zombi.esta_congelado()
                zombi.perder()
            for proyectil in proyectiles:
                proyectil.dibujar()
                proyectil.mover()
                proyectil.golpeo()
                proyectil.dibujar_sprites()
                proyectil.fuera_de_rango()
            for sol in soles:
                sol.dibujar()
                sol.mover()
                sol.dibujar_sprites()
                sol.desaparecer()
            for podas in podadoras:
                podas.dibujar()
                podas.mover()
                podas.activar()
                podas.atacar()
            if mouse_estado and planta_seleccionada:
                if planta_seleccionada.nombre == "carnivora":
                    screen.blit(planta_seleccionada.imagen, (pos_mouse[0] - altura_plantas / 2, pos_mouse[1] - ancho_plantas / 2 - 30))
                elif planta_seleccionada.nombre == "desesporada":
                    screen.blit(planta_seleccionada.imagen, (pos_mouse[0] - altura_plantas / 2 + 15, pos_mouse[1] - ancho_plantas / 2 + 15))
                elif planta_seleccionada.nombre == "pinchohierba":
                    screen.blit(planta_seleccionada.imagen, (pos_mouse[0] - altura_plantas / 2, pos_mouse[1] - ancho_plantas / 2 +15))
                elif planta_seleccionada.nombre == "cafe":
                    screen.blit(planta_seleccionada.imagen, (pos_mouse[0] - altura_plantas / 2 + 20, pos_mouse[1] -20 ))
                else:
                    screen.blit(planta_seleccionada.imagen, (pos_mouse[0] - altura_plantas / 2, pos_mouse[1] - ancho_plantas / 2 )) 
        else:
            screen.blit(imagen_game_over,(600-400,300-200))
    elif inicio: 
        if dia:
            screen.blit(fondo_pantalla1,(0,0))
        else:
            screen.blit(fondo_pantalla2,(0,0))


    elif estado_menu_seleccion:
        if dia:
            screen.blit(fondo_dia, (0, 0))
        else:
            screen.blit(fondo_noche, (0, 0))
        screen.blit(menu_plantil, (300, 0))
        screen.blit(imagen_menu_seleccion,(400,85))  
# Verificar y renderizar las semillas en cada posición 
        if None != plantas_menu_seleccionadas[0]:
            if que_semilla(0) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(0)[0], (420, 1))
                else:
                    screen.blit(que_semilla(0)[1], (420, 1))
            else:
                screen.blit(que_semilla(0)[0], (420, 1))       
        if None != plantas_menu_seleccionadas[1]:
            if que_semilla(1) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(1)[0], (485, 1))
                else:
                    screen.blit(que_semilla(1)[1], (485, 1))
            else:
                screen.blit(que_semilla(1)[0], (485, 1))        
        if None != plantas_menu_seleccionadas[2]:
            if que_semilla(2) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(2)[0], (550, 1))
                else:
                    screen.blit(que_semilla(2)[1], (550, 1))
            else:
                screen.blit(que_semilla(2)[0], (550, 1))
        if None != plantas_menu_seleccionadas[3]:
            if que_semilla(3) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(3)[0], (615, 1))
                else:
                    screen.blit(que_semilla(3)[1], (615, 1))
            else:
                screen.blit(que_semilla(3)[0], (615, 1))            
        if None != plantas_menu_seleccionadas[4]:
            if que_semilla(4) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(4)[0], (680, 1))
                else:
                    screen.blit(que_semilla(4)[1], (680, 1))
            else:
                screen.blit(que_semilla(4)[0], (680, 1))              
        if None != plantas_menu_seleccionadas[5]:
            if que_semilla(5) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(5)[0], (745, 1))
                else:
                    screen.blit(que_semilla(5)[1], (745, 1))
            else:
                screen.blit(que_semilla(5)[0], (745, 1))        
        if None != plantas_menu_seleccionadas[6]:
            if que_semilla(6) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(6)[0], (810, 1))
                else:
                    screen.blit(que_semilla(6)[1], (810, 1))
            else:
                screen.blit(que_semilla(6)[0], (810, 1))        
        if None != plantas_menu_seleccionadas[7]:
            if que_semilla(7) in imagenes_setas:
                if "cafe" in plantas_menu_seleccionadas:
                    screen.blit(que_semilla(7)[0], (875, 1))
                else:
                    screen.blit(que_semilla(7)[1], (875, 1))
            else:
                screen.blit(que_semilla(7)[0], (875, 1))        
        if "lanza" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_slanza, (430, 133))
        else:
            screen.blit(imagen_slanza_cooldown, (430, 133))

        if "gira" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_sgira, (498, 133))
        else:
            screen.blit(imagen_sgira_cooldown, (498, 133))

        if "nuez" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_snuez, (566, 133))
        else:
            screen.blit(imagen_snuez_cooldown, (566, 133))

        if "papapum" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_spapa, (634, 133))
        else:
            screen.blit(imagen_spapa_cooldown, (634, 133))

        if "peta" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_speta, (702, 133))
        else:
            screen.blit(imagen_speta_cooldown, (702, 133))

        if "repetidora" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_srepetidora, (770, 133))
        else:
            screen.blit(imagen_srepetidora_cooldown, (770, 133))

        if "tripitidora" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_stripitidora, (838, 133))
        else:
            screen.blit(imagen_stripitidora_cooldown, (838, 133))

        if "jala" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_sjala, (906, 133))
        else:
            screen.blit(imagen_sjala_cooldown, (906, 133))
        if "pinchohierba" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_spincho, (430, 208))
        else:
            screen.blit(imagen_spincho_cooldown, (430, 208))
        if "carnivora" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_scarnivora, (498, 208))
        else:
            screen.blit(imagen_scarnivora_cooldown, (498, 208))
        if "desesporada" not in plantas_menu_seleccionadas and (not dia or "cafe" in plantas_menu_seleccionadas): 
            screen.blit(imagen_sseta_desesporada, (634, 208))
        else:
            screen.blit(imagen_sseta_desesporada_cooldown, (634, 208))

        if "cafe" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_scafe, (566, 283))
        else:
            screen.blit(imagen_scafe_cooldown, (566, 283))

        if "solar" not in plantas_menu_seleccionadas and (not dia or "cafe" in plantas_menu_seleccionadas): 
            screen.blit(imagen_sseta_sol, (702, 208))
        else:
            screen.blit(imagen_sseta_sol_cooldown, (702, 208))

        if "miedosa" not in plantas_menu_seleccionadas and (not dia or "cafe" in plantas_menu_seleccionadas): 
            screen.blit(imagen_sseta_miedosita, (770, 208))
        else:
            screen.blit(imagen_sseta_miedosita_cooldown, (770, 208))

        if "lanza_hielo" not in plantas_menu_seleccionadas: 
            screen.blit(imagen_slanza_cong, (566, 208))
        else:
            screen.blit(imagen_slanza_cong_cooldown, (566, 208))

        if "humo" not in plantas_menu_seleccionadas and (not dia or "cafe" in plantas_menu_seleccionadas): 
            screen.blit(imagen_sseta_humo, (838, 208))
        else:
            screen.blit(imagen_sseta_humo_cooldown, (838, 208))

        if "petaseta" not in plantas_menu_seleccionadas and (not dia or "cafe" in plantas_menu_seleccionadas): 
            screen.blit(imagen_spetaseta, (906, 208))
        else:
            screen.blit(imagen_spetaseta_cooldown, (906, 208))

        if "seta_hielo" not in plantas_menu_seleccionadas and (not dia or "cafe" in plantas_menu_seleccionadas): 
            screen.blit(imagen_sseta_cong, (430, 283))
        else:
            screen.blit(imagen_sseta_cong_cooldown, (430, 283))

        if "hipnoseta" not in plantas_menu_seleccionadas and (not dia or "cafe" in plantas_menu_seleccionadas): 
            screen.blit(imagen_sseta_hyp, (498, 283))
        else:
            screen.blit(imagen_sseta_hyp_cooldown, (498, 283))
    
    if not inicio and not estado_menu_seleccion:
        contador = 0
        for zombi in zombies:
            if zombi.aliado:
                contador += 1
        if zombies_para_ganar <= zombies_cont and len(zombies) - contador == 0 and not ganaste:
            ganaste = True
            tiempo_ganaste = pygame.time.get_ticks()


    if ganaste:
        texto_ganaste = f"GANASTE"
        text_surface = font_ganaste.render(texto_ganaste, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(600,325))  
        screen.blit(text_surface, text_rect)
        if contotototo == 0:
            sonido_victoria.play()
            contotototo += 1
        if tiempo_ganaste + 5000 <= pygame.time.get_ticks():
            cuadricula = []
            for pos in posiciones:
                for filas in pos:
                    cuadricula.append([filas, False,None])
            contotototo = 0
            ganaste = False
            inicio = True
            zombies_cont = 0
            plantulis = [] 
            tiempo_recarga1 = 0
            tiempo_recarga2 = 0
            tiempo_recarga3 = 0
            tiempo_recarga4 = 0
            tiempo_recarga5 = 0
            tiempo_recarga6 = 0
            tiempo_recarga7 = 0
            tiempo_recarga8 = 0         
            cont = 0
            plantas_menu_seleccionadas = [None,None,None,None,None,None,None,None]
            if dia:
                dia = False
            else:
                dia = True
    screen.blit(imagen_huergo, (0, 525))
    screen.blit(imagen_compu, (100, 525))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit() 
