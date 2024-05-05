"""
Name:    Anna Szenas
CS230:   CS230-5
Data:    Rest Areas In California
URL:

Description:

This program creates a Streamlit Webpage about the Rest Areas in California. This webpage allows users to explore the
distribution of the Rest areas across geographic units such as districts, counties and routes. On this page users can
also check the percentage of rest areas with their chosen facilities and examine them on maps. Additionally, this
webpage allows users to look for rest areas near their chosen cities.
"""

#importing packages:----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import pydeck as pdk

#loading the dataframe--------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#my path:
path = "C:/Users/Felhasználó/Desktop/Annaa/corvinus/6. semester bentley/intro to python/codes/pythonProject/final_project2/"

st.set_option('deprecation.showPyplotGlobalUse', False)

#reading the dataframe:
rest_areas = pd.read_csv(path + "Rest_Areas.csv")

#[DA1]:
rest_areas.dropna(inplace=True)
rest_areas.rename(columns={"LATITUDE":"lat", "LONGITUDE": "lon"}, inplace= True)

#SIDEBAR:---------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#sidebar title:
#[ST4]:
st.sidebar.title("Pages")

#create page name list:
page_names = ["Home Page",
              "Distribution by Geographic Units",
              "Rest Area Facilities",
              "Rest Areas Near Cities",
              "Map and Location Guide"]

#create radiobuttons for pages:
#[ST2]:
selected_page = st.sidebar.radio("Select a page:", page_names)

#PAGE1:-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

if selected_page == "Home Page":
    #add title:
    st.title("Exploring Rest Areas in California")

    #add description:
    '''
    Rest areas are vital for travelers, offering a safe place to rest, stretch, and recharge during long journeys. 
    The following pages provide valuable insights into these crucial facilities, helping travelers make informed 
    decisions about their stops across the state of California.
    '''

    #add image:
    #[ST4]:
    from PIL import Image
    rest_img = Image.open("C:/Users/Felhasználó/Desktop/Annaa/corvinus/6. semester bentley/intro to python/codes/pythonProject/final_project2/rest_area_image.jpg")
    st.image(rest_img,width=700)

#PAGE2:-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

