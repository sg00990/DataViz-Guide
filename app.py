import streamlit as st
import pandas as pd
from streamlit_navigation_bar import st_navbar
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import pydeck as pdk

st.set_page_config(
    page_title="Data Viz Guide",
    page_icon="random",
    layout="wide"
)

df = pd.read_excel("shinkansen.xlsx")

df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['Longitude'] = pd.to_numeric(df['Longitude'])
df['Latitude'] = pd.to_numeric(df['Latitude'])

def area_chart():
    st.subheader("*Number of Stations Opened Per Year*")
    stations_per_year = df.groupby('Year').size()
    st.area_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations", color="#6298c0")

    st.write("**Function Signature**")
    code = '''st.area_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, stack=None, width=None, height=None, use_container_width=True)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **data**: Data being plotted (in my case, a pandas DataFrame)
        - **x**: Name of the x column
        - **y**: Name of the y column
        - **x_label**: Label for the x-axis
        - **y_label**: Label for the y-axis
        - **color**: Customize the color(s) used on the chart
        - **stack**: Choose whether or not to stack the areas
        - **width**: Set the width
        - **height**: Set the height
        - **use_container_width**: Overrides the width and sets it to the entire container width
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Group the number of stations by year
    stations_per_year = df.groupby('Year').size()

    # Display Streamlit chart
    st.area_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations", color="#6298c0")'''
    st.code(code, language="python")

def bar_chart():
    st.subheader("*Number of Stations Per Prefecture*")
    stations_per_prefecture = df['Prefecture'].value_counts()
    st.bar_chart(stations_per_prefecture, x_label="Prefecture", y_label="Number of Stations", color="#c18489")

    st.write("**Function Signature**")
    code = '''st.bar_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, horizontal=False, stack=None, width=None, height=None, use_container_width=True)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **data**: Data being plotted (in my case, a pandas DataFrame)
        - **x**: Name of the x column
        - **y**: Name of the y column
        - **x_label**: Label for the x-axis
        - **y_label**: Label for the y-axis
        - **color**: Customize the color(s) used on the chart
        - **horizontal**: Choose whether or not to make the bars horizontal
        - **stack**: Choose whether or not to stack the bars
        - **width**: Set the width
        - **height**: Set the height
        - **use_container_width**: Overrides the width and sets it to the entire container width
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Count number of stations per prefecture
    stations_per_prefecture = df['Prefecture'].value_counts()

    # Display Streamlit chart
    st.bar_chart(stations_per_prefecture, x_label="Prefecture", y_label="Number of Stations", color="#c18489")'''
    st.code(code, language="python")

def line_chart():
    st.subheader("*Stations Opened Per Year*")
    stations_per_year = df.groupby('Year').size()
    st.line_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations", color="#6298c0")

    st.write("**Function Signature**")
    code = '''st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, width=None, height=None, use_container_width=True)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **data**: Data being plotted (in my case, a pandas DataFrame)
        - **x**: Name of the x column
        - **y**: Name of the y column
        - **x_label**: Label for the x-axis
        - **y_label**: Label for the y-axis
        - **color**: Customize the color(s) used on the chart
        - **width**: Set the width
        - **height**: Set the height
        - **use_container_width**: Overrides the width and sets it to the entire container width
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Group the number of stations by year
    stations_per_year = df.groupby('Year').size()

    # Display Streamlit chart
    st.line_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations", color="#6298c0")'''
    st.code(code, language="python")

def scatter_plot():
    st.subheader("*Distance from Tokyo Station*")
    st.scatter_chart(df, x="Station Name", y="Distance from Tokyo Station", x_label="Station Name", y_label="Distance from Tokyo Station (km)", size="Company", color="#c7daed")

    st.write("**Function Signature**")
    code = '''st.scatter_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, size=None, width=None, height=None, use_container_width=True)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **data**: Data being plotted (in my case, a pandas DataFrame)
        - **x**: Name of the x column
        - **y**: Name of the y column
        - **x_label**: Label for the x-axis
        - **y_label**: Label for the y-axis
        - **color**: Customize the color(s) used on the chart
        - **size**: Size of the circles
        - **width**: Set the width
        - **height**: Set the height
        - **use_container_width**: Overrides the width and sets it to the entire container width
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Display Streamlit chart
    st.scatter_chart(df, x="Station Name", y="Distance from Tokyo Station", x_label="Station Name", y_label="Distance from Tokyo Station (km)", size="Company", color="#c7daed")'''
    st.code(code, language="python")

