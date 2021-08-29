import plotly
import plotly.graph_objs as G


def get_plot(x_tr, y, theta_0, theta_1):

    plot1 = G.Scatter(x=x_tr, y=y, mode='markers', name='Fact')
    plot2 = G.Scatter(x=[x for x in range(100, 250000, 100)],
                      y=[theta_0 + (x * theta_1) for x in
                      range(100, 250000, 100)],
                      mode='lines', line={'color': '#F48A8A'}, name='Predict')
    layout = G.Layout(title=dict(text='Зависимость стоимости авто от пробега',
                      font=dict(size=28, color='#18171C'), xref="paper",
                      xanchor='left'), xaxis=dict(title='Пробег',
                      titlefont=dict(size=18, color='#18171C')),
                      yaxis=dict(title='Стоимость машины',
                      titlefont=dict(size=18, color='#18171C')))
    fig = G.Figure(data=[plot1, plot2], layout=layout)
    plotly.offline.plot(fig, filename='basic-scatter.html')


def get_plot_error(n, errors):

    plot = G.Scatter(x=[x for x in range(n)], y=errors[1:],
                     mode='lines+markers', line_color='#296DFA', name='Errors')
    layout = G.Layout(title=dict(text='Уменьшение ошибки', font=dict(size=28,
                      color='#18171C'), xref="paper", xanchor='left'),
                      xaxis=dict(title='Количество итераций',
                      titlefont=dict(size=18, color='#18171C')),
                      yaxis=dict(title='Показатель ошибки',
                      titlefont=dict(size=18, color='#18171C')))
    fig = G.Figure(data=[plot], layout=layout)
    plotly.offline.plot(fig, filename='error.html')