elif selected_page == "Distribution by Geographic Units":
    #add page title:
    st.title("Exploring Rest Areas in California: Analyzing Rest Area Distribution by Geographic Units")

    #add description:
    '''
    Page Summary:
    '''
    '''
    This page allows you to visualize the distribution of rest areas in California across different geographic units. 
    Choose one or more options from routes, districts, or counties to see the number of rest areas represented on a 
    bar chart. By examining these charts, you can gain insights into the distribution of rest areas across specific 
    geographic units, helping you plan your travels in California more effectively and understand where rest areas are 
    concentrated.
    '''

    #add multiselect for the bar charts:
    #[ST1]:
    selection = ["Districts","Counties","Routes"]
    selected = st.multiselect("I want to see the number of Rest Areas by: ", selection)

    #if nothing is selected:
    if len(selected) == 0:
        st.write("You haven't made a selection yet")

    #Districts: bar1 - [VIZ1]
    if "Districts" in selected:
        #[DA7]:
        df_bar1D = rest_areas["DISTRICT"].value_counts()  #get a series
        #[DA2]:
        df_bar1D = df_bar1D.sort_values(ascending=False) #sort descending
        df_bar1D.plot(kind="bar", color="red") #plot the bar chart
        plt.title("Number of Rest Areas in each District") #chart title
        plt.ylabel("Number of Rest Areas") #y axis label
        plt.xlabel("Districts") #x axis label
        st.pyplot()

        #[DA3]:
        #getting the min max value
        min_areas_d = df_bar1D.min()
        max_areas_d = df_bar1D.max()

        #getting the districts with the max and min values:
        #[PY5]: Creating the dictionary - I will document accessing its values with "[PY5]-A"
        minmax_district_dict = {"min":[],
                                "max":[]}
        for index, count in df_bar1D.items():
            if count == min_areas_d:
                minmax_district_dict["min"].append(index)
            if count == max_areas_d:
                minmax_district_dict["max"].append(index)

        #displaying districts:
        #[PY4]: (+[PY5]-A)
        display_maxd = [str(i) for i in minmax_district_dict["max"]]
        display_maxd_str = ", ".join(display_maxd)
        st.write(f"The district(s) with the maximum amount of rest areas is/are: {display_maxd_str} - with the number of {max_areas_d} rest areas.")

        # [PY4]: (+[PY5]-A)
        display_mind = [str(i) for i in minmax_district_dict["min"]]
        display_mind_str = ", ".join(display_mind)
        st.write(f"The district(s) with the minimum amount of rest areas is/are: {display_mind_str} - with the number of {min_areas_d} rest areas.")

        #checkbox for the table
        #[ST3]:
        show_table1 = st.checkbox("Check if you want to see the table for the 'Number of rest areas in each District'")
        if show_table1:
            st.write(df_bar1D)

    #Counties: bar2 - [VIZ1]
    if "Counties" in selected:
        # [DA7]:
        df_bar1C = rest_areas["COUNTY"].value_counts() #get a series
        # [DA2]:
        df_bar1C = df_bar1C.sort_values(ascending=False) #sort descending
        df_bar1C.plot(kind="bar", color="red") #plot the bar chart
        plt.title("Number of Rest Areas in each County") #chart title
        plt.ylabel("Number of Rest Areas") #y axis label
        plt.xlabel("Counties") #x axis label
        st.pyplot()

        # [DA3]:
        #getting the min max value
        min_areas_c = df_bar1C.min()
        max_areas_c = df_bar1C.max()

        # getting the counties with the max and min values:
        # [PY5]: Creating the dictionary - I will document accessing its values with "[PY5]-A"
        minmax_counties_dict = {"min": [],
                                "max": []}
        for index, count in df_bar1C.items():
            if count == min_areas_c:
                minmax_counties_dict["min"].append(index)
            if count == max_areas_c:
                minmax_counties_dict["max"].append(index)

        # displaying dcounties:
        # [PY4]: (+[PY5]-A)
        display_maxc = [str(i) for i in minmax_counties_dict["max"]]
        display_maxc_str = ", ".join(display_maxc)
        st.write(f"The county/counties with the maximum amount of rest areas is/are: {display_maxc_str} - with the number of {max_areas_c} rest areas.")

        # [PY4]: (+[PY5]-A)
        display_minc = [str(i) for i in minmax_counties_dict["min"]]
        display_minc_str = ", ".join(display_minc)
        st.write(f"The county/counties with the minimum amount of rest areas is/are: {display_minc_str} - with the number of {min_areas_c} rest area.")

        # checkbox for the table
        # [ST3]:
        show_table2 = st.checkbox("Check if you want to see the table for the 'Number of rest areas in each County'")
        if show_table2:
            st.write(df_bar1C)

    #Routes: bar3 - [VIZ1]
    if "Routes" in selected:
        # [DA7]:
        df_bar1R = rest_areas["ROUTE"].value_counts() #get a series
        # [DA2]:
        df_bar1R = df_bar1R.sort_values(ascending = False) #sort descending
        df_bar1R.plot(kind = "bar", color = "red") #plot the bar chart
        plt.title("Number of Rest Areas along each Route") #chart title
        plt.ylabel("Number of Rest Areas") #y axis label
        plt.xlabel("Routes") #x axis label
        st.pyplot()

        # [DA3]:
        min_areas_r = df_bar1R.min()
        max_areas_r = df_bar1R.max()

        # getting the routes with the max and min values:
        # [PY5]: Creating the dictionary - I will document accessing its values with "[PY5]-A"
        minmax_routes_dict = {"min": [],
                              "max": []}
        for index, count in df_bar1R.items():
            if count == min_areas_r:
                minmax_routes_dict["min"].append(index)
            if count == max_areas_r:
                minmax_routes_dict["max"].append(index)

        # displaying routes:
        # [PY4]: (+[PY5]-A)
        display_maxr = [str(i) for i in minmax_routes_dict["max"]]
        display_maxr_str = ", ".join(display_maxr)
        st.write(f"The route(s) with the maximum amount of rest areas is/are: {display_maxr_str} - with the number of {max_areas_r} rest areas.")

        # [PY4]: (+[PY5]-A)
        display_minr = [str(i) for i in minmax_routes_dict["min"]]
        display_minr_str = ", ".join(display_minr)
        st.write(f"The route(s) with the minimum amount of rest areas is/are: {display_minr_str} - with the number of {min_areas_r} rest area.")

        # checkbox for the table
        # [ST3]:
        show_table3 = st.checkbox("Check if you want to see the table for the 'Number of Rest Areas along each Route'")
        if show_table3:
            st.write(df_bar1R)

