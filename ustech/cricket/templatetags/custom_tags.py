from django import template

register = template.Library()

import datetime


@register.filter(name='day')
def day(eventdate):
    date, time = eventdate.split('T',2)
    year, month, day = date.split('-',3)
    return day


@register.filter(name='month')
def month(eventdate):
    date, time = eventdate.split('T', 2)
    startDateTime = datetime.datetime.strptime(date, "%Y-%m-%d")
    month = startDateTime.strftime("%B")
    return month

@register.filter(name='date')
def date(eventdate):
    date, time = eventdate.split('T', 2)
    startDateTime = datetime.datetime.strptime(date, "%Y-%m-%d")
    d= startDateTime.strftime("%Y-%b-%d")
    return d


@register.filter(name='time')
def time(datea):
    print(datea)
    # return datea
    
    return datetime.datetime.strptime(
        datea, '%Y-%m-%dT%H:%M').strftime('%b %d %I:%M %p')
    