def map():
    st.subheader("*Shinkansen Stations in Japan*")
    st.map(df, longitude="Longitude", latitude="Latitude", color="#87bbe2")

    st.write("**Function Signature**")
    code = '''st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **data**: Data being plotted (in my case, a pandas DataFrame)
        - **longitude**: Name of the longitude column
        - **latitude**: Name of the latitude column
        - **color**: Customize the color(s) used on the chart
        - **size**: Size of the circles
        - **zoom**: Choose zoom level
        - **use_container_width**: Sets width to the entire container width
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Display Streamlit map
    st.map(df, longitude="Longitude", latitude="Latitude", color="#87bbe2")'''
    st.code(code, language="python")
    
def matplotlib_fig():
    custom_colors = ['#c18489', '#e3a8b3', '#87bbe2', '#c7daed', '#6298c0']
    shinkansen_lines = df['Shinkansen_Line'].unique()
    color_map = {line: custom_colors[i % len(custom_colors)] for i, line in enumerate(shinkansen_lines)}


    # Create a scatter plot
    plt.figure(figsize=(6, 4))
    for line in shinkansen_lines:
        subset = df[df['Shinkansen_Line'] == line]
        plt.scatter(
            subset['Longitude'], subset['Latitude'], 
            alpha=0.7, label=line, 
            edgecolors='w', s=30, 
            c=color_map[line]
        )

    plt.title('Shinkansen Stations in Japan')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt)

    st.write("**Function Signature**")
    code = '''st.pyplot(fig=None, clear_figure=None, use_container_width=True, **kwargs)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **fig**: Object to display
        - **clear_figure**: Customize the color(s) used on the chart
        - **use_container_width**: Sets width to the entire container width
        - **kwargs**: Arguements to pass to the savefig function
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
        # Customize the colors
        custom_colors = ['#c18489', '#e3a8b3', '#87bbe2', '#c7daed', '#6298c0']
        shinkansen_lines = df['Shinkansen_Line'].unique()
        color_map = {line: custom_colors[i % len(custom_colors)] for i, line in enumerate(shinkansen_lines)}
    
    
        # Create a scatter plot
        plt.figure(figsize=(6, 4))
        for line in shinkansen_lines:
            subset = df[df['Shinkansen_Line'] == line]
            plt.scatter(
                subset['Longitude'], subset['Latitude'], 
                alpha=0.7, label=line, 
                edgecolors='w', s=30, 
                c=color_map[line]
            )
    
        plt.title('Shinkansen Stations in Japan')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
    
        # Display the plot in Streamlit
        st.pyplot(plt)'''
    st.code(code, language="python")

    st.write('''To learn more, visit the documentation: https://matplotlib.org/stable/index.html''')

def altair_fig():
    company_counts = df['Company'].value_counts().reset_index()
    company_counts.columns = ['Company', 'Number of Stations']

    # Customize the colors
    custom_colors = ['#c18489', '#e3a8b3', '#87bbe2', '#c7daed', '#6298c0']
    company_list = company_counts['Company'].unique()
    color_map = {company: custom_colors[i % len(custom_colors)] for i, company in enumerate(company_list)}
    
    # Convert the color map to a scale for Altair
    color_scale = alt.Scale(domain=list(color_map.keys()), range=list(color_map.values()))
    
    # Create a bar chart using Altair
    chart = alt.Chart(company_counts).mark_bar().encode(
        x=alt.X('Company:N', sort='-y', title='Company'),
        y=alt.Y('Number of Stations:Q', title='Number of Stations'),
        color=alt.Color('Company:N', scale=color_scale),
        tooltip=['Company:N', 'Number of Stations:Q']
    ).properties(
        title='Number of Shinkansen Stations by Company',
        width=600,
        height=400
    )

    # Display the chart in Streamlit
    st.altair_chart(chart)

    st.write("**Function Signature**")
    code = '''st.altair_chart(altair_chart, *, use_container_width=False, theme="streamlit", key=None, on_select="ignore", selection_mode=None)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **altair_chart**: Object to display
        - **use_container_width**: Sets width to the entire container width
        - **theme**: Choose the theme of the chart
        - **key**: Gives the chart a unique identity
        - **on_select**: Determines how the chart behaves with user interaction
        - **selection_mode**: Determine selection parameters
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Get number of stations per company
    company_counts = df['Company'].value_counts().reset_index()
    company_counts.columns = ['Company', 'Number of Stations']

    # Customize the colors
    custom_colors = ['#c18489', '#e3a8b3', '#87bbe2', '#c7daed', '#6298c0']
    company_list = company_counts['Company'].unique()
    color_map = {company: custom_colors[i % len(custom_colors)] for i, company in enumerate(company_list)}
    
    # Convert the color map to a scale
    color_scale = alt.Scale(domain=list(color_map.keys()), range=list(color_map.values()))
    
    # Create a bar chart using Altair
    chart = alt.Chart(company_counts).mark_bar().encode(
        x=alt.X('Company:N', sort='-y', title='Company'),
        y=alt.Y('Number of Stations:Q', title='Number of Stations'),
        color=alt.Color('Company:N', scale=color_scale),
        tooltip=['Company:N', 'Number of Stations:Q']
    ).properties(
        title='Number of Shinkansen Stations by Company',
        width=600,
        height=400
    )

    # Display the chart in Streamlit
    st.altair_chart(chart)'''
    st.code(code, language="python")

    st.write('''To learn more, visit the documentation: https://altair-viz.github.io''')

