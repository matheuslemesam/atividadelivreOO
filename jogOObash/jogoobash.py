#jogoobash.json

import json
import random

shared_inventory = []

class Hero:
    def __init__(self, name, hero_class, mana, black_mana, vitality, arcane, speed, attack):
        self.__name = name
        self.__class = hero_class
        self.__mana = mana
        self.__black_mana = black_mana
        self.__vitality = vitality
        self.__arcane = arcane
        self.__speed = speed
        self.__attack = attack
        self.__level = 1
        self.__experience = 0
        self.__abilities = []  
        self.__inventory = [{"name": "Moedas", "amount": 20}]
        self.__equipped_items = []

    # Getters
    def get_name(self):
        return self.__name

    def get_class(self):
        return self.__class

    def get_mana(self):
        return self.__mana

    def get_black_mana(self):
        return self.__black_mana

    def get_vitality(self):
        return self.__vitality

    def get_arcane(self):
        return self.__arcane

    def get_speed(self):
        return self.__speed

    def get_attack(self):
        return self.__attack

    def get_level(self):
        return self.__level

    def get_experience(self):
        return self.__experience

    def get_abilities(self):
        return self.__abilities

    def get_inventory(self):
        return self.__inventory

    def get_equipped_items(self):
        return self.__equipped_items

    # Setters
    def set_mana(self, mana):
        self.__mana = mana

    def set_black_mana(self, black_mana):
        self.__black_mana = black_mana

    def set_vitality(self, vitality):
        self.__vitality = vitality

    def gain_experience(self, amount):
        self.__experience += amount
        if self.__experience >= 100:
            self.level_up()

    def level_up(self):
        self.__level += 1
        self.__experience -= 100
        print(f"{self.__name} subiu para o nível {self.__level}!")
        self.allocate_points()
        self.unlock_abilities()

    def allocate_points(self):
        points = 5
        while points > 0:
            print(f"Você tem {points} pontos para distribuir.")
            print("1. Mana\n2. Vitalidade\n3. Arcano\n4. Velocidade\n5. Ataque")
            if self.get_class() == "Necromante":
                print("6. Mana Negra")
            choice = int(input("Escolha um atributo para aumentar: "))
            if choice == 1:
                self.__mana += 1
            elif choice == 2:
                self.__vitality += 1
            elif choice == 3:
                self.__arcane += 1
            elif choice == 4:
                self.__speed += 1
            elif choice == 5:
                self.__attack += 1
            elif choice == 6 and self.get_class() == "Necromante":
                self.__black_mana += 1
            else:
                print("Opção inválida.")
                continue
            points -= 1

    def unlock_abilities(self):
        abilities_by_level = {
            "Mago": {
                2: "Bola de Fogo",
                4: "Tempestade Arcana",
                6: "Barreira Mágica",
                8: "Explosão de Mana",
                10: "Invocação de Elemental"
            },
            "Cavaleiro": {
                2: "Golpe de Escudo",
                4: "Carga Heroica",
                6: "Defesa Absoluta",
                8: "Espada da Justiça",
                10: "Chamado à Batalha"
            },
            "Profeta": {
                2: "Benção Divina",
                4: "Luz Curativa",
                6: "Chama Sagrada",
                8: "Proteção Celestial",
                10: "Julgamento Divino"
            },
            "Necromante": {
                2: "Levantar Mortos",
                4: "Explosão Sombria",
                6: "Sifão de Alma",
                8: "Maldição Mortal",
                10: "Exército de Mortos"
            },
            "Assassino": {
                2: "Golpe Sombrio",
                4: "Passo Silencioso",
                6: "Venenos Mortais",
                8: "Ataque Relâmpago",
                10: "Execução Perfeita"
            },
            "Tanque": {
                2: "Provocação",
                4: "Muralha de Ferro",
                6: "Investida Blindada",
                8: "Resistência Inabalável",
                10: "Última Linha"
            }
        }
        if self.__class in abilities_by_level:
            abilities = abilities_by_level[self.__class]
            if self.__level in abilities:
                new_ability = abilities[self.__level]
                self.__abilities.append(new_ability)
                print(f"Nova habilidade desbloqueada: {new_ability}!")

    def use_ability(self, ability):
        if ability in self.__abilities:
            print(f"{self.__name} usou {ability}!")
            return 50 
        elif ability == "Ataque Básico":
            return self.__attack
        else:
            print("Habilidade não disponível ou não desbloqueada!")
            return 0

    def serialize(self):
        return {
            "name": self.__name,
            "class": self.__class,
            "mana": self.__mana,
            "black_mana": self.__black_mana,
            "vitality": self.__vitality,
            "arcane": self.__arcane,
            "speed": self.__speed,
            "attack": self.__attack,
            "level": self.__level,
            "experience": self.__experience,
            "abilities": self.__abilities
        }

    @staticmethod
    def deserialize(data):
        hero = Hero(
            name=data["name"],
            hero_class=data["class"],
            mana=data["mana"],
            black_mana=data["black_mana"],
            vitality=data["vitality"],
            arcane=data["arcane"],
            speed=data["speed"],
            attack=data["attack"]
        )
        hero.__level = data["level"]
        hero.__experience = data["experience"]
        hero.__abilities = data.get("abilities", []) 
        return hero

    def add_item_to_inventory(self, item):
        self.__inventory.append(item)

    def spend_coins(self, amount):
        for item in self.__inventory:
            if item['name'] == "Moedas":
                if item['amount'] >= amount:
                    item['amount'] -= amount
                    return True
                else:
                    print("Moedas insuficientes!")
                    return False
        return False

    def get_coin_count(self):
        for item in self.__inventory:
            if item['name'] == "Moedas":
                return item['amount']
        return 0


