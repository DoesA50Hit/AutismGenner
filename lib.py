from words import adjectives, nouns  # Import adjectives and nouns from words.py

# :::::::::::::::::::::::::::
# Word List Setup
# :::::::::::::::::::::::::::

# Convert tuples to lists and combine them into a single WORDS list
WORDS = [word for word in list(adjectives) + list(nouns) if isinstance(word, str) and word.isalpha() and len(word) > 2]

# :::::::::::::::::::::::::::

CLASSES = {
    "Blaster" : "You attack from range with precision or overwhelming force—but your power falters up close. + 2 range, +1 control",
    "Striker" : "You need physical contact to activate your power, turning touch into a weapon or tool. + 2 attack, +2 control, 0 range +1 speed"
    "Shaker" :  "You alter the battlefield itself, but your control weakens with distance from the epicenter. +2 range, +1 control",
    "Mover" : "You defy movement laws (speed, flight, teleportation etc.), but momentum or cooldowns limit you. +3 speed",
    "Master" :  "You control minions, illusions, or emotions—but your influence wanes if your ‘puppets’ are destroyed. +2 control, -1 speed, +2 range",
    "Changer" : "You alter your body’s form, but the more you deviate from human, the harder it is to revert. +2 attack/defense, -1 control",
    "Breaker" : "You toggle between states that defy physics (intangibility, energy forms, etc), but your human side suffers. -3 control, +3 attack +3 defense",
    "Architect" : "You create persistent structures (portals, fortresses, etc), but they degrade or corrupt over time. +2 to controls +1 to defense",
    "Catalyst" :  "You empower others in some way, but their boosted abilities backfire on you. +2 to range, +2 to control, -1 to defense",
    "Flux" : "Your power mutates randomly (elements, effects, etc.), cycling through unstable ‘modes’. Auto 0 in control. +3 to attack and defense",
    "Nexus" : "You link minds, souls, or fates or something else entierly—but bonds go both ways. +2 control, + 1 range",
    "Husk" : "You consume matter/energy to fuel yourself, but lose humanity with each ‘meal’. +1 Speed, +1 Defense, +1 Attack, - 1 Control",
    "Fracture" : "Your power splits objects/yourself into parallel versions, but they gradually develop divergent wills. +2 attack, +3 defense, -3 control",
    "Tide" : "Your abilities wax and wane cyclically. +1 to all stats besides control,  -2 controls",
    "Vessel" :  "You channel energy/entities, but the more you hold, the less control you retain.   +1 control, +2 attack, -1 defense",
    "Paragon" : "You embody an ideal (justice, hunger, etc.), gaining power when acting in alignment—but the ideal consumes you over time. +2 attack, +2 Control, -1 Defense",
    "Anima" :  "You manifest a semi-sentient energy construct (animal, weapon, avatar) that reflects your subconscious. +1 attack, +2 defense, +1 control",
    "Leyline" : "You draw power from specific locations or patterns, becoming stronger in designated zones but weaker elsewhere. +2 attack, +1 range/control, -1 defense",
    "Ouroboros" : "Your abilities improve through self-harm or sacrifice, creating paradoxically sustainable feedback loops. +2 attack, +2 Defense, -1 Control",
    "Monolith" : "You embody an immutable law (e.g., ‘all wounds you inflict scar permanently’ or ‘you cannot be perceived from behind’ or something else entierly), but cannot circumvent it yourself. +2 Defense, +2 Control, -1 Speed",
    "Spore" :  "Your power ‘infects’ targets or areas in one way or another, creating dormant effects that activate under triggers. +2 attack, +2 control, -1 speed",
    "Zenith" : "Your power peaks during specific, rare situational and is inert otherwise. +3 attack, +1 speed, -2 control",
    "Gambling" : "Your power scales with risk—the more you stake (health, memories, allies etc), the greater the reward. But the house always wins eventually. + 2 to everything but 0 in control",
    "Thread" : "You create connections between things, transferring properties along them. + 3 range, +2 control, -2 attack",
    "Anchor" :  "You negate or cancel specific phenomena that are not the norm of reality such as powers, but cannot create anything yourself. Max Control for your level, Auto 0 in your attack"
}