def vega_fig():
    avg_distance_per_year = df.groupby('Year')['Distance from Tokyo Station'].mean().reset_index()
    avg_distance_per_year.columns = ['Year', 'Average Distance']

    # Create a line chart using Vega-Lite
    chart = {
        "data": {
            "values": avg_distance_per_year.to_dict(orient="records")
        },
        "mark": {
            "type":"line",
            "color": "#c18489"
        },
        "encoding": {
            "x": {"field": "Year", "type": "temporal", "title": "Year"},
            "y": {"field": "Average Distance", "type": "quantitative", "title": "Average Distance (km)"},
            "tooltip": [{"field": "Year", "type": "temporal"}, {"field": "Average Distance", "type": "quantitative"}]
        },
        "title": "Average Distance from Tokyo Station by Year"
    }

    # Display the chart in Streamlit
    st.vega_lite_chart(chart, use_container_width=True)

    st.write("**Function Signature**")
    code = '''st.vega_lite_chart(data=None, spec=None, *, use_container_width=False, theme="streamlit", key=None, on_select="ignore", selection_mode=None, **kwargs)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **data**: Data being plotted
        - **spec**: Vega-Lite spec for the chart
        - **use_container_width**: Sets width to the entire container width
        - **theme**: Choose the theme of the chart
        - **key**: Gives the chart a unique identity
        - **on_select**: Determines how the chart behaves with user interaction
        - **selection_mode**: Determine selection parameters
        - **kwargs**: Arguements to pass to the savefig function
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Get average distance from Tokyo Station per year
    avg_distance_per_year = df.groupby('Year')['Distance from Tokyo Station'].mean().reset_index()
    avg_distance_per_year.columns = ['Year', 'Average Distance']

    # Create a line chart using Vega-Lite
    chart = {
        "data": {
            "values": avg_distance_per_year.to_dict(orient="records")
        },
        "mark": {
            "type":"line",
            "color": "#c18489"
        },
        "encoding": {
            "x": {"field": "Year", "type": "temporal", "title": "Year"},
            "y": {"field": "Average Distance", "type": "quantitative", "title": "Average Distance (km)"},
            "tooltip": [{"field": "Year", "type": "temporal"}, {"field": "Average Distance", "type": "quantitative"}]
        },
        "title": "Average Distance from Tokyo Station by Year"
    }

    # Display the chart in Streamlit
    st.vega_lite_chart(chart, use_container_width=True)'''
    st.code(code, language="python")

    st.write('''To learn more, visit the documentation: https://vega.github.io/vega-lite/docs/''')