#PAGE3:-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

elif selected_page == "Rest Area Facilities":

    #add page title:
    st.title("Exploring Rest Areas in California: Percentage of Rest Areas with Selected Facilities")

    #add description:
    '''
    Page Summary:
    '''
    '''
    On this page each tab displays a pie chart illustrating the percentage of rest areas with and without the chosen 
    facility. By examining these pie charts, you can evaluate the availability of various amenities at rest areas across 
    California. With this tool, you will also have a clearer understanding of what to expect when you stop at a rest area 
    during your journey.
    '''

    # USING TABS FOR DIFFERENT KIND OF PIECHARTS:
    #creating the tab names
    tab_names = ["Restrooms", "Water", "Picnic Tables", "Phone", "Vending Machines",
                 "Facilities for Handicapped Individuals", "Station for Recreational Vehicles",
                 "Area designated for Pets"]

    #creating tabs:
    # [ST3+]:
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(tab_names)

    #tab contents
    #tab1
    with tab1:
        # [VIZ2]
        st.title("Percentage of Rest Areas with Restrooms")  # title
        # [DA7]:
        pie_df1 = rest_areas["RESTROOM"].value_counts()  # get the series
        # [DA2]:
        pie_df1.sort_index(inplace=True)  # sort by index
        pielabels1 = ["With Restrooms"]  # label
        piecolors1 = ["green"]  # color
        pie_df1.plot(kind="pie", colors=piecolors1, autopct="%.1f%%", labels=pielabels1)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable1 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Restrooms'")
        if showtable1:
            st.write(pie_df1)

    #tab2
    with tab2:
        # [VIZ2]
        st.title("Percentage of Rest Areas with Water")  # title
        # [DA7]:
        pie_df2 = rest_areas["WATER"].value_counts()  # get the series
        # [DA2]:
        pie_df2.sort_index(inplace=True)  # sort by index
        pielabels2 = ["With Water"]  # label
        piecolors2 = ["green"]  # color
        pie_df2.plot(kind="pie", colors=piecolors2, autopct="%.1f%%", labels=pielabels2)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable2 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Water'")
        if showtable2:
            st.write(pie_df2)

    #tab3
    with tab3:
        # [VIZ2]
        st.title("Percentage of Rest Areas with Picnic Tables")  # title
        # [DA7]:
        pie_df3 = rest_areas["PICNICTAB"].value_counts()  # get the series
        # [DA2]:
        pie_df3.sort_index(inplace=True)  # sort by index
        pielabels3 = ["No Data", "With Picnic Tables"]  # label
        piecolors3 = ["blue", "green"]  # color
        pie_df3.plot(kind="pie", colors=piecolors3, autopct="%.1f%%", labels=pielabels3)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable3 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Picnic Tables'")
        if showtable3:
            st.write(pie_df3)

    #tab4
    with tab4:
        # [VIZ2]
        st.title("Percentage of Rest Areas with Phone")  # title
        # [DA7]:
        pie_df4 = rest_areas["PHONE"].value_counts()  # get the series
        # [DA2]:
        pie_df4.sort_index(inplace=True)  # sort by index
        pielabels4 = ["No Data", "Without Phone", "With Phone"]  # label
        piecolors4 = ["blue", "red", "green"]  # color
        pie_df4.plot(kind="pie", colors=piecolors4, autopct="%.1f%%", labels=pielabels4)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable4 = st.checkbox("Check if you want to see the table for 'Percentage of Rest Areas with Phone'")
        if showtable4:
            st.write(pie_df4)

    #tab5
    with tab5:
        # [VIZ2]
        st.title("Percentage of Rest Areas with Vending Machines")  # title
        # [DA7]:
        pie_df5 = rest_areas["VENDING"].value_counts()  # get the series
        # [DA2]:
        pie_df5.sort_index(inplace=True)  # sort by index
        pielabels5 = ["Without Vending Machines", "With Vending Machines"]  # label
        piecolors5 = ["red", "green"]  # color
        pie_df5.plot(kind="pie", colors=piecolors5, autopct="%.1f%%", labels=pielabels5)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable5 = st.checkbox(
            "Check if you want to see the table for 'Percentage of Rest Areas with Vending Machines'")
        if showtable5:
            st.write(pie_df5)

    #tab6
    with tab6:
        # [VIZ2]
        st.title("Percentage of Rest Areas with Facilities for Handicapped Individuals")  # title
        # [DA7]:
        pie_df6 = rest_areas["HANDICAP"].value_counts()  # get the series
        # [DA2]:
        pie_df6.sort_index(inplace=True)  # sort by index
        pielabels6 = ["With Facilities for Handicapped Individuals"]  # label
        piecolors6 = ["green"]  # color
        pie_df6.plot(kind="pie", colors=piecolors6, autopct="%.1f%%", labels=pielabels6)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable6 = st.checkbox(
            "Check if you want to see the table for 'Percentage of Rest Areas with Facilities for Handicapped Individuals'")
        if showtable6:
            st.write(pie_df6)

    #tab7
    with tab7:
        # [VIZ2]
        st.title("Percentage of Rest Areas with a Station for Recreational Vehicles")  # title
        # [DA7]:
        pie_df7 = rest_areas["RV_STATION"].value_counts()  # get the series
        # [DA2]:
        pie_df7.sort_index(inplace=True)  # sort by index
        pielabels7 = ["Without a Station for Recreational Vehicles",
                      "With a Station for Recreational Vehicles"]  # label
        piecolors7 = ["red", "green"]  # color
        pie_df7.plot(kind="pie", colors=piecolors7, autopct="%.1f%%", labels=pielabels7)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable7 = st.checkbox(
            "Check if you want to see the table for 'Percentage of Rest Areas with a Station for Recreational Vehicles'")
        if showtable7:
            st.write(pie_df7)

    #tab8
    with tab8:
        # [VIZ2]
        st.title("Percentage of Rest Areas with an Area designated for Pets")  # title
        # [DA7]:
        pie_df8 = rest_areas["PET_AREA"].value_counts()  # get the series
        # [DA2]:
        pie_df8.sort_index(inplace=True)  # sort by index
        pielabels8 = ["No Data", "With an Area designated for Pets"]  # label
        piecolors8 = ["blue", "green"]  # color
        pie_df8.plot(kind="pie", colors=piecolors8, autopct="%.1f%%", labels=pielabels8)  # piechart
        plt.ylabel(" ")  # removed the label "count" from the y axis
        st.pyplot()
        # checkbox for the table
        # [ST3]:
        showtable8 = st.checkbox(
            "Check if you want to see the table for 'Percentage of Rest Areas with an Area designated for Pets'")
        if showtable8:
            st.write(pie_df8)

