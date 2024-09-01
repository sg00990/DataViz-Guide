import streamlit as st
import pandas as pd
from streamlit_navigation_bar import st_navbar
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
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
    stations_per_year = df.groupby('Year').size()
    st.area_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations")'''
    st.code(code, language="python")

def bar_chart():
    st.subheader("*Number of Stations Per Prefecture*")
    stations_per_prefecture = df['Prefecture'].value_counts()
    st.bar_chart(stations_per_prefecture, x_label="Prefecture", y_label="Number of Stations")

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
    stations_per_prefecture = df['Prefecture'].value_counts()
    st.bar_chart(stations_per_prefecture, x_label="Prefecture", y_label="Number of Stations")'''
    st.code(code, language="python")

def line_chart():
    st.subheader("*Stations Opened Per Year*")
    stations_per_year = df.groupby('Year').size()
    st.line_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations")

    code = '''st.line_chart(stations_per_year, x_label="Year Opened", y_label="Number of Stations")'''
    st.code(code, language="python")

def scatter_plot():
    st.subheader("*Distance from Tokyo Station*")
    st.scatter_chart(df, x="Station Name", y="Distance from Tokyo Station", x_label="Station Name", y_label="Distance from Tokyo Station (km)")

    code = '''st.scatter_chart(df, x="Station Name", y="Distance from Tokyo Station")'''
    st.code(code, language="python")

def map():
    st.subheader("*Shinkansen Stations in Japan*")
    st.map(df, longitude="Longitude", latitude="Latitude")

    code = '''st.map(df, longitude="Longitude", latitude="Latitude")'''
    st.code(code, language="python")

def matplotlib_fig():
    shinkansen_lines = df['Shinkansen_Line'].unique()
    colors = plt.get_cmap('tab10', len(shinkansen_lines))

    # Create a scatter plot
    plt.figure(figsize=(6, 4))
    for line in shinkansen_lines:
        subset = df[df['Shinkansen_Line'] == line]
        plt.scatter(
            subset['Longitude'], subset['Latitude'], 
            alpha=0.7, label=line, 
            edgecolors='w', s=30, 
            c=[colors(list(shinkansen_lines).index(line))]
        )

    plt.title('Shinkansen Stations in Japan')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt)

    code = '''st.pyplot(fig)'''
    st.code(code, language="python")

def altair_fig():
    company_counts = df['Company'].value_counts().reset_index()
    company_counts.columns = ['Company', 'Number of Stations']

    # Create a bar chart using Altair
    chart = alt.Chart(company_counts).mark_bar().encode(
        x=alt.X('Company:N', sort='-y', title='Company'),
        y=alt.Y('Number of Stations:Q', title='Number of Stations'),
        color='Company:N',
        tooltip=['Company:N', 'Number of Stations:Q']
    ).properties(
        title='Number of Shinkansen Stations by Company',
        width=600,
        height=400
    )

    st.altair_chart(chart)

    code = '''st.altair_chart(chart)'''
    st.code(code, language="python")

def vega_fig():
    avg_distance_per_year = df.groupby('Year')['Distance from Tokyo Station'].mean().reset_index()
    avg_distance_per_year.columns = ['Year', 'Average Distance']

    # Create a line chart using Vega-Lite
    chart = {
        "data": {
            "values": avg_distance_per_year.to_dict(orient="records")
        },
        "mark": "line",
        "encoding": {
            "x": {"field": "Year", "type": "temporal", "title": "Year"},
            "y": {"field": "Average Distance", "type": "quantitative", "title": "Average Distance (km)"},
            "tooltip": [{"field": "Year", "type": "temporal"}, {"field": "Average Distance", "type": "quantitative"}]
        },
        "title": "Average Distance from Tokyo Station by Year"
    }

    # Display the chart in Streamlit
    st.vega_lite_chart(chart, use_container_width=True)

    code = '''st.vega_lite_chart(chart)'''
    st.code(code, language="python")

def plotly_fig():
    prefecture_counts = df['Prefecture'].value_counts().reset_index()
    prefecture_counts.columns = ['Prefecture', 'Number of Stations']

    # Create a bar chart using Plotly
    fig = px.bar(
        prefecture_counts,
        x='Prefecture',
        y='Number of Stations',
        color='Prefecture',
        title='Number of Shinkansen Stations by Prefecture',
        labels={'Prefecture': 'Prefecture', 'Number of Stations': 'Number of Stations'},
        height=600
    )

    # Customize the layout for better readability
    fig.update_layout(
        xaxis_title='Prefecture',
        yaxis_title='Number of Stations',
        xaxis={'categoryorder':'total descending'}
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    code = '''st.plotly_chart(fig)'''
    st.code(code, language="python")

def bokeh_fig():
    year_counts = df['Year'].value_counts().reset_index()
    year_counts.columns = ['Year', 'Number of Stations']
    year_counts = year_counts.sort_values(by='Year')

    # Convert the data to a Bokeh ColumnDataSource
    source = ColumnDataSource(year_counts)

    # Create a Bokeh figure
    p = figure(
        title='Number of Shinkansen Stations Established by Year',
        x_axis_label='Year',
        y_axis_label='Number of Stations',
        width=800,
        height=400
    )

    # Add a line and circle glyph
    p.line(x='Year', y='Number of Stations', source=source, line_width=2, color='blue', legend_label='Stations')
    p.circle(x='Year', y='Number of Stations', source=source, size=8, color='red', legend_label='Stations')

    # Add hover tool for more interactivity
    hover = HoverTool()
    hover.tooltips = [
        ("Year", "@Year"),
        ("Number of Stations", "@{Number of Stations}")
    ]
    p.add_tools(hover)

    # Customize the chart
    p.legend.location = "top_left"
    p.title.text_font_size = "16pt"
    p.xaxis.axis_label_text_font_size = "12pt"
    p.yaxis.axis_label_text_font_size = "12pt"

    # Display the chart in Streamlit
    st.bokeh_chart(p, use_container_width=True)

    code = '''st.bokeh_chart(fig)'''
    st.code(code, language="python")

def pydeck_fig():
    layer = pdk.Layer(
        'ColumnLayer',
        data=df,
        get_position='[Longitude, Latitude]',
        get_elevation=1000,  # Fixed elevation for all stations, can be modified to use a data field
        elevation_scale=50,
        radius=10000,  # Adjust the radius of the columns
        get_fill_color='[200, 30, 0, 160]',  # RGBA color format
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

    code = '''st.pydeck_chart(r)'''
    st.code(code, language="python")

def graphviz_fig():
    graph = '''
    digraph G {
        rankdir=LR;
        
        Tokaido_Shinkansen [label="Tokaido Shinkansen", shape=box, style=filled, color=lightblue];
        Sanyo_Shinkansen [label="Sanyo Shinkansen", shape=box, style=filled, color="#90EE90"];
        Tohoku_Shinkansen [label="Tohoku Shinkansen", shape=box, style=filled, color=lightcoral];
        
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

    code = '''st.graphviz_chart(graph)'''
    st.code(code, language="python")

styles = {
    "nav": {
        "background-color": "rgb(227, 168, 179)",
    }
}

page = st_navbar(["Demo Dashboard", "Simple Charts", "Advanced Charts"], styles=styles)

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
        st.write('''*"Simple charts" are just data visualization tools native to Streamlit.*''')
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
        st.write('''*"Advanced charts" are just data visualization tools from other Python packages/libraries such as Matplotlib or Plotly.*''')
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

else:
    st.header("**Shinkansen in Japan 🚅**")
    st.write('######')

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