def plotly_fig():
    # Customize the colors
    custom_colors = ['#c18489', '#e3a8b3', '#87bbe2', '#c7daed', '#6298c0']

    prefecture_counts = df['Prefecture'].value_counts().reset_index()
    prefecture_counts.columns = ['Prefecture', 'Number of Stations']

    
    # Map each prefecture to a custom color
    prefecture_list = prefecture_counts['Prefecture'].unique()
    color_map = {prefecture: custom_colors[i % len(custom_colors)] for i, prefecture in enumerate(prefecture_list)}
    
    # Create a bar chart using Plotly
    fig = px.bar(
        prefecture_counts,
        x='Prefecture',
        y='Number of Stations',
        color='Prefecture',
        title='Number of Shinkansen Stations by Prefecture',
        labels={'Prefecture': 'Prefecture', 'Number of Stations': 'Number of Stations'},
        height=600,
        color_discrete_map=color_map  # Apply the custom colors
    )

    # Customize the layout for better readability
    fig.update_layout(
        xaxis_title='Prefecture',
        yaxis_title='Number of Stations',
        xaxis={'categoryorder':'total descending'}
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.write("**Function Signature**")
    code = '''st.plotly_chart(figure_or_data, use_container_width=False, *, theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), **kwargs)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **figure_or_data**: Object or data being plotted
        - **use_container_width**: Sets width to the entire container width
        - **theme**: Choose the theme of the chart
        - **key**: Gives the chart a unique identity
        - **on_select**: Determines how the chart behaves with user interaction
        - **selection_mode**: Determine selection mode
        - **kwargs**: Arguements to pass to the savefig function
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
    # Customize the colors
    custom_colors = ['#c18489', '#e3a8b3', '#87bbe2', '#c7daed', '#6298c0']

    # Get number of stations per prefecture
    prefecture_counts = df['Prefecture'].value_counts().reset_index()
    prefecture_counts.columns = ['Prefecture', 'Number of Stations']

    
    # Map each prefecture to a olor
    prefecture_list = prefecture_counts['Prefecture'].unique()
    color_map = {prefecture: custom_colors[i % len(custom_colors)] for i, prefecture in enumerate(prefecture_list)}
    
    # Create a bar chart using Plotly
    fig = px.bar(
        prefecture_counts,
        x='Prefecture',
        y='Number of Stations',
        color='Prefecture',
        title='Number of Shinkansen Stations by Prefecture',
        labels={'Prefecture': 'Prefecture', 'Number of Stations': 'Number of Stations'},
        height=600,
        color_discrete_map=color_map  # Apply the custom colors
    )

    # Customize the layout
    fig.update_layout(
        xaxis_title='Prefecture',
        yaxis_title='Number of Stations',
        xaxis={'categoryorder':'total descending'}
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)'''
    st.code(code, language="python")

    st.write('''To learn more, visit the documentation: https://plotly.com/python/''')

def bokeh_fig():
    st.write("Working on it...")

def pydeck_fig():
    layer = pdk.Layer(
        'ColumnLayer',
        data=df,
        get_position='[Longitude, Latitude]',
        get_elevation=1000,  # Fixed elevation for all stations, can be modified to use a data field
        elevation_scale=50,
        radius=10000,  # Adjust the radius of the columns
        get_fill_color='[98, 152, 192, 255]',   # RGBA color format
        pickable=True,  # Enable picking for interactivity
        auto_highlight=True
    )

    # Set the view of the map
    view_state = pdk.ViewState(
        latitude=df['Latitude'].mean(),
        longitude=df['Longitude'].mean(),
        zoom=5,
        pitch=50,  # Tilt the map for a 3D effect
    )

    # Create the pydeck chart
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Station: {Station Name}\nPrefecture: {Prefecture}\nLine: {Shinkansen_Line}"}
    )

    st.subheader("**3D Map of Shinkansen Stations in Japan**")
    st.pydeck_chart(r)
    
    st.write("**Function Signature**")
    code = '''st.pyplot(fig=None, clear_figure=None, use_container_width=True, **kwargs)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **fig**: Object being plotted
        - **clear_figure**: Choose whether or not figure is cleared after being rendered
        - **use_container_width**: Sets width to the entire container width
        - **kwargs**: Arguements to pass to the savefig function
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = '''
        layer = pdk.Layer(
        'ColumnLayer',
        data=df,
        get_position='[Longitude, Latitude]',
        get_elevation=1000,  
        elevation_scale=50,
        radius=10000,  
        get_fill_color='[98, 152, 192, 255]',  
        pickable=True,  
        auto_highlight=True
    )

    # Set the view of the map
    view_state = pdk.ViewState(
        latitude=df['Latitude'].mean(),
        longitude=df['Longitude'].mean(),
        zoom=5,
        pitch=50, 
    )

    # Create the pydeck chart
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Station: {Station Name}\nPrefecture: {Prefecture}\nLine: {Shinkansen_Line}"}
    )

    # Display chart title
    st.subheader("**3D Map of Shinkansen Stations in Japan**")

    # Display the chart in Streamlit
    st.pydeck_chart(r)'''
    st.code(code, language="python")

    st.write('''To learn more, visit the documentation: https://deckgl.readthedocs.io/en/latest/''')

