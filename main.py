# %%
import plotly.express as px
import pandas as pd

# %%
df1 = pd.read_csv("data\epl-players-expectedasistsper90.csv")
df2 = pd.read_csv("data\epl-players-prgPper90.csv")

# %%
def set_first_row_as_header(df):
    new_header = df.iloc[0]
    df = df[1:].copy()
    df.columns = new_header
    df.reset_index(drop=True, inplace=True)
    return df

# %%
df1 = set_first_row_as_header(df1)


# %%
df2 = set_first_row_as_header(df2)

# %%
df1.head()

# %%
df2.head()

# %%

epl_player_passing_data = pd.merge(df1, df2, on=['Player','90s', "Pos"], how='inner')
epl_player_passing_data = epl_player_passing_data[['Player', 'Pos', 'PrgP', 'xA', '90s']]

epl_player_passing_data.head()

# %%
epl_player_passing_data["90s"] = pd.to_numeric(epl_player_passing_data["90s"], errors='coerce')
epl_player_passing_data["90s"]

# %%
epl_player_passing_data["xA"] = pd.to_numeric(epl_player_passing_data["xA"], errors='coerce')
epl_player_passing_data["xA"]

# %%
epl_player_passing_data["xA/90s"] = epl_player_passing_data["xA"] / epl_player_passing_data["90s"]

epl_player_passing_data["xA/90s"]

# %%
epl_player_passing_data["PrgP"] = pd.to_numeric(epl_player_passing_data["PrgP"], errors="coerce")
epl_player_passing_data["PrgP"]

# %%
epl_player_passing_data["PrgP/90s"] = epl_player_passing_data["PrgP"] / epl_player_passing_data["90s"]

epl_player_passing_data["PrgP/90s"]

# %%
pass_fig = px.scatter(x=epl_player_passing_data["xA/90s"], y=epl_player_passing_data["PrgP/90s"], color=epl_player_passing_data["Pos"], symbol=epl_player_passing_data["Pos"], title="Progression and Final Pass", text=epl_player_passing_data['Player'])
pass_fig.update_layout(
    title_font=dict(size=30),
    title_x=0.48,
    annotations = [
        dict(
            text='Premier League 2024/25, GW10, Minimum 400 Minutes Played',
            xref='paper', 
            yref='paper',
            showarrow=False,
            x=0.5,  
            y=1.1,  
        )
    ],
    xaxis_title='Expected Assists per90',
    xaxis_title_font=dict(size=18),
    yaxis_title='Progressive Passes per90',
    yaxis_title_font=dict(size=18),
)

# %%
epl_keepers = pd.read_csv('data\epl-keepers-save-statistics.csv')
epl_keepers = set_first_row_as_header(epl_keepers)
epl_keepers = df = epl_keepers.iloc[1:].reset_index(drop=True)

# %%
epl_keepers["90s"] = epl_keepers["90s"].astype(float)
epl_keepers["Save%"] = epl_keepers["Save%"].astype(float)
epl_keepers["SoTA"] = epl_keepers["SoTA"].astype(float)

# %%
epl_keepers["Save%/90s"] = epl_keepers["Save%"] / epl_keepers["90s"]
epl_keepers["SoTA/90s"] = epl_keepers["SoTA"] / epl_keepers["90s"]

# %%
gk_fig = px.scatter(x=epl_keepers["SoTA/90s"], y=epl_keepers["Save%/90s"] , title="Shots Against and Saves", text=epl_keepers['Player'])
gk_fig.update_layout(
    title_font=dict(size=30),
    title_x=0.48,
    annotations = [
        dict(
            text='Premier League 2024/25, GW11, Minimum 400 Minutes Played',
            xref='paper', 
            yref='paper',
            showarrow=False,
            x=0.5,  
            y=1.1,  
        )
    ],
    xaxis_title='Shots On Target Against',
    xaxis_title_font=dict(size=18),
    yaxis_title='Save%',
    yaxis_title_font=dict(size=18),
)
with open('index.html', 'a') as f:
    f.write(pass_fig.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(gk_fig.to_html(full_html=False, include_plotlyjs='cdn'))


