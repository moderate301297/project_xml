# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CareerBuilderItem(scrapy.Item):
    job_title = scrapy.Field()
    job_description = scrapy.Field()
    job_requirements = scrapy.Field()
    address = scrapy.Field()
    categories = scrapy.Field()
    end_date = scrapy.Field()
    update_date = scrapy.Field()
    salary = scrapy.Field()
    position = scrapy.Field()
    other_information = scrapy.Field()
    company_name = scrapy.Field()
    company_address = scrapy.Field()
    company_size = scrapy.Field()
    experiment_required = scrapy.Field()
    benefits = scrapy.Field()
    job_description = scrapy.Field()
    job_requirements = scrapy.Field()
    diploma = scrapy.Field()
    age = scrapy.Field()
    sex = scrapy.Field()
    job_type = scrapy.Field()
    time_trail_work = scrapy.Field()
    time_work = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()


class CareerLinkItem(scrapy.Item):
    job_title = scrapy.Field()
    address = scrapy.Field()
    salary = scrapy.Field()
    job_description = scrapy.Field()
    skills = scrapy.Field()
    categories = scrapy.Field()
    position = scrapy.Field()
    education_requirements = scrapy.Field()
    experience_requirements = scrapy.Field()
    employment_type = scrapy.Field()
    sex = scrapy.Field()
    begin_date = scrapy.Field()
    end_date = scrapy.Field()
    company_name = scrapy.Field()
    company_size = scrapy.Field()
    company_address = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()


class TimViecNhanhItem(scrapy.Item):
    id = scrapy.Field()
    job_title = scrapy.Field()
    address = scrapy.Field()
    company_name = scrapy.Field()
    company_address = scrapy.Field()
    requied_experience = scrapy.Field()
    degree = scrapy.Field()
    number_of_recruitment = scrapy.Field()
    genrder_required = scrapy.Field()
    nature_of_work = scrapy.Field()
    work_form = scrapy.Field()
    dealine_for_submit = scrapy.Field()
    job_description = scrapy.Field()
    requirement = scrapy.Field()

    update_date = scrapy.Field()
    salary = scrapy.Field()
    categories = scrapy.Field()
    sex = scrapy.Field()
    benefits = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()


class MediatedItem(scrapy.Item):
    idx = scrapy.Field()
    job_title = scrapy.Field()
    address = scrapy.Field()
    job_description = scrapy.Field()
    categories = scrapy.Field()
    update_date = scrapy.Field()
    end_date = scrapy.Field()
    salary = scrapy.Field() # xử lý khi cho vào mongodb
    position = scrapy.Field()
    age = scrapy.Field()
    sex = scrapy.Field()
    benefits = scrapy.Field()
    experiment_required = scrapy.Field()
    diploma = scrapy.Field()
    company_name = scrapy.Field()
    company_address = scrapy.Field()
    company_size = scrapy.Field()
    source = scrapy.Field()