def graphviz_fig():
    graph = '''
    digraph G {
        rankdir=LR;
        
        Tokaido_Shinkansen [label="Tokaido Shinkansen", shape=box, style=filled, color="#c18489"];
        Sanyo_Shinkansen [label="Sanyo Shinkansen", shape=box, style=filled, color="#87bbe2"];
        Tohoku_Shinkansen [label="Tohoku Shinkansen", shape=box, style=filled, color="#6298c0"];
        
        Tokyo [label="Tokyo Station", shape=ellipse];
        Shin_Yokohama [label="Shin-Yokohama Station", shape=ellipse];
        Kyoto [label="Kyoto Station", shape=ellipse];
        Osaka [label="Osaka Station", shape=ellipse];
        Sendai [label="Sendai Station", shape=ellipse];
        
        Tokaido_Shinkansen -> Tokyo;
        Tokaido_Shinkansen -> Shin_Yokohama;
        Tokaido_Shinkansen -> Kyoto;
        Sanyo_Shinkansen -> Kyoto;
        Sanyo_Shinkansen -> Osaka;
        Tohoku_Shinkansen -> Tokyo;
        Tohoku_Shinkansen -> Sendai;
    }
    '''

    # Display the graph using st.graphviz_chart
    st.graphviz_chart(graph)

    st.write("**Function Signature**")
    code = '''st.graphviz_chart(figure_or_dot, use_container_width=False)'''
    st.code(code, language="python")

    st.markdown(
        """
        **Parameters**:
        - **figure_or_dot**: Object or dot string being plotted
        - **use_container_width**: Sets width to the entire container width
        """
    )
    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
    ''', unsafe_allow_html=True)

    st.write("**My Code**")
    code = """
     graph = '''
    digraph G {
        rankdir=LR;
        
        Tokaido_Shinkansen [label="Tokaido Shinkansen", shape=box, style=filled, color="#c18489"];
        Sanyo_Shinkansen [label="Sanyo Shinkansen", shape=box, style=filled, color="#87bbe2"];
        Tohoku_Shinkansen [label="Tohoku Shinkansen", shape=box, style=filled, color="#6298c0"];
        
        Tokyo [label="Tokyo Station", shape=ellipse];
        Shin_Yokohama [label="Shin-Yokohama Station", shape=ellipse];
        Kyoto [label="Kyoto Station", shape=ellipse];
        Osaka [label="Osaka Station", shape=ellipse];
        Sendai [label="Sendai Station", shape=ellipse];
        
        Tokaido_Shinkansen -> Tokyo;
        Tokaido_Shinkansen -> Shin_Yokohama;
        Tokaido_Shinkansen -> Kyoto;
        Sanyo_Shinkansen -> Kyoto;
        Sanyo_Shinkansen -> Osaka;
        Tohoku_Shinkansen -> Tokyo;
        Tohoku_Shinkansen -> Sendai;
    }
    '''

    # Display the graph in Streamlit
    st.graphviz_chart(graph)"""
    st.code(code, language="python")

    st.write('''To learn more, visit the documentation: https://graphviz.org/documentation/''')

styles = {
    "nav": {
        "background-color": "rgb(227, 168, 179)",
    }
}

page = st_navbar(["Demo Dashboard", "Simple Charts", "Advanced Charts", "Other"], styles=styles)

