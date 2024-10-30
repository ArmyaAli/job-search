import plotly.graph_objects as go

labels = [
    "Job Application: 53",
    "Direct²: 32",
    "Handshake: 7",
    "Linkedin: 6",
    "Career Centre: 7",
    "Network: 1",
    "Rejected: 20",
    "No Response: 12",
    "Cancelled: 7",
    "Interview: 7",
    "Assessment: 3",
    "Waiting³: 10",
    "Offer: 4",
]

sources = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 10, 9, 9, 9]

targets = [1, 2, 3, 4, 5, 10, 8, 9, 7, 6, 11, 8, 9, 7, 6, 11, 6, 11, 9, 11, 9, 6, 12, 6, 11]

values = [32, 7, 6, 7, 1, 3, 4, 2, 11, 11, 1, 3, 1, 1, 1, 1, 3, 3, 3, 4, 1, 3, 4, 2, 1]

fig = go.Figure(
    data=go.Sankey(
        node=dict(
            thickness=20, line=dict(color="black", width=0.5), label=labels, pad=50
        ),
        link=dict(source=sources, target=targets, value=values, label=values),
    )
)

fig.update_layout(
    width=1200,
    height=800,
    font=dict(size=16),
    title=dict(
        text="<b>Yu En's 2020 Summer Internship Research<sup>1</sup></b>",
        font=dict(size=22),
        xanchor="center",
        yanchor="top",
        x=0.5,
        y=0.95,
    ),
    annotations=[
        dict(
            text="<b>Note<sup>1</sup></b>: from Feb 03, 2020 to Apr 30, 2020<br><b>Note<sup>2</sup></b>: includes applying directly after learning about the opening<br><b>Note<sup>3</sup></b>: if the waiting period is longer than 3 months, the status is changed to no response",
            xref="paper",
            yref="paper",
            x=0,
            y=-0.1,
            align="left",
            showarrow=False,
            font=dict(size=13),
        )
    ],
)

fig.show()