class Monster:
    def __init__(self, name, monster_class, level, vitality, attack):
        self.__name = name
        self.__class = monster_class
        self.__level = level
        self.__vitality = vitality
        self.__attack = attack

    def get_name(self):
        return self.__name

    def get_class(self):
        return self.__class

    def get_level(self):
        return self.__level

    def get_vitality(self):
        return self.__vitality

    def set_vitality(self, vitality):
        self.__vitality = vitality

    def use_ability(self):
        return random.choice(["Ataque Básico", "Ataque Especial"])

    def attack_hero(self, ability):
        if ability == "Ataque Básico":
            return self.__attack
        elif ability == "Ataque Especial":
            return self.__attack * 2

    def get_experience_reward(self):
        return self.__level + 5

    def drop_loot(self):
        coins = random.randint(5, 12) 
        loot_table = {
            1: [{"name": "Poção de Vida", "buffs": {"vitality": 10}}],
            2: [{"name": "Espada Simples", "buffs": {"attack": 5}}],
            3: [{"name": "Armadura Leve", "buffs": {"vitality": 15}}],
            4: [{"name": "Arco Longo", "buffs": {"speed": 7}}],
            5: [{"name": "Elmo Resistente", "buffs": {"vitality": 20}}],
            6: [{"name": "Poção de Mana", "buffs": {"mana": 5}}],
        }
        common_item = {"name": "Item Comum", "buffs": self.generate_random_buffs()}
        loot = random.choice(loot_table.get(self.__level, [common_item]))
        return [loot, {"name": "Moedas", "amount": coins}]

