# Connecting to MySQL server Localhost
import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


mydb = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
user="2Gzzgf7uUMuiWvf.root",
password="Vz7UELZ5l4AxGUPv",
database="Census2011"
)

print(mydb)
mycursor = mydb.cursor(buffered=True)

# StreamLit Queries 
def Query(Query_title,query):
    st.title(Query_title)
    mycursor.execute(query)
    out = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    query_dataframe = pd.DataFrame(out, columns = columns)
    query_dataframe.style.set_properties(**{'background-color': 'black','color': 'green'})
    st.dataframe(query_dataframe,use_container_width=False)

# Query 1 :Total population of each District
def Query_1(selectedoption):
    Query(selectedoption,"Select District, SUM(population) AS Population FROM  Census2011 GROUP BY district ORDER BY District")

# Query 2 :2.How many literate males and females are there in each district?
def Query_2(selectedoption):
    Query(selectedoption,"Select State_UT AS State, District, Male_Literate As Male_Literates,Literate_Female As Female_Literates FROM Census2011 ORDER BY State_UT")

# Query 3 : Percentage of workers in each district
def Query_3(selectedoption):
    Query(selectedoption,"Select State_Ut AS State,  District,(workers/ population) * 100 AS Percentage_of_Workers from census2011 ORDER BY State_UT")

# Query 4 : How many households have access to LPG or PNG as a cooking fuel in each district?
def Query_4(selectedoption):
    Query(selectedoption,"select State_UT AS State, District, LPG_or_PNG_Households As LPG_PNG_Households FROM Census2011 ORDER BY State_Ut")

# Query 5 : What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?
def Query_5(selectedoption):
    Query(selectedoption,"SELECT State_UT AS State,District, SUM(Hindus) AS Hindus, SUM(Muslims) AS Muslims, SUM(Christians) AS Christians,SUM(Sikhs) AS Sikhs, SUM(Buddhists) AS Buddhists, SUM(Jains) AS Jains, SUM(Others_Religions) AS Other_Religion, SUM(Religion_Not_Stated) AS Religion_Not_State FROM Census2011 GROUP BY  State_UT , District  ORDER BY State_UT")    

# Query 6 : How many households have internet access in each district?
def Query_6(selectedoption):
    Query(selectedoption, 
            "Select State_UT AS State, District, Households_with_Internet AS Household_Using_Internet FROM Census2011")

# Query 7 : What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?
def Query_7(selectedoption):
    Query(selectedoption,
            'select State_UT AS State, District, Below_Primary_Education, Primary_Education, Middle_Education, Secondary_Education, Higher_Education, Graduate_Education, Other_Education, Literate_Education, Illiterate_Education, Total_Education FROM Census2011.Census2011')

# Query 8 : How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?
def Query_8(selectedoption):
    Query(selectedoption, 
            'Select State_UT AS State, District, Households_with_Bicycle, Households_with_Car_Jeep_Van, Households_with_Radio_Transistor, Households_with_Scooter_Motorcycle_Moped FROM Census2011.Census2011')

# Query 9 : What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility with latrine facility, etc.) in each district?
def Query_9(selectedoption):
    Query(selectedoption, 'SELECT State_UT as State,District,Condition_of_occupied_census_houses_Dilapidated_Households AS Houses_Occupied_Diplated,Households_with_separate_kitchen_Cooking_inside_house AS Houses_Separate_Kitchen,Having_bathing_facility_Total_Households AS Houses_Bathing_facility,Having_latrine_facility_within_the_premises_Total_Households AS Houses_Latrine_facility,Not_having_bathing_facility_within_the_premises_Total_Households AS Houses_No_Bathing_facility,Not_having_latrine_facility_within_the_premises_Alternative_sour AS Houses_No_Latrine_facility FROM Census2011')

# Query 10 : How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?
def Query_10(selectedoption):
    Query(selectedoption,'Select State_UT AS State, District,  Household_size_1_person_Households AS 1_Person_Household, Household_size_2_persons_Households AS 2_Persons_Household, Household_size_1_to_2_persons AS 1_to_2_Persons_Household,Household_size_3_persons_Households AS 3_Persons_Households, Household_size_4_persons_Households AS 4_Persons_Households,Household_size_5_persons_Households AS 5_Persons_Households, Household_size_3_to_5_persons_Households AS 3_to_5_Persons_Households,Household_size_6_8_persons_Households AS 6_to_8_Persons_Households, Household_size_9_persons_and_above_Households AS More_than_9_Persons FROM Census2011.Census2011 ORDER BY State_UT')

