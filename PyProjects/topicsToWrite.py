from random import randint

list_o_topics = {0: "Fantasy", 1: "Sci-Fi", 3: "Noir", 4: "Contemporary", 5: "Romantic"}
list_o_themes = {0: "Death", 1: "Alcohol", 2: "Faith", 3: "Shades of Grey", 4: "Dreams", 5: "Displacement",
6: "Solitude", 7: "Lonliness", 8: "Loss", 9: "Survival", 10: "Boredom"}
list_o_tones  = {0: "Humorous", 1: "Serious", 2: "Reserved", 3: "Surreal"}

topic = randint(0, len(list_o_topics))
theme = randint(0, len(list_o_themes))
tone  = randint(0, len(list_o_tones))

print "Topic is %s, and central theme is %s, with a %s tone" % (list_o_topics[topic], list_o_themes[theme], list_o_tones[tone])