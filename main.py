# %%
import plotly.express as px
import pandas as pd

# %%
df1 = pd.read_csv("data\epl-players-expectedasistsper90.csv")
df2 = pd.read_csv("data\epl-players-prgPper90.csv")

# %%
df1_new_header = df1.iloc[0] 
df1 = df1[1:]  
df1.columns = df1_new_header 

df1.reset_index(drop=True, inplace=True)


# %%
df2_new_header = df2.iloc[0] 
df2 = df2[1:]  
df2.columns = df2_new_header 

df2.reset_index(drop=True, inplace=True)


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
            y=1.05,  
        )
    ],
    xaxis_title='Expected Assists per90',
    xaxis_title_font=dict(size=18),
    yaxis_title='Progressive Passes per90',
    yaxis_title_font=dict(size=18),
)

pass_fig.write_html("index.html") 



