import json_loading
import tennis_odds
from odds_extract import player_names
import sqlite3

mozzart_df = []#tennis_odds.fetch_tennis_odds_mozzartbet()
soccer_df = []#tennis_odds.fetch_tennis_odds_soccerbet()
maxbet_df = []#tennis_odds.fetch_maxbet_odds()

#driver_1 = player_names.findTextBox()
#for index, row in maxbet_df.iterrows():
#    home_name = row['home_name']
#    away_name = row['away_name']

#    if '/' in home_name:
#        parts = home_name.split('/')
#        a = player_names.findPlayerName(parts[0], driver_1)
#        b = player_names.findPlayerName(parts[1], driver_1)

#        row['home_name'] = a + '/' + b
        #print(a + "/" + b, end=' - ')
        #for part in parts:
        #    a = player_names.findPlayerName(part, driver_1)
        #    b = player_names.findPlayerName(part, driver_1)
        #    print(a + "/" + b)
#    if '/' in away_name:
#        parts = away_name.split('/')
#        c = player_names.findPlayerName(parts[0], driver_1)
#        d = player_names.findPlayerName(parts[1], driver_1)
#        row['away_name'] = c + '/' + d
        #print(c + "/" + d, end='\n')
        #print()
#    else:
#        a = player_names.findPlayerName(home_name, driver_1)
 #       b = player_names.findPlayerName(away_name, driver_1)
 #       if a == 'Djokovic Marko':
 #           a = 'Djokovic Novak'
 #       elif b == 'Djokovic Marko':
 #           b = 'Djokovic Novak'
 #       row['home_name'] = a
 #       row['away_name'] = b

        #print(a + "-" + b)
###########
def execute():
    df_sup = tennis_odds.fetch_superbet_odds()

    print(df_sup.to_string())

###############

#https://www.sofascore.com/api/v1/search/all?q=Ostapenko&page=0


#df_mozz = spark_transformation.spark_creation(tennis_df)
#df_socc = spark_transformation.spark_creation(tennis_df_socc)

#max_odds_df = arbitrage_calculation_tennis.max_odds_fetch(df_mozz, df_socc)
#arbitrage_df = arbitrage_calculation_tennis.arbitrage_calculation(max_odds_df)
#arbitrage_df.show()

#maxbet_df.to_csv('maxbet.csv')
#tennis_df_socc.to_csv('socc.csv')
#tennis_df.to_csv('mozz.csv')

#df_ordered = arbitrage_df.orderBy("arbitrage_calc_ki").show()

#arbitrage_df.filter((arbitrage_df['arbitrage_calc_ki'] < 103)).show()


#mozzart_data = cursor.execute("SELECT * FROM mozzart_odds").fetchall()
#soccerbet_data = cursor.execute("SELECT * FROM soccerbet_odds").fetchall()
#maxbet_data = cursor.execute("SELECT * FROM maxbet_odds").fetchall()

#delete duplicates mozzart
#cursor.execute("create table duplicates_mozzart as \n with dupes_mozz as(select home_name, away_name, count() from mozzart_odds group by home_name, away_name having count(1)>1) select * from (select home_name, away_name, ki1, ki2, row_number() over (partition by home_name, away_name order by ki1 desc, ki2 desc) rnum from mozzart_odds where home_name || '-' || away_name in (select home_name || '-' || away_name from dupes_mozz)) where rnum = 1;")
#cursor.execute("delete from mozzart_odds where home_name || '-' || away_name || '' || ki1 = (select home_name || '-' || away_name || '' || ki1 from duplicates_mozzart);")



def execute_new():
    #mozzart_df_1 = tennis_odds.fetch_tennis_odds_mozzartbet()
    #print(mozzart_df_1.to_string())
    maxbet_df_1 = tennis_odds.fetch_maxbet_odds()
    print(maxbet_df_1.to_string())
    soccer_df_1 = tennis_odds.fetch_tennis_odds_soccerbet()
    print(soccer_df_1.to_string())
    superbet_df = tennis_odds.fetch_superbet_odds()
    print(superbet_df.to_string())
    conn = sqlite3.connect('/Users/luka/PycharmProjects/ods_extract_new/oddsNew.db')
    cursor = conn.cursor()

    #for index, row in mozzart_df_1.iterrows():
    #    home_name = row['home_name']
    #    away_name = row['away_name']
    #    ki1, ki2, first_1, first_2 = json_loading.loadOddsFromSofaScore(home_name + '-' + away_name)
    #    print(ki1, ki2, first_1, first_2)

    #mozzart_df_1.to_sql('mozzart_odds', conn, if_exists='replace', index=False)
    soccer_df_1.to_sql('soccerbet_odds', conn, if_exists='replace', index=False)
    maxbet_df_1.to_sql('maxbet_odds', conn, if_exists='replace', index=False)
    superbet_df.to_sql('superbet_odds', conn, if_exists='replace', index=False)
    cursor.close()
    conn.close()
    print("s")
    return 1


if __name__ == "__main__":
    execute_new()
    #execute()

#for row in maxbet_data:
#    print(row)

#for row in soccerbet_data:
#    print(row)

