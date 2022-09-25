import plotly.graph_objs as go
import plotly.express as px
from task_2 import get_population_2020_with_task2


def task_3(world_population_2020):
    # 3.1
    bar = go.Figure(px.bar(x=world_population_2020['Country'], y=world_population_2020['Population']))
    # 3.2
    bar.update_traces(marker=dict(color=world_population_2020['Population'], coloraxis='coloraxis'))
    # 3.3-3.5
    bar.update_layout(
        # 3.3
        title='Диаграмма популяции стран в 2020',
        title_x=0.5,
        title_font_size=20,
        # 3.4
        xaxis_title='Страны',
        yaxis_title='Популяция',
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        xaxis_tickangle=90,
        # 3.5
        xaxis_tickfont_size=14,
        yaxis_tickfont_size=14,
    )
    # 3.4
    bar.update_yaxes(nticks=20)

    bar.show()


if __name__ == '__main__':
    task_3(get_population_2020_with_task2())