class AdaptiveMonster:
    def __init__(self, name, monster_class, level, vitality, attack):
        self.__name = name
        self.__class = monster_class
        self.__level = level
        self.__vitality = vitality
        self.__attack = attack
        self.__last_action = None
        self.__resistance = {}

    def get_name(self):
        return self.__name

    def get_class(self):
        return self.__class

    def get_level(self):
        return self.__level

    def get_vitality(self):
        return self.__vitality

    def set_vitality(self, vitality):
        self.__vitality = vitality

    def adapt_strategy(self, last_hero_action):
        if last_hero_action:
            self.__resistance[last_hero_action] = self.__resistance.get(last_hero_action, 0) + 1

    def use_ability(self):
        if self.__resistance.get("Ataque Básico", 0) >= 2:
            return "Ataque Especial"
        return random.choice(["Ataque Básico", "Ataque Especial"])

    def attack_hero(self, ability):
        if ability == "Ataque Básico":
            return self.__attack
        elif ability == "Ataque Especial":
            return self.__attack * 2

    def get_experience_reward(self):
        return (self.__level*2) + 5

    def drop_loot(self):
        loot_table = {
            1: [{"name": "Poção de Vida", "buffs": {"vitality": 10}}],
            2: [{"name": "Espada Simples", "buffs": {"attack": 5}}],
            3: [{"name": "Armadura Leve", "buffs": {"vitality": 15}}],
            4: [{"name": "Arco Longo", "buffs": {"speed": 7}}],
            5: [{"name": "Elmo Resistente", "buffs": {"vitality": 20}}],
            6: [{"name": "Poção de Mana", "buffs": {"mana": 5}}],
        }
        common_item = {"name": "Item Comum", "buffs": self.generate_random_buffs()}
        return random.choice(loot_table.get(self.__level, [common_item]))

    def generate_random_buffs(self):
        stats = ["vitality", "mana", "attack", "speed", "arcane"]
        chosen_stats = random.sample(stats, 2)
        return {stat: random.randint(1, 5) for stat in chosen_stats}

    def equip_item(self, item):
        if len(self.__equipped_items) >= 3:
            print("Você já possui 3 itens equipados. Remova um antes de equipar outro.")
        elif item in self.__inventory:
            self.__equipped_items.append(item)
            self.__inventory.remove(item)
            print(f"Item {item['name']} equipado!")
        else:
            print("Item não encontrado no inventário.")

    def unequip_item(self, item_name):
        for item in self.__equipped_items:
            if item['name'] == item_name:
                self.__equipped_items.remove(item)
                self.__inventory.append(item)
                print(f"Item {item_name} removido!")
                return
        print("Item não está equipado.")

    def apply_buffs(self):
        for item in self.__equipped_items:
            for stat, value in item.get('buffs', {}).items():
                setattr(self, f"_{self.__class__.__name__}__{stat}", getattr(self, f"_{self.__class__.__name__}__{stat}") + value)

