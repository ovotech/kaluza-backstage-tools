import csv
from typing import List
import jinja2

def extractLinks(architecturalLinks, technicalLinks, supportLinks):
    links = []
    
    for link in architecturalLinks:
        links.append({"title": "Architecture", "url": link, "icon": "docs"})

    for link in technicalLinks:
        links.append({"title": "Technical", "url": link, "icon": "docs"})

    for link in supportLinks:
        links.append({"title": "Support", "url": link, "icon": "docs"})

    return links


with open('batch-catalog-template.yaml') as template:
    template_jinja = jinja2.Environment().from_string(template.read())
    with open('file.csv') as f:
        reader = csv.DictReader(f)
        data = list(reader)

        created_systems: List = []

        for entity in data:
            entity["tags"] = entity["tags"].split("\n")
            entity["links"] = extractLinks(entity["architectureLinks"].split("\n"), entity["technicalLinks"].split("\n"), entity["supportLinks"].split("\n"))
            entity["dependsOn"] = entity["dependsOn"].split("\n")
            entity["consumesApis"] = entity["consumesApis"].split("\n")
            entity["providesApis"] = entity["providesApis"].split("\n")

            if(entity["system"] in created_systems):
                entity["system"] = None
            else:
                created_systems.append(entity["system"])

            result = template_jinja.render(entity)
            open('catalog-info-' + entity["githubSlug"].split("/")[1] + '.yaml', 'a+').write(result + "\n")