#PAGE4:-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

elif selected_page == "Rest Areas Near Cities":
    # add page title:
    st.title("Exploring Rest Areas in California: Rest areas Near Cities")

    # add description:
    '''
    Page Summary:
    '''
    '''
    This page enables you to discover rest areas close to specific cities in California. Simply select a city from the
    drop-down menu, and the rest areas near your chosen city will be displayed.
    '''

    # creating empty citylist:
    citylist = []

    # [DA8]:
    #filling up empty citylist by iterating through the rows of the dataset
    for index, row in rest_areas.iterrows():
        city = row["CITY"]
        traffic_direction = row["TRAFFICDIR"]

        # if city is not in the list, then append
        if city not in citylist:
            citylist.append(city)

    # creating selection:
    citylist.append("A selection needs to be made:") #I added this to the list, to have a deafult value, where 0 selection has been made
    # [PY1]:
    citylist = sorted(citylist, reverse=False)
    del citylist[0]

    # [ST3+]:
    select_city = st.selectbox("Select a city:", citylist)

    # creating empty list for the matching areas
    matching_rest_areas = []

    # finding matching areas
    # [DA8]:
    for index, row in rest_areas.iterrows():
        city = row["CITY"]
        rest_area_name = row["NAME"]

        # check if the city and trafficdir matches the selected ones
        if city == select_city:
            matching_rest_areas.append(rest_area_name)

    # displaying matching areas
    if matching_rest_areas != []:
        st.write(f"Rest areas near the city {select_city}:")
        for area in matching_rest_areas:
            st.write(area)
    else: #display this line with the deaful value
        st.write("You haven't made a selection yet.")