def fight_with_loot(hero, monster, heroes):
    global shared_inventory  

    print(f"{hero.get_name()} ({hero.get_class()}) está enfrentando {monster.get_name()} ({monster.get_class()}, Nível {monster.get_level()})!")
    last_hero_action = None

    while hero.get_vitality() > 0 and monster.get_vitality() > 0:
        print(f"\n{hero.get_name()} - Vitalidade: {hero.get_vitality()}, Mana: {hero.get_mana()}")
        print(f"{monster.get_name()} - Vitalidade: {monster.get_vitality()}")

        print("Escolha sua ação:")
        print("1. Ataque Básico")
        print("2. Habilidade Especial")
        print("3. Fugir")
        action = input("Escolha a ação: ")

        if action == "1":
            hero_damage = hero.use_ability("Ataque Básico")
            last_hero_action = "Ataque Básico"
        elif action == "3":
            print(f"{hero.get_name()} fugiu da batalha!")
            return False
        elif action == "2":
            if not hero.get_abilities():
                print("Nenhuma habilidade especial desbloqueada. Usando ataque básico.")
                hero_damage = hero.use_ability("Ataque Básico")
                last_hero_action = "Ataque Básico"
            else:
                print("Escolha uma habilidade especial:")
                for idx, ability in enumerate(hero.get_abilities(), start=1):
                    print(f"{idx}. {ability}")
                ability_choice = input("Digite o número da habilidade ou pressione Enter para cancelar: ")
                if ability_choice.isdigit() and 1 <= int(ability_choice) <= len(hero.get_abilities()):
                    selected_ability = hero.get_abilities()[int(ability_choice) - 1]
                    hero_damage = hero.use_ability(selected_ability)
                    last_hero_action = selected_ability
                else:
                    print("Escolha inválida ou cancelada. Usando ataque básico.")
                    hero_damage = hero.use_ability("Ataque Básico")
                    last_hero_action = "Ataque Básico"
        else:
            print("Ação inválida, turno perdido.")
            hero_damage = 0

        monster.set_vitality(monster.get_vitality() - hero_damage)
        print(f"{hero.get_name()} causou {hero_damage} de dano em {monster.get_name()}.")

        if monster.get_vitality() <= 0:
            print(f"{monster.get_name()} foi derrotado!")
            hero.gain_experience(monster.get_experience_reward())

            recovery_option = random.choice(["heal", "potion"])
            if recovery_option == "heal":
                heal_amount = min(hero.get_vitality() + 20, 100)  
                hero.set_vitality(heal_amount)
                print(f"{hero.get_name()} recuperou 20 pontos de vitalidade!")
            elif recovery_option == "potion":
                shared_inventory.append({"name": "Poção de Vida", "buffs": {"vitality": 20}})
                print("Você recebeu uma Poção de Vida!")

            loot = monster.drop_loot()
            shared_inventory.append(loot)
            print(f"Você recebeu: {loot['name']}!")

            return True

        monster_action = monster.use_ability()
        monster_damage = monster.attack_hero(monster_action)
        hero.set_vitality(hero.get_vitality() - monster_damage)
        print(f"{monster.get_name()} usou {monster_action} e causou {monster_damage} de dano em {hero.get_name()}.")

        if hero.get_vitality() <= 0:
            print(f"{hero.get_name()} foi derrotado! Game Over.")
            heroes.remove(hero)  
            save_heroes(heroes)  
            return True
        
def display_inventory(inventory):
    if not inventory:
        print("Inventário vazio.")
        return
    for idx, item in enumerate(inventory, start=1):
        buffs = ", ".join([f"{stat}: {value}" for stat, value in item['buffs'].items()])
        print(f"{idx}. {item['name']} ({buffs})")

def show_heroes(heroes):
    if not heroes:
        print("Nenhum herói criado.")
    else:
        for idx, hero in enumerate(heroes, start=1):
            print(f"{idx}. Herói: {hero.get_name()}, Classe: {hero.get_class()}, Nível: {hero.get_level()}, Experiência: {hero.get_experience()}, Mana: {hero.get_mana()}, Mana Negra: {hero.get_black_mana()}, Vitalidade: {hero.get_vitality()}, Arcano: {hero.get_arcane()}, Velocidade: {hero.get_speed()}, Ataque: {hero.get_attack()}, Habilidades: {', '.join(hero.get_abilities())}")
        print("\nOpções adicionais:")
        print("1. Excluir um herói")
        print("2. Voltar")
        choice = input("Escolha uma opção: ")
        if choice == "1":
            while True:
                hero_choice_input = input("Digite o número do herói: ").strip()
                if hero_choice_input.isdigit():
                    hero_choice = int(hero_choice_input) - 1
                    if 0 <= hero_choice < len(heroes):  
                        break
                    else:
                        print("Número fora do intervalo. Tente novamente.")
                else:
                    print("Entrada inválida. Por favor, digite um número válido.")
            if 0 <= hero_choice < len(heroes):
                confirmation = input(f"Tem certeza que deseja excluir {heroes[hero_choice].get_name()}? (s/n): ")
                if confirmation.lower() == "s":
                    removed_hero = heroes.pop(hero_choice)
                    save_heroes(heroes)  
                    print(f"{removed_hero.get_name()} foi excluído com sucesso.")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Escolha inválida.")