# Query 11 : What is the total number of households in each state?
def Query_11(selectedoption):
    Query(selectedoption,'Select State_UT AS State, SUM(Households) AS Total_Households FROM Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 12 : How many households have a latrine facility within the premises in each state?
def Query_12(selectedoption):
    Query(selectedoption,'select State_UT AS State, SUM(Having_latrine_facility_within_the_premises_Total_Households) AS Households_having_latrine_facility_within_the_premises FROM Census2011.Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 13 : What is the average household size in each state?
def Query_13(selectedoption):
    Query(selectedoption,'Select State_UT AS State, ROUND(AVG(Household_size_1_person_Households), 2) AS Average_of_1_person_houses, ROUND(AVG(Household_size_2_persons_Households), 2) AS Average_of_2_person_houses, ROUND(AVG(Household_size_1_to_2_persons), 2) AS Average_of_1_to_2_person_houses, ROUND(AVG(Household_size_3_persons_Households), 2) AS Average_of_3_person_houses,ROUND(AVG(Household_size_4_persons_Households), 2) AS Average_of_4_person_houses,ROUND(AVG(Household_size_5_persons_Households), 2) AS Average_of_5_person_houses, ROUND(AVG(Household_size_3_to_5_persons_Households), 2) AS Average_of_3_to_5_persons_houses,ROUND(AVG(Household_size_6_8_persons_Households), 2) AS Average_of_6_to_8_persons_houses,ROUND(AVG(Household_size_9_persons_and_above_Households), 2) AS Average_of_9_and_above_persons FROM Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 14 : How many households are owned versus rented in each state?
def Query_14(selectedoption):
    Query(selectedoption,'select State_UT AS State, SUM(Ownership_Owned_Households) AS Owned_Houses, SUM(Ownership_Rented_Households) AS Rented_Houses FROM Census2011.Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 15 : What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?
def Query_15(selectedoption):
    Query(selectedoption,'select State_UT AS State, SUM(Type_of_latrine_facility_Pit_latrine_Households) AS Pit_Latrine,SUM(Type_of_latrine_facility_Night_soil_disposed_into_open_drain) AS Night_soil_disposed_into_open_drain_Latrine,SUM(Type_of_latrine_Flush_pour_connected_to_other_system_Households) AS Flush_or_Pour_Latrine, SUM(Type_of_latrine_facility_Other_latrine_Households) AS Other_Latrine_types FROM Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 16 : How many households have access to drinking water sources near the premises in each state?
def Query_16(selectedoption):
    Query(selectedoption,'select State_UT AS State,SUM(Location_of_drinking_water_source_Near_the_premises_Households) AS Households_with_drinking_water_source_Near_the_premises FROM Census2011.Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 17 : What is the average household income distribution in each state based on the power parity categories?
def Query_17(selectedoption):
    Query(selectedoption,'select State_UT AS State, ROUND(AVG(Power_Parity_Less_than_Rs_45000), 2) AS Avg_Power_Parity_Less_than_Rs_45000, ROUND(AVG(Power_Parity_Rs_45000_90000), 2) AS Avg_Power_Parity_Rs_45000_90000, ROUND(AVG(Power_Parity_Rs_90000_150000), 2) AS Avg_Power_Parity_Rs_90000_150000,ROUND(AVG(Power_Parity_Rs_45000_150000), 2) AS Avg_Power_Parity_Rs_45000_150000,ROUND(AVG(Power_Parity_Rs_150000_240000), 2) AS Avg_Power_Parity_Rs_150000_240000,ROUND(AVG(Power_Parity_Rs_240000_330000), 2) AS Avg_Power_Parity_Rs_240000_330000, ROUND(AVG(Power_Parity_Rs_150000_330000), 2) AS Avg_Power_Parity_Rs_150000_330000,ROUND(AVG(Power_Parity_Rs_330000_425000), 2) AS Avg_Power_Parity_Rs_330000_425000, ROUND(AVG(Power_Parity_Rs_425000_545000), 2) AS Avg_Power_Parity_Rs_425000_545000, ROUND(AVG(Power_Parity_Rs_330000_545000), 2) AS Avg_Power_Parity_Rs_330000_545000, ROUND(AVG(Power_Parity_Above_Rs_545000), 2) AS Avg_Power_Parity_Above_Rs_545000 FROM Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 18 : What is the percentage of married couples with different household sizes in each state?
def Query_18(selectedoption):
    Query(selectedoption,'select State_UT AS State, ROUND(SUM(Married_couples_1_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_1_Households, ROUND(SUM(Married_couples_2_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_2_Households, ROUND(SUM(Married_couples_3_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_3_Households, ROUND(SUM(Married_couples_3_or_more_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_3_or_more_Households, ROUND(SUM(Married_couples_4_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_4_Households,ROUND(SUM(Married_couples_5__Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_5__Households, ROUND(SUM(Married_couples_None_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_None_Households FROM Census2011 GROUP BY State_UT ORDER BY State_UT')

# Query 19 : How many households fall below the poverty line in each state based on the power parity categories?
def Query_19(selectedoption):
    Query(selectedoption,'select State_UT As State, SUM(Power_Parity_Less_than_Rs_45000) AS Households_below_poverty_line FROM Census2011.Census2011 GROUP BY State_UT')

# Query 20 : What is the overall literacy rate (percentage of literate population) in each state?
def Query_20(selectedoption):
    Query(selectedoption, 'select State_UT AS State, Round(SUM(Literate)/SUM(Population) * 100,2) AS Percentage_of_Literacy FROM Census2011.Census2011 GROUP BY State_UT Order by State_UT')

# Main Query

def main():
    st.title("Census Pipeline Project : Queries")
    options = ['District Wise Population', 
               'Male and Female Literate in Each District',
                'Percentage of Workers in each district', 
                'Households with LPG or PNG as Cooking fuel',
                'District Wise Religious Composition', 
                'District Wise Households with Internet',
                'District Wise Educational Qualification',
                'District Wise Access to Modes of Transport', 
                'District Wise Condition of Occupied Houses',
                'District Wise Distribution of Household', 
                'State Wise Household Size', 
                'State Wise Households having Latrine facility within the Premises', 
                'State Wise Household Size',
                'State Wise Owned versus rented houses', 
                'State Wise Distribution of of latrine facilities',
                'State Wise Houeholds with Drinking Water Sources near the Premises',
                'State Wise Houeholds with Drinking Water Sources near the Premises',
                'State Wise Percentage of married couples with different household sizes',
                'State Wise Households below Poverty Line', 
                'State Wise Literacy Rate']

    selectedoption = st.selectbox("Choose an option :",options = options, index = None, placeholder = 'Select Option to See Results')
    if selectedoption == 'District Wise Population':
       Query_1(selectedoption)
    elif selectedoption == 'Male and Female Literate in Each District':
        Query_2(selectedoption)
    elif selectedoption == 'Percentage of Workers in each district':
        Query_3(selectedoption)
    elif selectedoption == 'Households with LPG or PNG as Cooking fuel':
        Query_4(selectedoption)
    elif selectedoption == 'District Wise Religious Composition':
        Query_5(selectedoption)
    elif selectedoption == 'District Wise Households with Internet':
        Query_6(selectedoption)
    elif selectedoption == 'District Wise Educational Qualification':
        Query_7(selectedoption)
    elif selectedoption == 'District Wise Access to Modes of Transport':
        Query_8(selectedoption)
    elif selectedoption == 'District Wise Condition of Occupied Houses':
        Query_9(selectedoption)
    elif selectedoption == 'District Wise Distribution of Household':
        Query_10(selectedoption)
    elif selectedoption == 'State Wise Household Size':
        Query_11(selectedoption)
    elif selectedoption == 'State Wise Households having Latrine facility within the Premises':
        Query_12(selectedoption)
    elif selectedoption == 'State Wise Household Size':
        Query_13(selectedoption)
    elif selectedoption == 'State Wise Owned versus rented houses':
        Query_14(selectedoption)
    elif selectedoption == 'State Wise Distribution of of latrine facilities':
        Query_15(selectedoption)
    elif selectedoption == 'State Wise Houeholds with Drinking Water Sources near the Premises':
        Query_16(selectedoption)
    elif selectedoption == 'State Wise Average household income distribution':
        Query_17(selectedoption)
    elif selectedoption == 'State Wise Percentage of married couples with different household sizes':
        Query_18(selectedoption)
    elif selectedoption == 'State Wise Households below Poverty Line':
        Query_19(selectedoption)
    elif selectedoption == 'State Wise Literacy Rate':
        Query_20(selectedoption)
    else:
        st.write("Choose an option to Display Results")

main()