#PAGE5:-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

elif selected_page == "Map and Location Guide":
    # add page title:
    st.title("Exploring Rest Areas in California: Map and Location Guide")

    # add description:
    '''
    Page Summary:
    '''
    '''
    This page allows you to discover rest areas across various amenities and locations. You can explore all rest areas, 
    displaying their locations on the map, or locate rest areas equipped with restroom, water or phone facilities. You 
    can discover rest areas with picnic tables for outdoor dining or with vending machines for snacks and drinks. You 
    can locate rest areas with facilities for handicapped individuals or rest areas with designated RV stations as well.
    In addition, you can find rest areas with areas for pets to rest and play.
    '''
    # creating radio buttons for the map:-------------------------------------------------------------------------------
    map_options = ["All Rest Areas",
                   "Rest Areas with Restrooms",
                   "Rest Areas with Water",
                   "Rest Areas with Picnic Tables",
                   "Rest Areas with Phone",
                   "Rest Areas with Vending Machines",
                   "Rest Areas with Facilities for Handicapped Individuals",
                   "Rest Areas with a Station for Recreational Vehicles",
                   "Rest Areas with an Area designated for Pets"]
    # [ST2]:
    choosen_map = st.radio("Select a Map from the list:", options=map_options)

    # creating new dataframes for the maps:-----------------------------------------------------------------------------
    # [DA4]:
    restroom_df = rest_areas[rest_areas["RESTROOM"].str.upper() == "YES"]
    # [DA4]:
    water_df = rest_areas[rest_areas["WATER"].str.upper() == "YES"]
    # [DA4]:
    picnic_df = rest_areas[rest_areas["PICNICTAB"].str.upper() == "YES"]
    # [DA4]:
    phone_df = rest_areas[rest_areas["PHONE"].str.upper() == "YES"]
    # [DA4]:
    vending_df = rest_areas[rest_areas["VENDING"].str.upper() == "YES"]
    # [DA4]:
    handicap_df = rest_areas[rest_areas["HANDICAP"].str.upper() == "YES"]
    # [DA4]:
    rv_df = rest_areas[rest_areas["RV_STATION"].str.upper() == "YES"]
    # [DA4]:
    pet_df = rest_areas[rest_areas["PET_AREA"].str.upper() == "YES"]

    # all areas map:----------------------------------------------------------------------------------------------------
    # [VIZ3] - scatterplot map
    # create the viewstate:
    all_view_state = pdk.ViewState(
        latitude=rest_areas["lat"].mean(),  # the latitude of the view center - CENTER
        longitude=rest_areas["lon"].mean(),  # the longitude of the view center - CENTER
        zoom=5,  # view zoom level
        pitch=0)  # tilt level

    # create layers:
    all_layer1 = pdk.Layer(type="ScatterplotLayer",  # layer type
                           data=rest_areas,  # data
                           get_position="[lon, lat]",  # coordinates
                           get_radius=10000,  # scatter radius - adjust size
                           get_color=[255, 0, 0],  # scatter color - color code for red
                           pickable=True  # work with tooltip
                           )

    all_layer2 = pdk.Layer(type="ScatterplotLayer",  # layer type
                           data=rest_areas,  # data
                           get_position="[lon, lat]",  # coordinates
                           get_radius=5000,  # scatter radius - adjust size
                           get_color=[255, 165, 0],  # scatter color - color code for orange
                           pickable=True  # work with tooltip
                           )

    # create tooltip:
    all_tool_tip = {"html": "Rest Area Name:<br/> <b>{NAME}</b>",
                    "style": {"backgroundColor": "black",
                              "color": "white"}
                    }

    # create map:
    all_map = pdk.Deck(
        map_style="mapbox://styles/mapbox/satellite-streets-v12",
        initial_view_state=all_view_state,  # viewstate
        layers=[all_layer1, all_layer2],  # layers
        tooltip=all_tool_tip  # tooltip
    )


    # icon maps:--------------------------------------------------------------------------------------------------------
    # i created a function which creates the iconmap
    # inputs are the urls of the icons and the dataframe of the map

    # [PY3]: a function, that I wrote and returns a value - I used it 8 times, I will document the usages with "[PY3]-U"
    def create_iconmap(icon_url, dataframe):
        # [VIZ4] - iconmap
        # first the function should format the icon
        icon_data = {
            "url": icon_url,
            "width": 100,
            "height": 100,
            "anchorY": 1  # how far away do i want to put your icon
        }

        # then the function adds the icons to the dataframe
        # [DA9]:
        dataframe["icon_data"] = None  # new column with first nothing
        for i in dataframe.index:
            dataframe["icon_data"][i] = icon_data

        # the function creates the layer with the custom icon
        icon_layer = pdk.Layer(type="IconLayer",
                               data=dataframe,
                               get_icon="icon_data",  # where we get this icon from
                               get_position="[lon,lat]",
                               get_size=13,
                               pickable=True)

        # then viewstate:
        icon_view_state = pdk.ViewState(
            latitude=dataframe["lat"].mean(),
            longitude=dataframe["lon"].mean(),
            zoom=5,  # same zoom as the allmap
            pitch=0
        )

        # tooltip:
        icon_tool_tip = {"html": "Rest Area Name:<br/> <b>{NAME}</b>",
                         "style": {"backgroundColor": "black",
                                   "color": "white"}
                         }

        icon_map = pdk.Deck(
            map_style="mapbox://styles/mapbox/satellite-streets-v12",
            layers=[icon_layer],
            initial_view_state=icon_view_state,
            tooltip=icon_tool_tip
        )

        return icon_map


    # creating url list and dataframe list for the icons:---------------------------------------------------------------
    iconlist = ["https://upload.wikimedia.org/wikipedia/commons/8/8f/Toilets_unisex.svg",
                "https://upload.wikimedia.org/wikipedia/commons/c/cd/Waterbody.svg",
                "https://upload.wikimedia.org/wikipedia/commons/b/be/Picnic_Table_Icon.svg",
                "https://upload.wikimedia.org/wikipedia/commons/1/1f/Phoneicon.svg",
                "https://upload.wikimedia.org/wikipedia/commons/3/32/Noun44656_vending_machine.svg",
                "https://upload.wikimedia.org/wikipedia/commons/3/31/Wheelchair-green3.svg",
                "https://upload.wikimedia.org/wikipedia/commons/1/15/Rv-site.svg",
                "https://upload.wikimedia.org/wikipedia/commons/a/a1/Dog-1800633.svg"]

    df_list = [restroom_df, water_df, picnic_df, phone_df, vending_df, handicap_df, rv_df, pet_df]

    # showing the maps:-------------------------------------------------------------------------------------------------
    if choosen_map == "All Rest Areas":
        # show the all_map and title
        st.title("All Rest Areas:")
        st.pydeck_chart(all_map)

    elif choosen_map == "Rest Areas with Restrooms":
        # show title + map:
        st.title("Rest Areas with Restrooms:")
        # [PY3]-U:
        iconmap1 = create_iconmap(icon_url=iconlist[0], dataframe=df_list[0])
        st.pydeck_chart(iconmap1)

    elif choosen_map == "Rest Areas with Water":
        # show title + map:
        st.title("Rest Areas with Water:")
        # [PY3]-U:
        iconmap2 = create_iconmap(icon_url=iconlist[1], dataframe=df_list[1])
        st.pydeck_chart(iconmap2)

    elif choosen_map == "Rest Areas with Picnic Tables":
        st.title("Rest Areas with Picnic Tables:")
        # [PY3]-U:
        iconmap3 = create_iconmap(icon_url=iconlist[2], dataframe=df_list[2])
        st.pydeck_chart(iconmap3)

    elif choosen_map == "Rest Areas with Phone":
        st.title("Rest Areas with Phone:")
        # [PY3]-U:
        iconmap4 = create_iconmap(icon_url=iconlist[3], dataframe=df_list[3])
        st.pydeck_chart(iconmap4)

    elif choosen_map == "Rest Areas with Vending Machines":
        st.title("Rest Areas with Vending Machines:")
        # [PY3]-U:
        iconmap5 = create_iconmap(icon_url=iconlist[4], dataframe=df_list[4])
        st.pydeck_chart(iconmap5)

    elif choosen_map == "Rest Areas with Facilities for Handicapped Individuals":
        st.title("Rest Areas with Facilities for Handicapped Individuals:")
        # [PY3]-U:
        iconmap6 = create_iconmap(icon_url=iconlist[5], dataframe=df_list[5])
        st.pydeck_chart(iconmap6)

    elif choosen_map == "Rest Areas with a Station for Recreational Vehicles":
        st.title("Rest Areas with a Station for Recreational Vehicles:")
        # [PY3]-U:
        iconmap7 = create_iconmap(icon_url=iconlist[6], dataframe=df_list[6])
        st.pydeck_chart(iconmap7)

    elif choosen_map == "Rest Areas with an Area designated for Pets":
        st.title("Rest Areas with an Area designated for Pets:")
        # [PY3]-U:
        iconmap8 = create_iconmap(icon_url=iconlist[7], dataframe=df_list[7])
        st.pydeck_chart(iconmap8)


#SOURCES I USED:--------------------------------------------------------------------------------------------------------

#On PAGE2:
    #For the checkbox:
        #checkbox: https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox

    #For counting how many times something occours in a column:
        #https://saturncloud.io/blog/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas/
            #When I first tried to count all the rest areas in each district, I tried to do it with groupby and it did not work very well.
            #Then I found this ".value_counts()" method and by using this I was able to get a serie of the "counts", which I found very useful.

#On PAGE3:
    # For the checkbox:
        # checkbox: https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox

    #For the tabs:
        #tabs: https://docs.streamlit.io/develop/api-reference/layout/st.tabs

#On PAGE5:
    #For the image or icon URL-s:
        #Wikimedia

    #For the map type:
        #https://docs.mapbox.com/api/maps/styles/