def create_hero(heroes):
    if len(heroes) >= 4:
        print("Número máximo de heróis alcançado. Exclua um herói antes de criar um novo.")
        return

    name = input("Nome do herói: ")
    print("Escolha o tipo de herói:")
    print("1. Mago\n2. Cavaleiro\n3. Profeta\n4. Necromante\n5. Assassino\n6. Tanque")
    hero_type = input("Digite o número correspondente: ")
    if hero_type == '1':
        heroes.append(Hero(name, "Mago", mana=70, black_mana=0, vitality=40, arcane=60, speed=50, attack=30))
    elif hero_type == '2':
        heroes.append(Hero(name, "Cavaleiro", mana=40, black_mana=0, vitality=70, arcane=30, speed=50, attack=50))
    elif hero_type == '3':
        heroes.append(Hero(name, "Profeta", mana=80, black_mana=0, vitality=50, arcane=70, speed=40, attack=20))
    elif hero_type == '4':
        heroes.append(Hero(name, "Necromante", mana=0, black_mana=50, vitality=40, arcane=80, speed=30, attack=25))
    elif hero_type == '5':
        heroes.append(Hero(name, "Assassino", mana=30, black_mana=0, vitality=50, arcane=20, speed=80, attack=70))
    elif hero_type == '6':
        heroes.append(Hero(name, "Tanque", mana=50, black_mana=0, vitality=90, arcane=30, speed=40, attack=25))
    else:
        print("Tipo de herói inválido.")
        return
    
    print("Herói criado com sucesso!")

def save_heroes(heroes):
    with open("jogoobash.json", "w") as file:
        data = [hero.serialize() for hero in heroes]
        json.dump(data, file, indent=4)

def load_heroes():
    try:
        with open("jogoobash.json", "r") as file:
            content = file.read()
            if not content.strip():  
                return []
            data = json.loads(content)
            return [Hero.deserialize(hero_data) for hero_data in data]
    except FileNotFoundError:
        return []  
    except json.JSONDecodeError:
        return []  

def show_class_info():
    classes = {
        "Mago": Hero("Exemplo", "Mago", mana=70, black_mana=0, vitality=40, arcane=60, speed=50, attack=30),
        "Cavaleiro": Hero("Exemplo", "Cavaleiro", mana=40, black_mana=0, vitality=70, arcane=30, speed=50, attack=50),
        "Profeta": Hero("Exemplo", "Profeta", mana=80, black_mana=0, vitality=50, arcane=70, speed=40, attack=20),
        "Necromante": Hero("Exemplo", "Necromante", mana=0, black_mana=50, vitality=40, arcane=80, speed=30, attack=25),
        "Assassino": Hero("Exemplo", "Assassino", mana=30, black_mana=0, vitality=50, arcane=20, speed=80, attack=70),
        "Tanque": Hero("Exemplo", "Tanque", mana=50, black_mana=0, vitality=90, arcane=30, speed=40, attack=25)
    }
    for class_name, hero in classes.items():
        print(f"Classe: {class_name}")
        print(f"Mana: {hero.get_mana()}, Mana Negra: {hero.get_black_mana()}, Vitalidade: {hero.get_vitality()}, Arcano: {hero.get_arcane()}, Velocidade: {hero.get_speed()}, Ataque: {hero.get_attack()}")
        print("-" * 30)

