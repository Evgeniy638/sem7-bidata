import plotly.graph_objs as go
import plotly.express as px
from task_2 import get_population_russia_with_task2


def task_5(world_population):
    line = go.Figure()

    line.add_trace(go.Scatter(
        x=world_population['Year'],
        y=world_population['Population'],
        mode='lines+markers',
        name='динамика популяции России с 1955 до 2020'
    ))

    # 5.1
    line.update_traces(
        line=dict(color="crimson"),
        marker=dict(
            color='darkblue',
            line=dict(color='blue', width=2)
        )
    )

    # 5.2
    line.update_traces(showlegend=True)
    line.update_layout(legend_x=0, legend_y=0)

    # 5.3
    line.update_xaxes(gridcolor='azure')
    line.update_yaxes(gridcolor='azure')

    # 5.4
    line.update_layout(
        title='Диаграмма популяции России с 1955 до 2020',
        title_x=0.5,
        title_font_size=20,
        xaxis_title='Годы',
        yaxis_title='Популяция',
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        xaxis_tickangle=90,
        xaxis_tickfont_size=14,
        yaxis_tickfont_size=14,
    )
    line.update_yaxes(nticks=20)

    line.show()


if __name__ == '__main__':
    task_5(get_population_russia_with_task2())