if page == "Simple Charts":
    st.header('Streamlit Data Viz Guide')
    choice = st.selectbox('Choose a chart type', options=['Area Chart', 'Bar Chart', 'Line Chart', 'Scatter Plot', 'Map'], index=None, key=1)
    st.write('###')

    if choice == "Area Chart":
        area_chart()
    elif choice == "Bar Chart":
        bar_chart()
    elif choice == "Line Chart":
        line_chart()
    elif choice == "Scatter Plot":
        scatter_plot()
    elif choice == "Map":
        map()
    else:
        st.subheader("Pros and Cons of Simple Charts")
        st.write('''*"Simple charts" are data visualization tools native to Streamlit.*''')
        st.markdown(
            """
            **Pros**:
            - **Simplicity**: Streamlit's native charts are straightforward to use with minimal code. They are ideal for quickly adding visualizations to your app.
            - **Easy Integration**: These charts are fully integrated with Streamlit, meaning they handle reactivity (e.g., updates when data changes) and layout automatically.
            - **Performance**: Native charts are optimized for performance within Streamlit, ensuring quick rendering and smooth user experience.
            - **Low Learning Curve**: For users who are new to data visualization or want to get something on the screen quickly, native Streamlit charts are very accessible.
            """
        )
        st.markdown(
            """
            **Cons**:
            - **Limited Customization**: Native charts lack the advanced customization options available in more powerful libraries. If you need complex formatting or highly specific visual elements, they might not be sufficient.
            - **Fewer Choices**: The range of chart types and options is more limited compared to external libraries like Plotly or Matplotlib.
            - **Basic Interactivity**: While Streamlit charts support basic interactivity, they don’t offer the advanced interactive features available in other libraries.
            """
        )
        st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:40px;
            }
            </style>
        ''', unsafe_allow_html=True)

        st.subheader("My Data")
        st.write("My dataset is a Japanese bullet train (shinkansen) dataset from Kaggle and I used pandas to import/manipulate it.")
        st.code('''df = pd.read_excel("shinkansen.xlsx")''', language="python")

elif page == "Advanced Charts":
    st.header('Streamlit Data Viz Guide')
    choice = st.selectbox('Choose a chart type', options=['Matplotlib', 'Altair', 'Vega Lite', 'Plotly', 'Bokeh', 'Pydeck', 'Graphviz'], index=None, key=2)
    st.write('###')

    if choice == "Matplotlib":
        matplotlib_fig()
    elif choice == 'Altair':
        altair_fig()
    elif choice == 'Vega Lite':
        vega_fig()
    elif choice == 'Plotly':
        plotly_fig()
    elif choice == 'Bokeh':
        bokeh_fig()
    elif choice == 'Pydeck':
        pydeck_fig()
    elif choice == "Graphviz":
        graphviz_fig()
    else:
        st.subheader("Pros and Cons of Advanced Charts")
        st.write('''*"Advanced charts" are data visualization tools from other Python packages/libraries such as Matplotlib or Plotly.*''')
        st.markdown(
            """
            **Pros**:
            - **Many Customization Options**: These libraries offer extensive customization options for every aspect of your charts, including styling, labeling, and layout.
            - **Wide Variety of Chart Types**: Libraries like Plotly and Matplotlib provide a broad range of chart types, from basic to highly specialized visualizations.
            - **Advanced Interactivity**: Some tools offer robust interactive features like hover effects, zooming, and clicking, making them ideal for complex, interactive dashboards.
            - **Publication-Ready Quality**: These tools can produce publication-quality figures, which is important for professional presentations or reports.
            - **Community Support and Extensions**: Being widely used in the data science community, these libraries have extensive documentation, community support, and numerous plugins/extensions.
            """
        )
        st.markdown(
            """
            **Cons**:
            - **Steeper Learning Curve**: These tools require more effort to learn and use effectively, especially for complex customizations.
            - **Additional Dependencies**: Using these libraries requires installing additional packages, which might add to your app's dependencies.
            - **Potential Performance Overhead**: Advanced libraries, particularly with complex or interactive charts, can introduce performance overhead, which might slow down your app, especially with large datasets.
            - **Integration Complexity**: You might need to handle some integration aspects manually, such as ensuring reactivity or properly managing layout within your Streamlit app.
            """
        )
        st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:40px;
            }
            </style>
        ''', unsafe_allow_html=True)

        st.subheader("My Data")
        st.write("My dataset is a Japanese bullet train (shinkansen) dataset from Kaggle and I used pandas to import/manipulate it.")
        st.code('''df = pd.read_excel("shinkansen.xlsx")''', language="python")