def get_random_event(hero):
    events = [
        "Você encontrou um baú de tesouro!",
        "Você caiu em uma armadilha e perdeu 10 pontos de vitalidade!",
        "Um mercador misterioso apareceu e oferece um item raro.",
        "Você encontrou um NPC que precisa de ajuda com uma missão.",
        "Um monstro raro apareceu! Prepare-se para lutar!"
    ]
    event = random.choice(events)
    print(event)

    if event == "Você encontrou um baú de tesouro!":
        loot = {"name": "Joia Rara", "value": 100}
        shared_inventory.append(loot)
        print(f"Você adicionou {loot['name']} ao inventário compartilhado!")

    elif event == "Você caiu em uma armadilha e perdeu 10 pontos de vitalidade!":
        hero.set_vitality(max(hero.get_vitality() - 10, 0))
        print(f"Vitalidade de {hero.get_name()} agora é {hero.get_vitality()}.")

    elif event == "Um mercador misterioso apareceu e oferece um item raro.":
        shop_items = [
            {"name": "Espada de Luz", "buffs": {"attack": 10}, "price": 50},
            {"name": "Armadura de Mithril", "buffs": {"vitality": 20}, "price": 75},
            {"name": "Poção Arcana", "buffs": {"arcane": 15}, "price": 40},
            {"name": "Botas da Agilidade", "buffs": {"speed": 10}, "price": 30},
        ]
        print("O mercador oferece os seguintes itens:")
        for idx, item in enumerate(shop_items, start=1):
            buffs = ", ".join(f"{stat}: +{value}" for stat, value in item["buffs"].items())
            print(f"{idx}. {item['name']} (Buffs: {buffs}) - Preço: {item['price']} moedas")
        choice = input("Escolha um item para comprar (ou pressione Enter para cancelar): ")
        if choice.isdigit() and 1 <= int(choice) <= len(shop_items):
            selected_item = shop_items[int(choice) - 1]
            if hero.spend_coins(selected_item["price"]):
                hero.add_item_to_inventory(selected_item)
                print(f"Você comprou {selected_item['name']}!")
            else:
                print("Moedas insuficientes!")

    elif event == "Você encontrou um NPC que precisa de ajuda com uma missão.":
        mission = {
            "name": "Proteger a vila",
            "description": "Derrote 5 goblins que estão atacando a vila.",
            "reward": {"experience": 50, "gold": 20}
        }
        print(f"Missão: {mission['name']}\nDescrição: {mission['description']}")
        accept = input("Deseja aceitar a missão? (s/n): ")
        if accept.lower() == 's':
            complete_mission(hero, mission)

    elif event == "Um monstro raro apareceu! Prepare-se para lutar!":
        monster = Monster("Dragão Jovem", "Dragão", level=10, vitality=100, attack=30)
        fight_with_loot(hero, monster, heroes)

def complete_mission(hero, mission):
    print(f"Você aceitou a missão: {mission['name']}")
    success = random.choice([True, False])  # Determina aleatoriamente se a missão foi concluída
    if success:
        print(f"Você completou a missão: {mission['name']}! Recebeu {mission['reward']['experience']} de experiência e {mission['reward']['gold']} moedas.")
        hero.gain_experience(mission['reward']['experience'])
        hero.get_inventory().append({"name": "Moedas", "amount": mission['reward']['gold']})
    else:
        print(f"Você falhou na missão: {mission['name']}.")

def explore(hero):
    print(f"{hero.get_name()} está explorando o mundo...")
    chance = random.randint(1, 100)
    if chance <= 50:
        get_random_event(hero)
    else:
        print("Nada aconteceu durante a exploração.")

