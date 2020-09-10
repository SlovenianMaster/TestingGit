import yaml
data_file = open("site.yaml")
base_site = open("basehtml.yaml")
data = yaml.load(data_file, Loader=yaml.FullLoader)
html = yaml.load(base_site, Loader=yaml.FullLoader)

with open("site.yaml", "r") as stream:
    out = yaml.load(stream, Loader=yaml.FullLoader)
i = 0
ing = out["ingridients"].copy()

with open("pytest.html", "w") as file:
    file.write(html["before_title"])
    file.write(data["title"])
    file.write(html["end_head"])
    file.write(html["body_start"])
    file.write(data["title"])
    file.write(html["h1_end"])
    file.write(html["ing"])
    #ingridients
    file.write(html["ul_start"])
    while i < len(ing):
        file.write(html["li_start"])
        file.write(ing[i])
        file.write(html["li_stop"])
        i = i + 1
    file.write(html["ul_stop"])
    file.write(html["p_start"])
    file.write(data["recepie"])
    file.write(html["p_end"])
    file.write(html["finish"])
