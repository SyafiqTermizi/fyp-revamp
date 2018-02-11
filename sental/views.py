from django.shortcuts import render
from twittur.models import SearchItem, Tweets
from twittur.models import Tweets

from . import classify
from .fusioncharts import FusionCharts

def index(request):
    saved_searched = SearchItem.objects.filter(user=request.user.id)
    return render(request, 'sental/index.html', {'saved_search':saved_searched})

def analyse(request, search_id):
    tweets = Tweets.objects.filter(search_word=search_id)
    sental = classify.analyse(tweets)

    neg = 0
    pos = 0
    neut = 0
    for x in sental:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            neut += 1

    context = {
        'neg': neg,
        'pos': pos,
        'neut': neut,
    }

    pie_chart = {}
    pie_chart['chart'] = {
        "caption": "Analysis Result",
        "subCaption": " ",
        "numberPrefix": "$",
        "showBorder": "0",
        "use3DLighting": "0",
        "enableSmartLabels": "0",
        "startingAngle": "310",
        "showLabels": "0",
        "showPercentValues": "1",
        "showLegend": "1",
        "defaultCenterLabel": "Total revenue: $64.08K",
        "centerLabel": "Revenue from $label: $value",
        "centerLabelBold": "1",
        "showTooltip": "0",
        "decimals": "0",
        "useDataPlotColorForLabels": "1",
        "theme": "zune"
    }
    pie_chart['data'] = [
        {
            "label": "Negative Tweets",
            "value": neg
        },
        {
            "label": "Positive Tweets",
            "value": pos
        },
        {
            "label": "Neutral Tweets",
            "value": neut
        },
    ]

    pie = FusionCharts('pie2d', 'pie', '600', '400', 'chart', 'json', pie_chart)
 
    return render(request, 'sental/analyse.html', {'output': pie.render()})