def main():
    heroes = load_heroes()
    monsters = [

        AdaptiveMonster("Goblin", "Goblin", level=1, vitality=30, attack=10),
        AdaptiveMonster("Orc", "Orc", level=3, vitality=50, attack=15),
        AdaptiveMonster("Golem", "Golem", level=5, vitality=80, attack=20),
        AdaptiveMonster("Lich", "Lich", level=7, vitality=60, attack=25),
        AdaptiveMonster("Elfo", "Elfo", level=4, vitality=40, attack=18),
        AdaptiveMonster("Cérbero", "Cérbero", level=10, vitality=100, attack=30)
    ]

    while True:
        print("1. Criar Herói")
        print("2. Mostrar Heróis")
        print("3. Lutar com Monstro")
        print("4. Mostrar Classes")
        print("5. Inventário")
        print("6. Inventário Compartilhado")
        print("7. Explorar")
        print("8. Salvar e Sair")
        
        choice = input("Escolha uma opção: ").strip()

        if not choice:
            print("Opção inválida. Digite um número correspondente às opções.")
            continue

        if choice == '1':
            create_hero(heroes)

        elif choice == '2':
            show_heroes(heroes)

        elif choice == '3':
            if not heroes:
                print("Nenhum herói criado para lutar.")
                continue
            print("Escolha um herói para lutar:")
            for idx, hero in enumerate(heroes, start=1):
                print(f"{idx}. {hero.get_name()} (Classe: {hero.get_class()})")
            hero_choice = int(input("Digite o número do herói: ")) - 1
            if 0 <= hero_choice < len(heroes):
                hero = heroes[hero_choice]
                monster = random.choice(monsters)
                fight_with_loot(hero, monster, heroes)
            else:
                print("Escolha inválida.")

        elif choice == '4':
            show_class_info()

        elif choice == '5':
            print("Escolha um herói para gerenciar o inventário:")
            for idx, hero in enumerate(heroes, start=1):
                print(f"{idx}. {hero.get_name()} (Classe: {hero.get_class()})")
            hero_choice = int(input("Digite o número do herói: ")) - 1
            if 0 <= hero_choice < len(heroes):
                hero = heroes[hero_choice]
                print("\n1. Ver inventário")
                print("2. Equipar item")
                print("3. Remover item equipado")
                inventory_choice = input("Escolha uma opção: ")
                if inventory_choice == '1':
                    print("Inventário:", hero.get_inventory())
                    print("Equipados:", [item['name'] for item in hero.get_equipped_items()])
                elif inventory_choice == '2':
                    print("Inventário:", hero.get_inventory())
                    item_name = input("Digite o nome do item para equipar: ")
                    for item in hero.get_inventory():
                        if item['name'] == item_name:
                            hero.equip_item(item)
                            hero.apply_buffs()
                            break
                    else:
                        print("Item não encontrado.")
                elif inventory_choice == '3':
                    print("Equipados:", [item['name'] for item in hero.get_equipped_items()])
                    item_name = input("Digite o nome do item para remover: ")
                    hero.unequip_item(item_name)

        elif choice == '6':  
            print("Inventário Compartilhado:")
            for idx, item in enumerate(shared_inventory, start=1):
                buffs = item.get("buffs", "Sem buffs")
                print(f"{idx}. {item['name']} - Buffs: {buffs}")
    
            print("\n1. Usar item")
            print("2. Voltar")
            inventory_choice = input("Escolha uma opção: ")

            if inventory_choice == '1':
                item_idx = int(input("Digite o número do item a ser usado: ")) - 1
                if 0 <= item_idx < len(shared_inventory):
                    item = shared_inventory.pop(item_idx)
                    print(f"Você usou {item['name']}.")
                    if "vitality" in item['buffs']:
                        print("Escolha um herói para usar o item:")
                        for idx, hero in enumerate(heroes, start=1):
                            print(f"{idx}. {hero.get_name()} (Vitalidade: {hero.get_vitality()})")
                        hero_choice = int(input("Digite o número do herói: ")) - 1
                        if 0 <= hero_choice < len(heroes):
                            hero = heroes[hero_choice]
                            hero.set_vitality(hero.get_vitality() + item['buffs']['vitality'])
                            print(f"{hero.get_name()} agora tem {hero.get_vitality()} de vitalidade!")
                        else:
                            print("Herói inválido.")
                else:
                    print("Item inválido.")

        if choice == '7':
            if not heroes:
                print("Nenhum herói criado para explorar.")
                continue
            print("Escolha um herói para explorar:")
            for idx, hero in enumerate(heroes, start=1):
                print(f"{idx}. {hero.get_name()} (Classe: {hero.get_class()})")
            hero_choice = int(input("Digite o número do herói: ")) - 1
            if 0 <= hero_choice < len(heroes):
                hero = heroes[hero_choice]
                explore(hero)
            else:
                print("Escolha inválida.")


        elif choice == '8': 
            save_heroes(heroes)
            print("Progresso salvo. Até logo!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
