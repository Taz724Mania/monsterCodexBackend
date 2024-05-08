from django.db import models

class Codex(models.Model):

    name=models.TextField("")

    description=models.TextField("")

    size=models.TextChoices("tiny", "small", "medium", "large", "huge", "gargantuan")

    type=models.TextChoices("Aberration", "Beast", "Celestial", "Construct", "Dragon", "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Swarm", "Undead")

    alignement=models.TextChoices("Chaotic Evil", "Lawful Evil", "Evil", "Chaotic Good", "Lawful Good", "Good", "Neutral Evil", "Neutral Good", "True Neutral", "Unaligned")

    armorClass=models.PositiveIntegerField()

    hitPoints=models.PositiveIntegerField()

    hitDice=models.TextField("")

    

