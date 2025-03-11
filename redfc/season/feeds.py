from django_ical.views import ICalFeed

from icalendar import Alarm
from datetime import timedelta

from .models import Match

class MatchFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//redfc.com.br//redfc//PT'
    timezone = 'America/Sao_Paulo'
    file_name = 'feed.ics'

    # def file_name(self, obj):
    #     return "%s_feed.ics" % obj.season.team.name

    def items(self):
        return Match.objects.all().order_by('-schedule')

    def item_title(self, item):
        return item.get_match_title()

    def item_description(self, item):
        return item.get_match_description()
    
    def item_link(self, item):
        return item.get_absolute_url()
    
    def item_location(self, item):
        return item.field.address

    def item_start_datetime(self, item):
        return item.schedule
    
    def item_valarm(self, item):
        valarm = Alarm()
        valarm.add('action', 'display')
        valarm.add('description', item.get_match_title())
        valarm.add('trigger', timedelta(days=-1))
        return [valarm]
