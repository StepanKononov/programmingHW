import plotly.express as px
data = dict(
    character=["Россия ", "Германия", "Франция", "Норвегия", "Аврика", "Финляндия", "Швеция", "Англия", "Мальдивы"],
    parent=["Регионы", "dfdf", "Регионы", "Регионы", "Регионы", "Регионы", "Регионы", "Регионы", "Регионы" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig =px.sunburst(
    data,
    path=['parent', 'character'],
    values='value'

)
fig.show()