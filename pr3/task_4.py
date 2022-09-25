import plotly.graph_objs as go
import plotly.express as px
from task_2 import get_population_2020_with_task2


def task_4(world_population_2020):
    pie = go.Figure()
    pie.add_trace(go.Pie(labels=world_population_2020['Country'], values=world_population_2020['Population']))

    # копия из task_3
    pie.update_traces(marker=dict(colors=world_population_2020['Population']))
    pie.update_layout(
        title='Диаграмма популяции стран в 2020',
        title_x=0.5,
        title_font_size=20,
        xaxis_title='Страны',
        yaxis_title='Популяция',
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        xaxis_tickangle=90,
        xaxis_tickfont_size=14,
        yaxis_tickfont_size=14,
    )
    pie.update_yaxes(nticks=20)

    pie.show()


if __name__ == '__main__':
    task_4(get_population_2020_with_task2())
