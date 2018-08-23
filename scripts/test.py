import pdfkit
import requests
import json
from json2html import *


def main():
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'
    payload = {
    # parses school JSON data from url and joins it to API query
    # string
        'api_key': "xEkxcoO8n1pP7Mird5j4bmrXj13pnNcndpCoKb9I",
        '_fields': ','.join([
            'school.name',
            'school.school_url',
            'school.city',
            'school.state',
            'school.zip',
            '2015.student.size',
        ]),
        'school.operating': '1',
        '2015.academics.program_available.assoc_or_bachelors': 'true',
        '2015.student.size__range': '1..',
        'school.degrees_awarded.predominant__range': '1..3',
        'school.degrees_awarded.highest__range': '2..4',
        'id': '240444',
    }
    # appends data to HTML file as string.
    data = requests.get(url, params=payload).json()
    formatted_json = json.dumps(data["results"])
    index= open("index.html","a")
    index.write(formatted_json)
    index.close()

main()

def data_race():
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'
    payload = {
        'api_key': "xEkxcoO8n1pP7Mird5j4bmrXj13pnNcndpCoKb9I",
        '_fields': ','.join([
            '2015.student.demographics.race_ethnicity.white',
            '2015.student.demographics.race_ethnicity.black',
            '2015.student.demographics.race_ethnicity.hispanic',
            '2015.student.demographics.race_ethnicity.asian',
            '2015.student.demographics.race_ethnicity.aian',
            '2015.student.demographics.race_ethnicity.nhpi',
            '2015.student.demographics.race_ethnicity.two_or_more',
            '2015.student.demographics.race_ethnicity.non_resident_alien',
            '2015.student.demographics.race_ethnicity.unknown',
        ]),
        'school.operating': '1',
        '2015.academics.program_available.assoc_or_bachelors': 'true',
        '2015.student.size__range': '1..',
        'school.degrees_awarded.predominant__range': '1..3',
        'school.degrees_awarded.highest__range': '2..4',
        'id': '240444',
    }
    data = requests.get(url, params=payload).json()
    # prints all JSON data on vm environment
    formatted_json = json.dumps(data["results"])
    index= open("index.html","a")
    index.write(formatted_json)
    index.close()

data_race()

def data_program_percentage():
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'
    payload = {
        'api_key': "xEkxcoO8n1pP7Mird5j4bmrXj13pnNcndpCoKb9I",
        '_fields': ','.join([
            '2015.academics.program_percentage.agriculture',
            '2015.academics.program_percentage.resources',
            '2015.academics.program_percentage.architecture',
            '2015.academics.program_percentage.ethnic_cultural_gender',
            '2015.academics.program_percentage.communication',
            '2015.academics.program_percentage.computer',
            '2015.academics.program_percentage.education',
            '2015.academics.program_percentage.engineering',
            '2015.academics.program_percentage.language',
            '2015.academics.program_percentage.family_consumer_science',
            '2015.academics.program_percentage.legal',
            '2015.academics.program_percentage.english',
            '2015.academics.program_percentage.biological',
            '2015.academics.program_percentage.mathematics',
            '2015.academics.program_percentage.multidiscipline',
            '2015.academics.program_percentage.parks_recreation_fitness',
            '2015.academics.program_percentage.philosophy_religious',
            '2015.academics.program_percentage.physical_science',
            '2015.academics.program_percentage.psychology',
            '2015.academics.program_percentage.public_administration_social_service',
            '2015.academics.program_percentage.social_science',
            '2015.academics.program_percentage.visual_performing',
            '2015.academics.program_percentage.health',
            '2015.academics.program_percentage.business_marketing',
            '2015.academics.program_percentage.history',
        ]),
        'school.operating': '1',
        '2015.academics.program_available.assoc_or_bachelors': 'true',
        '2015.student.size__range': '1..',
        'school.degrees_awarded.predominant__range': '1..3',
        'school.degrees_awarded.highest__range': '2..4',
        'id': '240444',
    }
    data = requests.get(url, params=payload).json()
    formatted_json = json.dumps(data["results"])
    index= open("index.html","a")
    index.write(formatted_json)
    index.close()

data_program_percentage()

def data_public_net_price():
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'
    payload = {
        'api_key': "xEkxcoO8n1pP7Mird5j4bmrXj13pnNcndpCoKb9I",
        '_fields': ','.join([
            '2015.cost.net_price.public.by_income_level.0-30000',
            '2015.cost.net_price.public.by_income_level.30001-48000',
            '2015.cost.net_price.public.by_income_level.48001-75000',
            '2015.cost.net_price.public.by_income_level.75001-110000',
            '2015.cost.net_price.public.by_income_level.110001-plus',
        ]),
        'school.operating': '1',
        '2015.academics.program_available.assoc_or_bachelors': 'true',
        '2015.student.size__range': '1..',
        'school.degrees_awarded.predominant__range': '1..3',
        'school.degrees_awarded.highest__range': '2..4',
        'id': '240444',
    }
    data = requests.get(url, params=payload).json()
    formatted_json = json.dumps(data["results"])
    index= open("index.html","a")
    index.write(formatted_json)
    index.close()

data_public_net_price()

def parent_educational_level():
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'
    payload = {
        'api_key': "xEkxcoO8n1pP7Mird5j4bmrXj13pnNcndpCoKb9I",
        '_fields': ','.join([
            '2015.student.share_firstgeneration_parents.middleschool',
            '2015.student.share_firstgeneration_parents.highschool',
            '2015.student.share_firstgeneration_parents.somecollege',
        ]),
        'school.operating': '1',
        '2015.academics.program_available.assoc_or_bachelors': 'true',
        '2015.student.size__range': '1..',
        'school.degrees_awarded.predominant__range': '1..3',
        'school.degrees_awarded.highest__range': '2..4',
        'id': '240444',
    }
    data = requests.get(url, params=payload).json()
    formatted_json = json.dumps(data["results"])
    index= open("index.html","a")
    index.write(formatted_json)
    index.close()

parent_educational_level()
