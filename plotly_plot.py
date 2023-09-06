import plotly.graph_objs


class Plot:
    def draw(self, hours, temperatures):
        fig = plotly.graph_objs.Figure(
            plotly.graph_objs.Scatter(x=hours, y=temperatures)
        )
        fig.show()