elif page == "Other":
    st.subheader("Honorable Mentions")
    st.write("*A brief overview of other Streamlit widgets that can be utilized for data visualization*")
    col1, col2 = st.columns(2)

    with col1.expander("**Text Widgets**", expanded=True):
        st.title("This is a title.")
        st.code('''st.title("This is a title.")''', language="Python")

        st.header("This is a header.")
        st.code('''st.header("This is a header.")''', language="Python")

        st.subheader("This is a subheader.")
        st.code('''st.subheader("This is a subheader.")''', language="Python")


else:
    st.header("**Shinkansen in Japan 🚅**")
    st.markdown("---")

    col1, col2, col3 = st.columns([1.5, 4.5, 2], gap='medium')

    selected_year = col1.slider("Filter by Year", min_value=df['Year'].dt.year.min(), max_value=df['Year'].dt.year.max(), value=(df['Year'].dt.year.min(), df['Year'].dt.year.max()), step=10)

    df['Year'] = df['Year'].dt.year
    df = df[(df['Year'] >= selected_year[0]) & (df['Year'] <= selected_year[1])]



    most_recent_year = df['Year'].max()
    previous_year = '2016'
    
    stations_most_recent = df[df['Year'] == most_recent_year]['Station Name'].count()
    stations_previous = df[df['Year'] == previous_year]['Station Name'].count()

    # Calculate the difference
    station_delta = stations_most_recent - stations_previous

    with col1:
        with st.container(border=True):
            st.metric("*Stations*", df['Station Name'].count(), delta=int(station_delta))
        with st.container(border=True):
            st.metric("*Train Lines*", df['Shinkansen_Line'].nunique())
        with st.container(border=True):
            st.metric("*Companies*", df['Company'].nunique())

        # Create the pie chart
        color_scale = alt.Scale(domain=['JR Central', 'JR East', 'JR West', 'JR Kyushu', 'JR Hokkaido'], 
                            range=['#c18489', '#e3a8b3', '#87bbe2', '#c7daed', '#6298c0'])
        pie_data = df.groupby(['Company']).size().reset_index(name='# of Stations')
        pie_chart = alt.Chart(pie_data).mark_arc().encode(
            theta=alt.Theta('# of Stations:Q', stack=True),
            color=alt.Color('Company:N', scale=color_scale, legend=None),
            tooltip=['Company:N', '# of Stations:Q']
        ).properties(
            width=150,  # Set width
            height=150
        )

        st.write('*Stations Per Company*')
        st.altair_chart(pie_chart)

    layer = pdk.Layer(
        'ColumnLayer',
        data=df,
        get_position='[Longitude, Latitude]',
        get_elevation=1000,  # Fixed elevation for all stations, can be modified to use a data field
        elevation_scale=50,
        radius=10000,  # Adjust the radius of the columns
        get_fill_color='[98, 152, 192, 255]',  # RGBA color format
        pickable=True,  # Enable picking for interactivity
        auto_highlight=True
    )

    # Set the view of the map
    view_state = pdk.ViewState(
        latitude=df['Latitude'].mean(),
        longitude=df['Longitude'].mean(),
        zoom=5,
        pitch=50,  # Tilt the map for a 3D effect
    )

    # Create the pydeck chart
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style='mapbox://styles/mapbox/light-v10',
        tooltip={"text": "Station: {Station Name}\nPrefecture: {Prefecture}\nLine: {Shinkansen_Line}"}
    )

    #col2.subheader("**3D Map of Shinkansen Stations in Japan**")
    col2.pydeck_chart(r)

    heatmap_data = df.groupby(['Prefecture']).size().reset_index(name='station_count')
    prefecture_totals = heatmap_data.groupby('Prefecture')['station_count'].sum().reset_index()

    top_5_prefectures = prefecture_totals.sort_values(by='station_count', ascending=False).head(5)['Prefecture']

    # Filter the original heatmap data to include only the top 5 prefectures
    heatmap_data = heatmap_data[heatmap_data['Prefecture'].isin(top_5_prefectures)]
    heatmap_data = heatmap_data.sort_values(by=['station_count'], ascending=False)
    heatmap_data = heatmap_data.rename(columns={"station_count":"# of Stations"})

    col3.subheader('*Top Prefectures*')
    col3.dataframe(heatmap_data, hide_index=True, use_container_width=True)

    col3.subheader("*Stations Per Year*")
    stations_per_year = df.groupby('Year').size()
    col3.line_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations", color="#6298c0")

    col2.image('train2.png', use_column_width=True)
